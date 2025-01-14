FROM python:3

RUN mkdir -p /usr/app/
WORKDIR /usr/app

COPY examples/python-mutex/*py /usr/app/

COPY dredlock/*py /usr/app/

RUN pip install redis

CMD ["python", "-u",  "mutex.py"]