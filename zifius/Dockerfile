FROM ubuntu

RUN apt-get update
RUN apt-get install -y php5

ADD ./info.php /www/info.php
# RUN pip install -r /www/requirements.txt

# ADD ./app.py /www/app.py

EXPOSE 8000

WORKDIR /www

CMD php -S 0.0.0.0:8000
