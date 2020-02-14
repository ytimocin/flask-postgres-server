# https://opensource.com/article/19/11/python-web-api-flask

1. pip install flask-restful
2. pip freeze > requirements.txt
3. python main.py

# Adding gunicorn and nginx
# https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a

1. asdas

# sqlAlchemy

1. pip install flask_sqlalchemy

# app/__init__.py

1. export FLASK_APP=app
2. export FLASK_ENV=development
3. flask run

# will add gunicorn later

# https://stackoverflow.com/questions/55839111/installing-psycopg2-fails-on-macos-with-unclear-error-message

# flask-alembic

1. flask db init => creates the migrations folder
2. flask db revision -m "create account table" => creates a new version
3. flask db upgrade => runs the migrations

# https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

# docker-compose
1. docker-compose up --build --remove-orphans