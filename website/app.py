from flask import Flask, jsonify

__all__ = ["create_app"]


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route("/<name>")
    def index(name):
        #return "hello world"
        data = {
        "message": "Hello, world!",
        "status": "success",
        "name": name
        }
        return jsonify(data)

    return app
