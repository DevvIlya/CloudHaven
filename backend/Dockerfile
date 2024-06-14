
FROM python:3.10.12


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /code


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


EXPOSE 8000

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

CMD ["sh", "-c", "/wait-for-it.sh db:5432 -- \
    python backend/myproject/manage.py makemigrations && \
    python backend/myproject/manage.py migrate --noinput && \
    python backend/myproject/manage.py createsuperuser --noinput && \
    python backend/myproject/manage.py runserver 0.0.0.0:8000"]