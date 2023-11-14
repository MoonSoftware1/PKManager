import sys
import json
from application.packages.logger import Logger
from application.packages.error_manager import ErrorManager

JSON_FILE_PATH = "data/configurations.json"
VALID_COMMANDS = []


def load_json(file_path):
    try:
        with open(file_path, "r") as config_file:
            content = json.load(config_file)

        return content
    except FileNotFoundError as error:
        ErrorManager(format(str(error)), "CA001")
        sys.exit(5)
    except json.JSONDecodeError as error:
        ErrorManager(format(str(error)), "CA002")
        sys.exit(5)


class CommandHandler:
    def __init__(self, command, valid_command):
        Logger(f"Command enter : {command}")

        if command in valid_command:
            print("Hello World")


class ConsoleApplication:
    def __init__(self):
        self.application_config = load_json(JSON_FILE_PATH)
        self.is_running = True

        self.print_application_info()
        self.handle_user_input()

    def print_application_info(self):
        print("{} - {}\n".format(
            self.application_config['application']['product-name'],
            self.application_config['application']['version'])
        )
        print("Welcome to PKManager, here you can securely store your passwords directly on your PC.\n"
              'For more information, enter the command: "help".\n')

    def handle_user_input(self):
        while self.is_running:
            user_input = input("> ")
            CommandHandler(user_input, VALID_COMMANDS)
