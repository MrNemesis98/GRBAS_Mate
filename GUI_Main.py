import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

# icons for buttons: https://icons8.de/icons/set/free-icons--style-glyph-neue

import GUI_Style_Sheets as GSS
import GUI_Text_Manager as GTM
import GUI_Sound_Manager as GSM


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label_main_title = None
        self.init_ui()

    def init_ui(self):

        # Labels
        self.label_main_title = QLabel(GTM.label_main_title(), self)
        self.label_main_title.setAlignment(Qt.AlignCenter)

        # Window properties
        self.setWindowTitle("GRBAS Mate v1.0")
        self.resize(1280, 720)
        self.setFixedSize(self.width(), self.height())


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
