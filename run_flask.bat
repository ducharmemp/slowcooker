set FLASK_APP=source.app.py
set FLASK_ENV=development
python -c "from source.models import init_database; init_database()"
flask run
