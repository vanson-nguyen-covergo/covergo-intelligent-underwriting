from typing import List
from covergo_rag_insure.schemas.motor_insurance import DetailItem, MotorInsuranceRequest, MotorInsuranceResponse, PremiumRange
from covergo_rag_insure.services.openai_service import call_openai_api

def map_sample_details() -> List[DetailItem]:
    details_data = [
    {
        "category_code": "AGE_EXP",
        "answer": "At 55 years old with only 2 years of driving experience, the driver is still relatively inexperienced, especially in an urban setting like Hong Kong. The lack of extensive driving experience at an older age poses a significant risk due to potential slower reaction times and less familiarity with complex traffic situations.",
        "score": 0.8
    },
    {
        "category_code": "NUMBER_OF_PAST_CLAIMS",
        "answer": "Having 20 past claims is a substantial risk factor, suggesting a history of frequent incidents. This pattern indicates a higher probability of future claims, significantly increasing the risk for insurers.",
        "score": 0.8
    },
    {
        "category_code": "VEHICLE_MAKE_MODEL_AGE",
        "answer": "The Peugeot Partner, while suitable for various purposes, may be more challenging to maneuver in tight urban spaces compared to smaller vehicles. Although the car is relatively new at 3 years old, its usage profile still contributes to an elevated risk level.",
        "score": 0.8
    },
    {
        "category_code": "VEHICLE_USE",
        "answer": "While the vehicle is designated for personal use, the annual mileage of 100,000 km is exceptionally high for personal purposes. High mileage increases the exposure to accidents and general wear and tear, thus elevating the overall risk.",
        "score": 0.8
    },
    {
        "category_code": "LOCATION",
        "answer": "At 55 years old with only 2 years of driving experience, the driver is still relatively inexperienced, especially in an urban setting like Hong Kong. The lack of extensive driving experience at an older age poses a significant risk due to potential slower reaction times and less familiarity with complex traffic situations.",
        "score": 0.8
    },
    {
        "category_code": "ANNUAL_MILEAGE",
        "answer": "With 100,000 km driven annually, the risk exposure is substantially higher than that of the average driver. The high mileage correlates with an increased likelihood of accidents due to more time spent on the road.",
        "score": 0.8
    },
    {
        "category_code": "PARKING_SITUATION",
        "answer": "Street parking further elevates the risk due to the increased likelihood of theft, vandalism, and accidental damage compared to a more secure parking environment like a garage.",
        "score": 0.8
    },
    {
        "category_code": "DRIVING_HISTORY",
        "answer": "Street parking further elevates the risk due to the increased likelihood of theft, vandalism, and accidental damage compared to a more secure parking environment like a garage.",
        "score": 0.8
    }
    ]

    return [DetailItem(**item) for item in details_data]


def assess_motor_insurance_risk(data: MotorInsuranceRequest) -> MotorInsuranceResponse:
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

    response = call_openai_api(messages)
    
    return MotorInsuranceResponse(
        riskLevel="Low",
        premiumRange=[PremiumRange(min=2000.0, max=3500.0)],
        score=0.7,
        detail=map_sample_details()
    )
