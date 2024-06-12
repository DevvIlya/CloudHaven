import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

api_token = os.getenv('API_TOKEN')

if not api_token:
    raise ValueError("API_TOKEN is not found in the environment variables")

headers = {
    'Authorization': f'Token {api_token}',
    'Content-Type': 'application/json',
}

# Правильный URL для доступа к UserViewSet
url = 'http://localhost:8000/users/'

response = requests.get(url, headers=headers)

print(f'Status Code: {response.status_code}')
print(f'Response Text: {response.text}')

try:
    response_json = response.json()
    print(response_json)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format")

