from azure.cosmos import CosmosClient

# Cosmos DB Connection
COSMOS_ENDPOINT = "your_cosmos_db_endpoint"
COSMOS_KEY = "your_cosmos_key"
DATABASE_NAME = "HR"
CONTAINER_NAME = "Candidates"

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def save_candidate(candidate_data):
    container.upsert_item(candidate_data)
    print("Candidate data saved successfully")

# Example Data
candidate = {
    "id": "123",
    "name": "Alice",
    "email": "alice@example.com",
    "skills": ["Python", "Azure", "AI"],
    "experience": 4,
    "score": 85
}

save_candidate(candidate)