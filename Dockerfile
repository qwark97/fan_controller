# WILL WORK ONLY AT RPI

FROM python:3-buster
WORKDIR /app
EXPOSE 50000
ENTRYPOINT ["python", "./main.py"]
COPY rpi_packages /rpi_packages
RUN \
    dpkg -i /rpi_packages/device-tree-compiler.deb && \
    dpkg -i /rpi_packages/raspberrypi-bootloader.deb && \
    dpkg -i /rpi_packages/libraspberrypi0.deb && \
    dpkg -i /rpi_packages/libraspberrypi-bin.deb && \
    pip install --no-cache-dir Flask==1.1.2 RPi.GPIO==0.7.0
COPY main.py .