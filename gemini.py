
import requests
import json
import sys

# Replace 'YOUR_API_KEY' with your actual Google Cloud API key

API_KEY = 'AIzaSyBWbMAWoa9d9qHhktz-627CRi81qfrKefU'  # Placeholder for your API key
text = ''
if len(sys.argv) > 1:
    text = sys.argv[1]

# Define the URL endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

# Prepare the request data
data = {
    "contents": [
        {
            "parts": [
                {"text": text}
            ]
        }
    ]


}

# Set the headers
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Check for successful response
if response.status_code == 200:
  # Parse the JSON response
  response_data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  # Access the generated text
  print(response_data)
else:
  print(f"Error: {response.status_code}")