import datetime
import os
from application.packages.error_manager import ErrorManager

LOG_FILE = "logs.txt"
LOG_FORMAT = "[ {} ] : {}\n"


class Logger:
    def __init__(self, log_message):
        self.log_entry = LOG_FORMAT.format(datetime.datetime.now(), log_message)
        self.log_file_exists = os.path.exists(LOG_FILE)

        try:
            if self.log_file_exists:
                self.append_log()
            else:
                self.create_log()
        except Exception as error:
            ErrorManager(format(str(error)), "LM001")

    def append_log(self):
        try:
            with open(LOG_FILE, "a") as log_file:
                log_file.write(self.log_entry)
        except Exception as error:
            ErrorManager(format(str(error)), "LM002")

    def create_log(self):
        try:
            with open(LOG_FILE, "w") as log_file:
                log_file.write(self.log_entry)
        except Exception as error:
            ErrorManager(format(str(error)), "LM003")
