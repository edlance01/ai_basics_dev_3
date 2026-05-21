import os
from openai import OpenAI

# TODO add some token tracking here

client = OpenAI()

# memory starts here, the api is stateless
chat_history = [
     {"role": "system", "content": "You are a friendly, enthusiastic travel buddy assistant."}
]

print("Travel Chatbot Initialized! Type 'exit' to quit.")
print("-------------------------------------------------")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # 1. Append the new user message to history
    chat_history.append({"role": "user", "content": user_input})

    # 2. Send the cummulative history to the API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    ai_answer = response.choices[0].message.content
    print(f"Travel Buddy: {ai_answer}")

    # 3. Append the AI's answer so it remembers what it said next time
    chat_history.append({"role": "assistant", "content": ai_answer})