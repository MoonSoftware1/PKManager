import datetime
from application.packages.error_manager.manager import error_code_list

ERROR_FORMAT = "[{}] : ERROR {} - {}"


class CustomError(Exception):
    """Custom exception class for handling errors."""

    def __init__(self, error_message, error_code):
        super().__init__(error_message)
        self.error_code = error_code
        self.key_code = self._find_error_key()

    def _find_error_key(self):
        """Find the corresponding error key for the given error code."""
        for error_dict in error_code_list:
            key_code = error_dict.get(str(self.error_code))
            if key_code is not None:
                return key_code
        return None


class ErrorManager:
    def __init__(self, error_message, error_code):
        self.error = CustomError(error_message, error_code)
        self.error_output()

    def error_output(self):
        """Print the formatted error message to the console."""
        formatted_error = ERROR_FORMAT.format(self.get_current_timestamp(), self.error.error_code, str(self.error))
        print(formatted_error)

    @staticmethod
    def get_current_timestamp():
        """Returns the current timestamp in a formatted string."""
        return datetime.datetime.now()
