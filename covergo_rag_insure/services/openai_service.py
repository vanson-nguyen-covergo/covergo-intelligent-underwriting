import os
import logging
import openai

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configure the OpenAI API key

def call_openai_api(messages: list) -> str:
    """
    Calls the OpenAI API with the provided messages to assess risk.
    
    Args:
        messages (list): The list of messages for the OpenAI API.
    
    Returns:
        str: The response from the OpenAI API.
    """
    logging.info(f"OpenAI request")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )

    response = response.choices[0].message.content
    
    logging.info(f"OpenAI response: {response}")

    return response
