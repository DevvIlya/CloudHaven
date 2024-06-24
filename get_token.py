import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

BASE_URL = os.getenv('BASE_URL', 'http://localhost:8000')
USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME')
PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not BASE_URL or not USERNAME or not PASSWORD:
    print("Не удалось загрузить необходимые переменные окружения.")
    exit(1)

# Запрос на получение токена
try:
    response = requests.post(f'{BASE_URL}/api-token-auth/', data={
        'username': USERNAME,
        'password': PASSWORD
    })

    response.raise_for_status()  # Проверка на ошибки HTTP
    token = response.json().get('token')

    if token:
        print(f'Token: {token}')

        # Обновление файла .env
        with open('.env', 'a') as f:
            f.write(f'\nAPI_TOKEN={token}\n')
    else:
        print("Токен не получен.")
except requests.exceptions.RequestException as e:
    print(f'Произошла ошибка при запросе на получение токена: {e}')

