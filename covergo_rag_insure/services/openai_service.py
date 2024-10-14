# covergo_rag_insure/services/openai_service.py

import openai
import os

# Configure the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai_api(messages: list) -> str:
    """
    Calls the OpenAI API with the provided messages to assess risk.
    
    Args:
        messages (list): The list of messages for the OpenAI API.
    
    Returns:
        str: The response from the OpenAI API.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )

    return response.choices[0].message['content']
