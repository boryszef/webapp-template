# webapp-template

Template af complete stack for a web application backend, containing:
- Django app running on uWSGI
- nginx server hosting static files and routing traffic to the app
- Postgresql database
- Celery worker
- RabbitMQ broker for the communication between the app and the worker
- Grafana with Loki for log aggregation and analysis

## Running the whole stack

Use the `.env.template` to prepare the `.env` file with your credentials.
Then simply start using docker-compose:
```
docker-compose up -d
```
It will start the following services:
| URL                            | Service                |
|--------------------------------|------------------------|
| http://127.0.0.1/schema/ui/    | Swagger API            |
| http://127.0.0.1/schema/redoc/ | API documentation      |
| http://127.0.0.1:3000/         | Grafana                |
| http://127.0.0.1:8080/         | RabbitMQ               |

## Development mode

To develop the app, first prepare the virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements/development.txt
```

then go to `./app/src` and run the local server:
```

./manage.py migrate
./manage.py runserver
```

## Running tests

Initialize the virtual environment and launch pytest:
```
source venv/bin/activate
cd ./app/src
pytest
```