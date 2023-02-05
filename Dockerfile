FROM python:3.9-bullseye

COPY ./src/discord-songwhip /discord-songwhip
COPY ./requirements/discord-songwhip.txt /discord-songwhip
COPY Secrets.py /discord-songwhip

WORKDIR /discord-songwhip/

ENV PYTHONPATH=/discord-songwhip/

RUN pip install --no-cache-dir -r discord-songwhip.txt

CMD [ "python", "main.py"]