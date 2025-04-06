import requests

# Microsoft Graph API Credentials
GRAPH_API_URL = "https://graph.microsoft.com/v1.0/me/events"
ACCESS_TOKEN = "your_access_token"

def schedule_interview(candidate_name, candidate_email):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    meeting_data = {
        "subject": f"Interview with {candidate_name}",
        "attendees": [{"emailAddress": {"address": candidate_email}, "type": "required"}],
        "start": {"dateTime": "2025-03-20T10:00:00", "timeZone": "UTC"},
        "end": {"dateTime": "2025-03-20T11:00:00", "timeZone": "UTC"},
        "location": {"displayName": "Microsoft Teams Meeting"},
        "isOnlineMeeting": True,
        "onlineMeetingProvider": "teamsForBusiness"
    }
    response = requests.post(GRAPH_API_URL, json=meeting_data, headers=headers)
    return response.json()

meeting_response = schedule_interview("Alice", "alice@example.com")
print(meeting_response)