FROM python:3

RUN mkdir -p /usr/app/
WORKDIR /usr/app

COPY examples/python-hello-world-catchsig/*py /usr/app/

COPY hungry_hungry_hippos/*py /usr/app/

RUN pip install redis

CMD ["python3",  "-u",  "hello-world-catchsigterm.py"]