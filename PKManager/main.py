import sys
from PyQt5.QtWidgets import QApplication
from application.templates.home import HOMETemplate
from application.packages.log import logs

if __name__ == '__main__':
    logs("Launch the application.")
    application = QApplication(sys.argv)
    root = HOMETemplate()
    root.show()
    sys.exit(application.exec_())
