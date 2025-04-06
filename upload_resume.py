import os
from azure.storage.blob import BlobServiceClient

# Azure Blob Storage Connection
AZURE_STORAGE_CONNECTION_STRING = "your_blob_connection_string"
CONTAINER_NAME = "resumes"

def upload_resume(file_path):
	# Create the BlobServiceClient object
	blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
	# Get a reference to the container
	container_client = blob_service_client.get_container_client(CONTAINER_NAME)
	# Get the file name
	file_name = os.path.basename(file_path)
	# Upload the file
	with open(file_path, "rb") as data:
		container_client.upload_blob(name=file_name, data=data)





    
