from flask import Flask

from source.routes.v1 import v1_api

app = Flask(__name__)
app.register_blueprint(v1_api)
