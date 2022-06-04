FROM python:3.8

WORKDIR /usr/src/app

# intall java
# RUN apt-get -y update && apt-get -y install openjdk-8-jdk
#install espeak
RUN  apt-get -y update  && apt-get install -y libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev
RUN RUN apt-get install -qqy x11-apps
ENV DISPLAY :0

RUN  apt-get -y update  && apt-get install -y espeak
RUN python -m pip install --upgrade pip
COPY requirements.txt ./

RUN apt-get -y update && apt-get -y install build-essential \
    gcc \
    libpulse-dev \
    swig
    
RUN pip install --no-cache-dir -r requirements.txt
#install pyaudio
RUN pip install pyaudio
COPY . .

# CMD ["python3", "./main.py"]