import requests

# Azure AI Document Intelligence Endpoint & Key
AI_ENDPOINT = "your_ai_endpoint"
AI_KEY = "your_ai_key"

def extract_resume_data(blob_url):
    # Prepare the request headers
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": AI_KEY
    }
    # Prepare the request body
    body = {
        "source": blob_url
    }
    # Make the request to the AI service
    response = requests.post(AI_ENDPOINT, headers=headers, json=body)
    # Return the extracted data
    return response.json()