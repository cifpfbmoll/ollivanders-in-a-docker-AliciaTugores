FROM python:3.8-slim-buster

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1 

WORKDIR /Ollivanders_api_rest

COPY . /Ollivanders_api_rest

COPY requeriments.txt .

RUN python -m pip install -r requeriments.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", ".api.py"]