FROM python:3.10.9-slim

COPY . /docker

RUN cd /docker && pip install -r requirements.txt

ENV ROOT=/docker
WORKDIR ${ROOT}
EXPOSE 7860
CMD python -u main.py
