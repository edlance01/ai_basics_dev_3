import os
from openai import OpenAI

# Initialize the OpenAI client, it will automatically read the OPENAI_API_KEY from the environment variable
client = OpenAI()

print("Sending request to OpenAI...")


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Summarize why Python is the preferred language for AI in exactly two sentences."},
    ],
)

# Print the response from the model
print("Response from OpenAI:")
print(response)

# Exact and print just the text content of the response
print("\nExtracted content:")
print(response.choices[0].message.content)