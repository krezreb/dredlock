FROM python:2.7

RUN mkdir -p /usr/app/
WORKDIR /usr/app

COPY examples/python-hello-world/* /usr/app/
COPY lib/* /usr/app/lib/

RUN pip install -r requirements.txt

CMD python hello-world.py 