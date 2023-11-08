import sys
from PyQt5.QtWidgets import QApplication
from application.templates.home import HOMETemplate

if __name__ == '__main__':
    application = QApplication(sys.argv)
    root = HOMETemplate()
    root.show()
    sys.exit(application.exec_())
