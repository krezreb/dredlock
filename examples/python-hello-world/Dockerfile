FROM python:2.7

RUN mkdir -p /usr/app/
WORKDIR /usr/app

COPY lib/requirements.txt /usr/app/

RUN pip install -r requirements.txt

COPY examples/python-hello-world/* /usr/app/
COPY lib/* /usr/app/lib/


CMD python hello-world.py 