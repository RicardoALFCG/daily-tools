import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json


# Load environment variables from .env file
load_dotenv()

# Fetching values from the .env file
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = os.getenv("PROJECT_KEY")

# Construct the API endpoint URL
url = f'https://{JIRA_DOMAIN}/rest/api/3/search'

# Define the JQL query to fetch issues from a specific project
jql_query = f'project={PROJECT_KEY}'

# Set up the request headers
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Set up authentication
auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

# Define the request payload
payload = {
    'jql': jql_query,
    'maxResults': 50,  # Adjust the number as needed
    'fields': ['summary', 'status', 'assignee']  # Specify fields to retrieve
}

# Make the API request
response = requests.post(url, headers=headers, auth=auth, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    issues = response.json().get('issues', [])
    for issue in issues:
        print(f"Issue Key: {issue['key']}, Summary: {issue['fields']['summary']}")
else:
    print(f"Failed to fetch issues: {response.status_code} - {response.text}")
