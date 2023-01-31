FROM python:3.10

WORKDIR /flask
COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt


CMD ["gunicorn", "app:create_app()"]
