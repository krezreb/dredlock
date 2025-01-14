FROM python:3

RUN mkdir -p /usr/app/
WORKDIR /usr/app

COPY dredlock/*py /usr/app/
RUN pip install redis

COPY examples/python-hello-world/*py /usr/app/


CMD ["python",  "hello-world.py"] 