export SECRET_KEY=phoenix01
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://april:2222@localhost/blog'
# python3 manage.py db init
# python3 manage.py db migrate -m "Deployment Migration"
# python3 manage.py db upgrade
python3.9 manage.py server