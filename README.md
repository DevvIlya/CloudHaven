# Облачное хранилище Cloud Haven

## инструкция по запуску

+ **Скачать проект**

создать файл .env в корне проекта

скопировать в него код и подставить свои значения. Без пробела.

  ```
  POSTGRES_DB=
  POSTGRES_USER=
  POSTGRES_PASSWORD=
  SECRET_KEY_DJANGO=
  CORS_ALLOWED_HOSTS=example.com,localhost, 127.0.0.1,localhost, [::1], 0.0.0.0
  ALLOWED_HOSTS=127.0.0.1,localhost, [::1], 0.0.0.0
  STORAGE_PATH=media
  DJANGO_SUPERUSER_USERNAME=
  DJANGO_SUPERUSER_PASSWORD=
  DJANGO_SUPERUSER_EMAIL=dev@example.com
```

+ Устанавливаем зависимости

```pip install -r requirements.txt```

+ Проводим миграции 

перейти в директорию

```cd cloudhaven```

+ запустить скрипт create_superuser.py, он подтянет данные из .env

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

+ запустить скрипт get_token.py, он получит токен и запишет в .env

в браузере открыть

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin


в новом окне терминала перейти в директорию

cloudhaven/frontend

+ запустить 

```npm run dev```

в браузере открыть

http://localhost:5173/

