FROM python:2.7

RUN mkdir -p /usr/app/
WORKDIR /usr/app


RUN pip install "redis>=3.0.0,<3.1.0"
RUN pip install dredlock redis-py-cluster

COPY *py /usr/app/

CMD python -u mutex.py