''' 
Main function of the VNA Reader Software
'''

import sys
from PyQt5.QtWidgets import QApplication
from .local_classes.definition_class_my_vna_reader_main_gui import (
        vnaReaderMainGUI)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Creates an instance of the vnaReaderMainGui class
    # defined in definition_class_my_vna_reader_main_gui
    # It opens the main GUI of the program
    w = vnaReaderMainGUI()
    w.show()
    sys.exit(app.exec_())
