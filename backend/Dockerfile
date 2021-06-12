FROM python:3.8.10

WORKDIR /

COPY requiraments.txt requiraments.txt

COPY flask_app/sslkey.pem app/sslkey.pem

RUN python -m venv venv

RUN . venv/bin/activate

RUN pip install -r requiraments.txt

ENV FLASK_APP=wsgi.py

COPY . .

EXPOSE 5000 

CMD [ "flask", "run"]