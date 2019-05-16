FROM python:2.7

RUN mkdir -p /usr/app/
WORKDIR /usr/app

RUN pip install hungry-hungry-hippos

COPY *py /usr/app/

CMD python -u mutex.py