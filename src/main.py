"""
Initiates a flask-server and reads the json-file given as --file-path
"""
from pathlib import Path
from argparse import ArgumentParser
import logging
from src.routes import signal_interpreter_app, parser_factory

logger = logging.getLogger(__name__)


def parse_arguments():
    """Return path specified to --file-path"""
    parser = ArgumentParser()
    parser.add_argument("--file-path")
    args = parser.parse_args()
    return args


def read_database(file_path):
    """Finds appropriate parser based on file extension amd parses the file"""
    file_type = Path(file_path).suffix
    parser_factory.set_signal_database_format(file_type[1:])
    parser = parser_factory.get_parser()
    parser.load_file(file_path)
    logger.info("Database parsed from  %s", file_path)


def main():
    """Main script to start server and read data"""
    args = parse_arguments()
    read_database(args.file_path)
    signal_interpreter_app.run()


def init():
    """Init function"""
    if __name__ == '__main__':
        main()


init()
