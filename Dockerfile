FROM python:alpine

COPY . /opt/flask/

ENV FLASK_APP=/opt/flask/app.py

WORKDIR /opt/flask

RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0
