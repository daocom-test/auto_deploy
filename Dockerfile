FROM python:2.7

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["python", "/app/app.py"]

