FROM php:8.1.12RC1-apache-buster
COPY www/ /var/www/html/

COPY certs/ /etc/ssl/certs/
COPY conf/ /etc/apache2/sites-enabled/

RUN chown -R www-data:www-data /var/www
RUN a2enmod ssl
RUN find /var/www/html -type d -exec chmod 755 -R {} \;
RUN find /var/www/html -type f -exec chmod 644 {} \;
EXPOSE 443
