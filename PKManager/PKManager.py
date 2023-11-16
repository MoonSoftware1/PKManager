import sys
from application.packages.logger import Logger
from application import ConsoleApplication

if __name__ == '__main__':
    Logger("Open the application")
    try:
        ConsoleApplication()
    except KeyboardInterrupt:
        Logger("Closing the application")
        sys.exit(0)
