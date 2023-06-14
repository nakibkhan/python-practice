FROM python:3.10
# Or any preferred Python version.
RUN apt-get update &&  \
    apt-get install -y build-essential wget vim g++  && \
#    apt-get install -y python-pip python-dev && \
#    apt-get install -y libblas-dev libatlas-dev libatlas-base-dev liblapack-dev && \
#    apt-get install -y gfortran libpq-dev libjpeg-dev  && \
    apt-get update && \
    apt-get install -y libopencv-dev --fix-missing

ADD main.py .
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]