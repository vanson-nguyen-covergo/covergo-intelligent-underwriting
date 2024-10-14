from pydantic import BaseModel, Field
from typing import List

class MotorInsuranceRequest(BaseModel):
    age: int = Field(..., description="Age of the driver in years.")
    driving_experience: int = Field(..., description="Number of years the driver has been driving.")
    claims_history: int = Field(..., description="Number of past insurance claims made by the driver.")
    vehicle_model: str = Field(..., description="The make and model of the vehicle.")
    vehicle_age: int = Field(..., description="Age of the vehicle in years.")
    vehicle_use: str = Field(..., description="Usage type of the vehicle (personal or commercial).")
    location: str = Field(..., description="Location where the vehicle is primarily used (urban, New Territories, etc.).")
    annual_mileage: int = Field(..., description="Estimated annual mileage of the vehicle in kilometers.")
    parking: str = Field(..., description="Type of parking used (garage, street, etc.).")
    driving_history: str = Field(..., description="History of traffic violations or driving offenses (e.g., clean, minor offenses).")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 35,
                "driving_experience": 15,
                "claims_history": 0,
                "vehicle_model": "Honda Civic",
                "vehicle_age": 3,
                "vehicle_use": "personal",
                "location": "urban",
                "annual_mileage": 10000,
                "parking": "garage",
                "driving_history": "clean"
            }
        }

class PremiumRange(BaseModel):
    min: float
    max: float

class DetailItem(BaseModel):
    category_code: str = Field(..., description="The code representing the category of the assessment (e.g., AGE_EXP, VEHICLE_USE).")
    answer: str = Field(..., description="Detailed explanation or justification for the risk factor in this category.")
    score: float = Field(..., description="The risk score for this category, ranging from 0 to 1.")

    class Config:
        json_schema_extra = {
            "example": {
                "category_code": "AGE_EXP",
                "answer": "At 55 years old with only 2 years of driving experience, the driver is still relatively inexperienced, especially in an urban setting like Hong Kong. The lack of extensive driving experience at an older age poses a significant risk due to potential slower reaction times and less familiarity with complex traffic situations.",
                "score": 0.8
            }
        }

class MotorInsuranceResponse(BaseModel):
    riskLevel: str
    premiumRange: List[PremiumRange]
    score: float
    detail: List[DetailItem]

    class Config:
        json_schema_extra = {
            "example": {
                "riskLevel": "Medium",
                "premiumRange": [
                    {"min": 2000.0, "max": 3500.0}
                ],
                "score": 0.75,
                "detail": [
                    {
                        "category_code": "AGE_EXP",
                        "answer": "The driver has a moderate amount of driving experience for their age, which reduces the overall risk.",
                        "score": 0.8
                    }
                ]
            }
        }

