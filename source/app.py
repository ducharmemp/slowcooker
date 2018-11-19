from flask import Flask

from source.routes.v1 import v1_api
from source.models import connection

app = Flask(__name__)
app.register_blueprint(v1_api)

@app.route('/')
def index():
    with connection() as conn:
        return str(conn.execute('SELECT 1').fetchone()[0])

