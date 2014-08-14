FROM ubuntu

RUN apt-get update
RUN apt-get install -y python-dev python-distribute python-pip

ADD ./requirements.txt /www/requirements.txt
RUN pip install -r /www/requirements.txt

ADD ./app.py /www/app.py

EXPOSE 5000

CMD python /www/app.py
