import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

input = "How to Build a Weather Station With Elixir"

response = client.embeddings.create(
  model="text-embedding-3-small",
  input=input
)

print(response.data[0].embedding)
print(np.array(response.data[0].embedding))