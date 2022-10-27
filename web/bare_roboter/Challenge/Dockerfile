FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./src/. /var/www/.
RUN pip install Flask

# https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-20-04
