FROM postgres:alpine

RUN mkdir /var/log/export
RUN chown postgres:postgres /var/log/export
COPY ./postgresql.conf /usr/local/share/postgresql/postgresql.conf.sample