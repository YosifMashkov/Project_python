FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r /Requirements/requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "main.py"]
