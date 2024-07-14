# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="TheBloke/una-cybertron-7B-v2-GGUF",
  messages=[
    {"role": "system", "content": "You are a wold class soccer player"},
    {"role": "user", "content": "how many  worldcup maches played by Pele "}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)