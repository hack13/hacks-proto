FROM python:3
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python my-discord.py
LABEL org.opencontainers.image.source=https://github.com/hack13/hacks-proto