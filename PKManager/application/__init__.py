import sys
import json
from application.packages.logger import Logger
from application.packages.error_manager import ErrorManager

JSON_FILE_PATH = "data/configurations.json"
VALID_COMMANDS = []


def load_json(file_path):
    """Loads the contents of a JSON file."""
    try:
        with open(file_path, "r") as config_file:
            content = json.load(config_file)
        return content
    except FileNotFoundError as error:
        ErrorManager(str(error), "CA001")
        sys.exit(5)
    except json.JSONDecodeError as error:
        ErrorManager(str(error), "CA002")
        sys.exit(5)


class CommandHandler:
    def __init__(self, command, valid_commands):
        Logger(f"Command entered: {command}")

        if command in valid_commands:
            self.handle_command(command)
        else:
            print("Invalid command. Type 'help' for available commands.")

    def handle_command(self, command):
        """Manages the execution of orders."""
        return 0


class ConsoleApplication:
    def __init__(self):
        self.application_config = load_json(JSON_FILE_PATH)
        self.is_running = True

        self.print_application_info()
        self.handle_user_input()

    def print_application_info(self):
        """Displays the application information."""
        print("{} - {}\n".format(
            self.application_config['application']['product-name'],
            self.application_config['application']['version'])
        )
        print("Welcome to PKManager, here you can securely store your passwords directly on your PC.\n"
              'For more information, enter the command: "help".\n')

    def handle_user_input(self):
        """Manages user input in loop."""
        while self.is_running:
            user_input = input("> ")
            CommandHandler(user_input, VALID_COMMANDS)