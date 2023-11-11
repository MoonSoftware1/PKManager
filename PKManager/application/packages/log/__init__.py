import os
from datetime import datetime


def logs(text):
    file = "logs.txt"
    currentTime = datetime.now()

    if not os.path.exists(file):
        with open(file, "w"):
            pass

    with open(file, "a") as logFile:
        logFile.write("[ {} ] : {}\n".format(currentTime, text))

    return 0
