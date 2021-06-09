"""Module to start Flask-server and initiate JsonParser-object
and declare functions that responds to server calls"""
from flask import Flask, request, jsonify
from src.json_parser import JsonParser


signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """Returns signal title"""
    data = request.get_json()
    signal_title = json_parser.get_signal_title(data['signal'])
    return jsonify(signal_title)
