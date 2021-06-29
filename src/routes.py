"""Module to start Flask-server and initiate JsonParser-object
and declare functions that responds to server calls"""
from flask import Flask, request, jsonify, abort
from src.json_parser import JsonParser, NotInDatabase
import logging


signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()
logger = logging.getLogger(__name__)

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """Returns signal title"""
    data = request.get_json()
    try:
        signal_id = data['signal']
    except KeyError as err:
        logger.warning("Badly formatted signal id request from client: %s", data)
        return "send your request as a json object with key=signal and value='id' where id is an integer", 404

    try:
        signal_title = json_parser.get_signal_title(signal_id)
        return jsonify(signal_title)
    except NotInDatabase as err:
        abort(400, description=err.message)


