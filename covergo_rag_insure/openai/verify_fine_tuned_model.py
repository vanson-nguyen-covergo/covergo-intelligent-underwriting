import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step to verify fine tune model
# 1. Fine-tuning on your current dataset
# 2. Fine-tuning on half of your current dataset
# 3. Observing the quality gap between the two

def build_chat_message() -> list[str]:
   messages = [
    {"role": "system", "content": "You are an insurance expert who answers questions based on AXA iMotor Insurance."},
    {"role": "user", "content": f"""
      Given the details of a motor insurance application, assess the risk level (Low, Medium, High) 
        and suggest an appropriate premium range in HKD.

        Details:
        - Age of the driver: 50
        - Driving experience (years): 20
        - Number of past claims: 5
        - Vehicle make and model: Honda Civic 2021
        - Vehicle age (years): 2
        - Vehicle use (personal/commercial): personal
        - Location in HK (urban, New Territories, etc.): New Territories
        - Annual mileage: 100000km
        - Parking situation (street, garage): street
        - Driving history (e.g., traffic violations): clean

        Based on the above information, provide:
        1. Risk level (Low, Medium, High)
        2. Suggested premium range in HKD (e.g., HKD 2,000 - 3,500)
        3. Justification for the risk level, considering local factors in Hong Kong
      """
    }
   ]
   return messages

def verify_fine_tuned_model(fine_tuned_model_id):

  completion = client.chat.completions.create(
    model=fine_tuned_model_id,
    messages=build_chat_message(),
    max_tokens=100,
    temperature=0.7
  )
  
  return completion.choices[0].message

fine_turning_jobs = client.fine_tuning.jobs.list(limit=100)
latest_job = sorted(fine_turning_jobs.data, key=lambda x: x.created_at, reverse=True)[0]

message = verify_fine_tuned_model(latest_job.fine_tuned_model)
print(f"OpenAI messgae\n {message}")