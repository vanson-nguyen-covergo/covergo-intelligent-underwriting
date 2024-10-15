from openai import OpenAI
import os

# Set OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_failed_finetuning_jobs(limit=100):
    """
    This function lists fine-tuning jobs and deletes the ones with a status of 'failed'.
    
    Args:
    limit (int): Maximum number of jobs to retrieve (default is 100).
    
    Returns:
    None
    """
    
    # Retrieve the fine-tuning jobs
    fine_tuning_jobs = client.fine_tuning.jobs.list(limit=limit)
    
    failed_jobs = [job for job in fine_tuning_jobs.data if job.status == 'failed']
    
    if not failed_jobs:
        print("No failed fine-tuning jobs found.")
        return

    # Loop through failed jobs and delete them
    for job in failed_jobs:
        print(f"Deleting failed job: {job.id}, created at {job.created_at}")
        try:
            client.fine_tuning.jobs.cancel(job.id)
            print(f"Successfully deleted fine-tuning job {job.id}.")
        except Exception as e:
            print(f"Failed to delete fine-tuning job {job.id}: {e}")

if __name__ == "__main__":
    clean_failed_finetuning_jobs(limit=100)
