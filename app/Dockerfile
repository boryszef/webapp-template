FROM python:3.12-alpine
RUN apk add build-base linux-headers
RUN apk cache clean
RUN mkdir /app
RUN adduser -D uwsgi
RUN python -m venv /app/venv

COPY src /app/
COPY requirements/production.txt /app/requirements.txt
COPY api.sh /app/
RUN chmod 755 /app/api.sh
RUN mkdir /static
RUN mkdir /applogs

RUN chown -R uwsgi /app /static /applogs
USER uwsgi
ENV PATH="/app/venv/bin:$PATH"
RUN pip install -r /app/requirements.txt
ENTRYPOINT [ "/app/api.sh" ]