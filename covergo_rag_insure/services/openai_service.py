import json
from pymemcache.client import base
import os
import time
import openai
from covergo_rag_insure.common.logger import logger

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
cache = base.Client(('localhost', 11211))

# Configure the OpenAI API key

def call_openai_api(request_id, messages: list):
    """
    Calls the OpenAI API with the provided messages to assess risk.
    
    Args:
        messages (list): The list of messages for the OpenAI API.
    
    Returns:
        str: The response from the OpenAI API.
    """
    time.sleep(5)
    logger.info(f"OpenAI request")
    
    request_bytes = cache.get(request_id)
    request = json.loads(request_bytes.decode('utf-8'))
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300,
            temperature=0.7
        )

        response = response.choices[0].message.content
    
        logger.info(f"OpenAI response: {response}")
        
        request['status'] = 'completed'
        request['result'] = response
        cache.set(request_id, json.dumps(request))

    except Exception as e:
        request['status'] = 'failed'
        request['result'] = str(e)
        cache.set(request_id, json.dumps(request))
