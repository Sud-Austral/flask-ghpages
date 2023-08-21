from flask import Flask, jsonify

__all__ = ["create_app"]


def create_app():
    app = Flask.Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route("/")
    def index():
        #return "hello world"
        data = {
        "message": "Hello, world!",
        "status": "success"
        }
        return jsonify(data)

    return app
