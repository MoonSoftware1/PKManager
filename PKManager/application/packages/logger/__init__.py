import os
import datetime
from application.packages.error_manager import ErrorManager

LOG_FILE = "logs.txt"
LOG_FORMAT = "[{}] : {}\n"


class Logger:
    def __init__(self, log_message):
        self.log_entry = LOG_FORMAT.format(self.get_current_timestamp(), log_message)
        self.log_file_exists = os.path.exists(LOG_FILE)

        try:
            if self.log_file_exists:
                self.append_log()
            else:
                self.create_log()
        except Exception as error:
            ErrorManager(str(error), "LM001")

    @staticmethod
    def get_current_timestamp():
        """Returns the current timestamp in a formatted string."""
        return datetime.datetime.now()

    def append_log(self):
        """Appends the log entry to an existing log file."""
        try:
            with open(LOG_FILE, "a") as log_file:
                log_file.write(self.log_entry)
        except Exception as error:
            ErrorManager(str(error), "LM002")

    def create_log(self):
        """Creates a new log file and writes the log entry."""
        try:
            with open(LOG_FILE, "w") as log_file:
                log_file.write(self.log_entry)
        except Exception as error:
            ErrorManager(str(error), "LM003")
