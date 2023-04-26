FROM python:3.7-slim
RUN mkdir /app
ADD . /app
WORKDIR /app
COPY ./requirements.txt requirements.txt
COPY ./harcascade-face.xml harcascade-face.xml
RUN pip install -r requirements.txt
RUN apt update && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 

CMD ["python", "face-recognition.py"]