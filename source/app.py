from flask import Flask, url_for, jsonify

from source.routes.v1 import v1_api
from source.models import connection, init_database

app = Flask(__name__)
app.register_blueprint(v1_api, url_prefix="/api/v1")

# app.before_first_request(init_database)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site-map")
def site_map():
    links = []

    print(app.url_map)
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return jsonify(links)
