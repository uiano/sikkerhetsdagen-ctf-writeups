FROM php:8.1.12RC1-apache-buster
COPY www/ /var/www/html/
RUN chown -R www-data:www-data /var/www

RUN find /var/www/html -type d -exec chmod 755 -R {} \;
RUN find /var/www/html -type f -exec chmod 644 {} \;
EXPOSE 80
