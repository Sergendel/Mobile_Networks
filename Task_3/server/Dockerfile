FROM python:3.6

RUN mkdir -p /usr/src/app/
RUN pip install requests
WORKDIR /usr/src/app/

COPY . /usr/src/app/
EXPOSE 80

CMD ["python","server.py" ]


