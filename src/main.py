from src.routes import signal_interpreter_app, json_parser
from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file-path")
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    signal_interpreter_app.run()


if __name__ == '__main__':
    main()

