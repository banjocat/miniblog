FROM django:python2

# This should be started with a volume pointing to the local database file
# docker run -d -P -v /home/name/miniblog/db/:/var/src/app/db
# This will bind the container to the local database
# This allows easier migrations... containers should be immutable


RUN mkdir -p /opt/blog
COPY blog/. /opt/app/.
WORKDIR /opt/app

CMD ./manage.py runserver 0.0.0.0:8000

