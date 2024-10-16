import requests
import os

# Set up the API key and file paths
CHUNKR_API_KEY = os.getenv("CHUNKR_API_KEY")
FILE_PATH = "covergo_rag_insure/chunkr-pdf/Sample_HK_ID_Card.pdf"

# Define the POST request to start the task
url_post = "https://api.chunkr.ai/api/v1/task"
headers_post = {
    "Authorization": CHUNKR_API_KEY
}
files = {
    "file": (FILE_PATH, open(FILE_PATH, "rb")),
    "model": (None, "HighQuality"),
    "target_chunk_length": (None, "512"),
    "ocr_strategy": (None, "Auto")
}

# Make the POST request
response = requests.post(url_post, headers=headers_post, files=files)

if response.status_code == 200:
    response_data = response.json()
    task_id = response_data.get("task_id")
    print(f"Task started successfully with ID: {task_id}")
else:
    print(f"Failed to start the task. Status Code: {response.status_code}, Response: {response.text}")
    exit()

# Define the GET request to get the status of the task
url_get = f"https://api.chunkr.ai/api/v1/task/{task_id}"
headers_get = {
    "Authorization": CHUNKR_API_KEY
}

# Polling until task completion (example)
import time

while True:
    response = requests.get(url_get, headers=headers_get)
    if response.status_code == 200:
        task_data = response.json()
        status = task_data.get("status")
        print(f"Task status: {status}")

        if status == "Succeeded":
            # Print the result or process it accordingly
            print("Task completed:", task_data)
            break
        elif status == "failed":
            print("Task failed:", task_data)
            break
    else:
        print(f"Failed to get the task status. Status Code: {response.status_code}, Response: {response.text}")
        break

    time.sleep(5)  # Sleep for 5 seconds before polling again
