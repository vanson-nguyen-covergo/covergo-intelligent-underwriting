import json
from pymemcache.client import base
from fastapi import APIRouter, BackgroundTasks
from covergo_rag_insure.schemas.motor_insurance import MotorInsuranceRequest, MotorInsuranceResponse
from covergo_rag_insure.services.motor_insure import assess_motor_insurance_risk

router = APIRouter()
cache = base.Client(('localhost', 11211))

@router.post("/assess", response_model=dict)
async def assess_motor_insurance(data: MotorInsuranceRequest, background_tasks: BackgroundTasks, request_store: dict):
    """
    Endpoint to assess the motor insurance risk.
    
    This endpoint takes in a motor insurance request and returns an assessment of the risk
    level and suggested premium range based on the provided data.
    """
    
    result = assess_motor_insurance_risk(data, background_tasks)
    return {
        "data": {
            "request_id": result
        }
    }

@router.get("/assess/{request_id}", response_model=dict)
async def get_assess_detail(request_id: str):
    """
    Endpoint to get the assess detail.
    """
    request_bytes = cache.get(request_id)
    
    if not request_bytes:
        return {"error": "Request ID not found"}
    
    request = json.loads(request_bytes.decode('utf-8'))
    
    return {
        "data": request
    }