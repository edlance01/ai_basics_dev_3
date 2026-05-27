
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from openai import OpenAI

app = FastAPI(title="Production-Ready Travel API")
client = OpenAI()

# Nested schema structure to ensure rigorous validation of past conversation context
class ChatTurn(BaseModel):
    role: str  # system, user, or assistant
    content: str

class HistoryChatRequest(BaseModel):
    history: List[ChatTurn]
    new_message: str

@app.post("/api/travel/chat")
def continuous_travel_chat(request: HistoryChatRequest):
    # 1. Convert incoming Pydantic models back into standard dicts for the OpenAI SDK
    formatted_messsages = [{"role": turn.role, "content": turn.content} for turn in request.history]

    # If history is completely empty, insert our baseline system context
    if not any(msg['role'] == 'system' for msg in formatted_messsages):
        formatted_messsages .insert(0, {"role": "system", "content": "You are a professional travel agent expert."})

    # 2. Append the new user message to the conversation history
    formatted_messsages.append({"role": "user", "content": request.new_message})
    
    # 3. Request completion from Open AI 
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=formatted_messsages 
                                        
    )

    ai_reply = response.choices[0].message.content

    # 4. Append AI answer to update our status tracking array 
    formatted_messsages.append({"role": "assistant", "content": ai_reply})  

    # 5. Return the AI's response and the updated conversation history to the client
    #return {"updated_history": formatted_messsages}
    return {"updated_history": formatted_messsages, "ai_reply": ai_reply}
                                       
