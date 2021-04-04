FROM python:3-slim
WORKDIR /usr/src/app
EXPOSE 50000
CMD ["python", "./main.py"]
RUN pip install --no-cache-dir Flask==1.1.2 RPi.GPIO==0.7.0
COPY main.py .