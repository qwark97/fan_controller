FROM python:3-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 50000

CMD ["python", "./main.py"]