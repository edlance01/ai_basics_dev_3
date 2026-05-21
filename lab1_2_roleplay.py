import os
from openai import OpenAI

client = OpenAI()

user_query = input("Ask a question:  ")

# Define the System persona 
robot_system = "You are a highly sarcastic robot who hates answering questions but does so anyway."

knight_system = "You are a noble medieval knight from the round table.  Speak only in Old English style."

# Call 1: Sarcastic Robot (Low temperature = precise, focused)
response_robot = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": robot_system},
        {"role": "user", "content": user_query}
    ],
    temperature=0.2
)   

# Call 2: Medieval Knight (High temperature = creative, varied)
response_knight = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": knight_system},
        {"role": "user", "content": user_query}
    ],
    temperature=1.0
)

print("\n--- Sarcastic Robot Response ---")
print(response_robot.choices[0].message.content.strip())

print("\n--- Medieval Knight Response ---")
print(response_knight.choices[0].message.content.strip())