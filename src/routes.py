"""Module to start Flask-server and initiate JsonParser-object
and declare functions that responds to server calls"""
import logging
from flask import Flask, request, jsonify
from src.json_parser import JsonParser
from src.xml_parser import XmlParser, NotInDatabaseError
from src.parser_factory import ParserFactory


parser_factory = ParserFactory()
parser_factory.register_format("json", JsonParser)
parser_factory.register_format("xml", XmlParser)
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
        parser = parser_factory.get_parser()
        signal_title = parser.get_signal_title(signal_id)
        return jsonify(signal_title)
    except NotInDatabaseError as err:
        return err.message, 400
