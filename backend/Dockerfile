FROM python:3.11

WORKDIR /backend

RUN apt update 

COPY . . 

RUN pip install -e ".[dev]"

ENTRYPOINT ["night"]