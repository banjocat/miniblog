FROM django:onbuild

# This should be started with a volume pointing to the local database file
# docker run -d -P -v /home/name/miniblog/db/:/var/src/app/db
# This will bind the container to the local database
# This allows easier migrations... containers should be immutable

env DJANGO_DOCKER 1

# Need to set it!
ARG KEY

env DJANGO_SECRET_KEY SECRET_KEY

