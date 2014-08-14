FROM ubuntu

RUN apt-get update
RUN apt-get install -y php5

RUN mkdir -p /public_html

RUN echo "<?php echo 'Hello world!';" > /public_html/index.php

EXPOSE 5000

WORKDIR /public_html

CMD php -S 0.0.0.0:5000
