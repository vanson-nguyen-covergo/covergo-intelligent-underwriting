from fastapi import APIRouter
from covergo_rag_insure.schemas.motor_insurance import MotorInsuranceRequest, MotorInsuranceResponse
from covergo_rag_insure.services.motor_insure import assess_motor_insurance_risk

router = APIRouter()

@router.post("/assess", response_model=MotorInsuranceResponse)
async def assess_motor_insurance(data: MotorInsuranceRequest):
    """
    Endpoint to assess the motor insurance risk.
    
    This endpoint takes in a motor insurance request and returns an assessment of the risk
    level and suggested premium range based on the provided data.
    """
    result = assess_motor_insurance_risk(data)
    return result
