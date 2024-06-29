FROM python:3.10.12


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install -y \
    postgresql-server-dev-all \
    gcc \
    python3-dev \
    musl-dev \
    && apt clean

RUN pip install --upgrade pip

WORKDIR /code


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


EXPOSE 8000

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

CMD sh -c '/wait-for-it.sh db:5432 -- \
    && python cloudhaven/manage.py makemigrations \
    && python cloudhaven/manage.py migrate --noinput \
    && python cloudhaven/create_superuser.py \
    && python cloudhaven/manage.py collectstatic --noinput \
    && python cloudhaven/manage.py runserver 0.0.0.0:8000'