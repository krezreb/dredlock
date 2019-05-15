FROM python:2.7

RUN mkdir -p /usr/app/
WORKDIR /usr/app

RUN pip install hungry_hungry_hippos

COPY examples/python-hello-world/* /usr/app/

CMD python hello-world.py 