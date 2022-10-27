FROM php:8.1.12RC1-apache-buster
COPY www/ /var/www/html/
COPY flag.txt /var/www/flag.txt
COPY random.txt /var/www/random.txt 

COPY conf/ /etc/apache2/sites-enabled/

RUN chown www-data:www-data /var/www/random.txt 
RUN chown www-data:www-data /var/www/flag.txt 

RUN find /var/www/html -type d -exec chmod 755 -R {} \;
RUN find /var/www/html -type f -exec chmod 644 {} \;
EXPOSE 80
