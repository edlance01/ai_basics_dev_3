
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI


app = FastAPI(title="My First AI API")
client = OpenAI()

# Define the structure of data we expect from the user
class TextRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_ai_text(request: TextRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": request.prompt}
        ]
    )

    ai_message = response.choices[0].message.content

# FastAPI automatically serializes dictionaires into clean JSON responses
    return {"status": "success", "ai_response": ai_message}

