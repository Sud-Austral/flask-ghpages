from flask import Flask, jsonify
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import numpy
import tflearn
import tensorflow
import json
import random
import pickle
nltk.download('punkt')

__all__ = ["create_app"]


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route("/")
    def index():
        #return "hello world"
        data = {
        "message": "Hello, world!",
        "status": "success",
        }
        return jsonify(data)
    
    @app.route("/greed/")
    @app.route("/greed/<name>")
    def greed(name="stranger"):
        #return "hello world"
        data = {
        "message": "Hello, world!",
        "status": "success",
        "name": name
        }
        return jsonify(data)

    return app
