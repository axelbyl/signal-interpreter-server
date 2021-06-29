"""
Initiates a flask-server and reads the json-file given as --file-path
"""
from argparse import ArgumentParser
from src.routes import signal_interpreter_app, json_parser
import logging

logger = logging.getLogger(__name__)


def parse_arguments():
    """Return path specified to --file-path"""
    parser = ArgumentParser()
    parser.add_argument("--file-path")
    args = parser.parse_args()
    return args


def main():
    """Main script to start server and read data"""
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    logger.info("Datbase parsed from  %s", args.file_path)
    signal_interpreter_app.run()


def init():
    if __name__ == '__main__':
        main()


init()
