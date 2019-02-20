FROM python:3.7-alpine

ADD . /code

WORKDIR /code

RUN pip install flask-cors --upgrade
RUN pip install -r requirements.txt

CMD ["python", "api.py"]