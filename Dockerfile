FROM python:3.9.7

WORKDIR /crud-python

ADD . /crud-python

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]