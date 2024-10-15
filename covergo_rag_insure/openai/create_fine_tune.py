import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = "gpt-3.5-turbo"

def create_fine_tune_axa() -> str:
  # The maximum file upload size is 1 GB, though we do not suggest fine-tuning 
  # with that amount of data since you are unlikely to need that large of an amount to see improvements.
  file = client.files.create(
    file=open("./covergo_rag_insure/openai/axa_underwriting_data_prompt.jsonl", "rb"),
    purpose="fine-tune"
  )
  job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model=model
  )
  
  return job.id
  

job_id = create_fine_tune_axa()
print(f"Fine tuning job id: {job_id}")