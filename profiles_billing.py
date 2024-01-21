import os
import json
import csv
import requests


# Fetch secret values from environment variables
client_id = "cdeddf8a-5208-4822-b65e-4317f28f2124"
client_secret = os.environ["CLIENT_SECRET"]



token_url = "https://login.microsoftonline.com/2b764c26-32e2-4258-bea0-78bfc55d48fe/oauth2/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": "https://graph.windows.net"
}

# Obtain the access token
token_response = requests.post(token_url, data=token_data)
access_token = token_response.json().get("access_token")

# Specify the API version and customer_id
api_version = "1.0"  # Adjust the version accordingly
customer_id = "6b35628c-c50e-4255-9eaa-c14f130d789d"  # Replace with the actual customer_id

api_url = f"https://api.partnercenter.microsoft.com/v{api_version}/customers/{customer_id}/profiles/billing"

# Make the API request
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(api_url, headers=headers)
print(response.text)  # Print the response content

if response.status_code == 200:
    # Your processing logic for a successful response goes here
    pass
else:
    print(f"Error: {response.status_code} - {response.text}")
