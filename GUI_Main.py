import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer

# icons for buttons: https://icons8.de/icons/set/free-icons--style-glyph-neue

import GUI_Style_Sheets as GSS
import GUI_Text_Manager as GTM
import GUI_Sound_Manager as GSM


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.gui_pos = None

        self.label_main_background = None
        self.label_main_headline_background = None
        self.label_main_headline = None
        self.label_main_nav_bar_background = None

        self.button_main_ctrl_exit = None

        self.button_main_nav_home = None
        self.button_main_nav_description = None
        self.button_main_nav_study = None
        self.button_main_nav_training = None
        self.button_main_nav_settings = None

    def init_ui(self):

        # Window properties --------------------------------------------------------------------------------------------
        # self.setWindowTitle(GTM.window_title())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(1280, 720)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setFixedSize(self.width(), self.height())

        # Labels for Background colours, headlines etc. ----------------------------------------------------------------
        self.label_main_background = QLabel(self)
        self.label_main_background.setGeometry(0, 0, 1280, 720)
        self.label_main_background.setStyleSheet(GSS.label_main_background())

        self.label_main_headline_background = QLabel(GTM.label_main_headline_background(), self)
        self.label_main_headline_background.setGeometry(0, 0, 1280, 100)
        self.label_main_headline_background.setStyleSheet(GSS.label_main_headline_background())
        self.label_main_headline_background.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        # self.label_main_headline.setMouseTracking(True)
        # self.label_main_headline.installEventFilter(self)

        self.label_main_nav_bar_background = QLabel(self)
        self.label_main_nav_bar_background.setGeometry(0, 100, 100, 620)
        self.label_main_nav_bar_background.setStyleSheet(GSS.label_main_nav_bar_background())

        # Main GUI controls (4 buttons) --------------------------------------------------------------------------------
        self.button_main_ctrl_exit = QPushButton(self)
        self.button_main_ctrl_exit.setGeometry(1200, 35, 30, 30)
        self.button_main_ctrl_exit.setStyleSheet(GSS.button_main_ctrl_exit())
        self.button_main_ctrl_exit.setText('Exit')
        self.button_main_ctrl_exit.clicked.connect(self.close)

        # faq
        # minimieren
        # user guide

        # Main Navigation Bar (5 Buttons) ------------------------------------------------------------------------------
        # [Home, Description, Study, Training, Settings]
        self.button_main_nav_home = QPushButton(self)
        self.button_main_nav_home.setGeometry(5, 110, 90, 90)
        self.button_main_nav_home.clicked.connect(lambda: QTimer.singleShot(50, self.menu_home))

        self.button_main_nav_description = QPushButton(self)
        self.button_main_nav_description.setGeometry(5, 210, 90, 90)
        self.button_main_nav_description.clicked.connect(lambda: QTimer.singleShot(50, self.menu_description()))

        self.button_main_nav_study = QPushButton(self)
        self.button_main_nav_study.setGeometry(5, 310, 90, 90)
        self.button_main_nav_study.clicked.connect(self.menu_study)

        self.button_main_nav_training = QPushButton(self)
        self.button_main_nav_training.setGeometry(5, 410, 90, 90)
        self.button_main_nav_training.clicked.connect(self.menu_training)

        self.button_main_nav_settings = QPushButton(self)
        self.button_main_nav_settings.setGeometry(5, 620, 90, 90)
        self.button_main_nav_settings.clicked.connect(self.menu_settings)

        self.menu_settings()

    def menu_home(self):
        print("Home")
        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=True))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

    def menu_description(self):
        print("Description")
        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=True))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

    def menu_study(self):
        print("Study")
        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=True))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

    def menu_training(self):
        print("Training")
        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=True))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

    def menu_settings(self):
        print("Settings")
        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=True))


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
