FROM python:2.7

RUN mkdir -p /usr/app/
WORKDIR /usr/app

RUN pip install redis==2.10.6
RUN pip install hungry-hungry-hippos redis-py-cluster

COPY *py /usr/app/

CMD python -u mutex.py