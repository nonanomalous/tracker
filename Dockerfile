# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update
RUN apk upgrade
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev git nano
RUN apk add --no-cache libpq

#git clone the repo
RUN git clone https://github.com/nonanomalous/tracker.git tracker

# ensure www-data user exists
RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

#pip
RUN cd tracker
WORKDIR /app/tracker
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


#cleanup leftovers and install nginx
RUN apk del .build-deps
RUN apk add nginx
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
COPY start-server.sh /app/tracker

# copy project
#COPY . /app/tracker/

#Start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/app/tracker/start-server.sh"]
