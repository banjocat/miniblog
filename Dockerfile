FROM django:onbuild

env DJANGO_DOCKER 1
env DJANGO_SECRETE_KEY (INSERT KEY)

RUN mkdir /db
VOLUME /db
