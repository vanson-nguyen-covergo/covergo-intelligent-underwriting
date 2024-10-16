import json
from typing import List
import uuid
from pymemcache.client import base

from fastapi import BackgroundTasks
from covergo_rag_insure.schemas.motor_insurance import MotorInsuranceRequest, MotorInsuranceResponse, PremiumRange
from covergo_rag_insure.services.openai_service import call_openai_api

def assess_motor_insurance_risk(data: MotorInsuranceRequest, background_tasks: BackgroundTasks):
    """
    Assess the motor insurance risk by preparing the OpenAI messages
    and making a call to the OpenAI API.
    
    Args:
        data (MotorInsuranceRequest): The motor insurance request data.
        
    Returns:
        MotorInsuranceResponse: The risk assessment response.
    """
    
    messages = [
        {"role": "system", "content": "You are an insurance risk assessment expert specializing in the Hong Kong market."},
        {"role": "user", "content": f"""
        Given the details of a motor insurance application, assess the risk level (Low, Medium, High) 
        and suggest an appropriate premium range in HKD.

        Details:
        - Age of the driver: {data.age}
        - Driving experience (years): {data.driving_experience}
        - Number of past claims: {data.claims_history}
        - Vehicle make and model: {data.vehicle_model}
        - Vehicle age (years): {data.vehicle_age}
        - Vehicle use (personal/commercial): {data.vehicle_use}
        - Location in HK (urban, New Territories, etc.): {data.location}
        - Annual mileage: {data.annual_mileage}
        - Parking situation (street, garage): {data.parking}
        - Driving history (e.g., traffic violations): {data.driving_history}

        Based on the above information, provide:
        1. Risk level (Low, Medium, High)
        2. Suggested premium range in HKD (e.g., HKD 2,000 - 3,500)
        3. Justification for the risk level, considering local factors in Hong Kong
        """}
    ]
    
    client = base.Client(('localhost', 11211))
    request_id = str(uuid.uuid4())
    client.set(request_id, json.dumps({
        'status': 'in_progress',
        'result': None,
    }))
    

    background_tasks.add_task(call_openai_api, request_id, messages)
    
    return request_id
