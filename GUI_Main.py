import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt

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
        self.label_main_headline = None

        self.button_main_ctrl_exit = None

        self.button_main_nav_home = None
        self.button_main_nav_study = None


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

        self.label_main_headline = QLabel("GRBAS_Mate ((ɡʁæps mæɪtʰ))", self)
        self.label_main_headline.setGeometry(0, 0, 300, 40)
        self.label_main_headline.setStyleSheet("background-color: rgba(50, 50, 50, 180); color: white; padding-left: 10px;")
        self.label_main_headline.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_main_headline.setMouseTracking(True)
        self.label_main_headline.installEventFilter(self)


        # self.label_main_title = QLabel(GTM.label_main_title(), self)
        # self.label_main_title.setAlignment(Qt.AlignCenter)

        # Main GUI controls (4 buttons) --------------------------------------------------------------------------------
        self.button_main_ctrl_exit = QPushButton(self)
        self.button_main_ctrl_exit.setGeometry(1200, 10, 30, 30)
        self.button_main_ctrl_exit.setStyleSheet(GSS.button_main_ctrl_exit())
        self.button_main_ctrl_exit.setText('Exit')
        self.button_main_ctrl_exit.clicked.connect(self.close)

        # faq
        # minimieren
        # user guide



        # Main Navigation Bar (5 Buttons) ------------------------------------------------------------------------------
        self.button_main_nav_home = QPushButton(self)
        self.button_main_nav_home.setGeometry(2, 120, 90, 90)
        self.button_main_nav_home.setStyleSheet(GSS.buttons_main_nav())
        self.button_main_nav_home.setIcon(QIcon("./src/gui/ico/button_main_nav_home.png"))
        self.button_main_nav_home.setIconSize(self.button_main_nav_home.size())
        """
        self.button_main_nav_home.released.connect(
            lambda: self.button_main_nav_home.setIcon(QIcon("./src/gui/ico/button_main_nav_home.png"))
            if self.button_main_nav_home.underMouse()
            else self.button_main_nav_home.setIcon(QIcon("./src/gui/ico/button_main_nav_study.png")))
        self.button_main_nav_home.pressed.connect(
           self.button_main_nav_home.setIcon(QIcon("./src/gui/ico/button_main_nav_home.png")))"""
        # self.button_main_nav_home.setText("Home")

        self.button_main_nav_study = QPushButton(self)
        self.button_main_nav_study.setGeometry(2, 230, 90, 90)
        self.button_main_nav_study.setStyleSheet(GSS.buttons_main_nav())
        self.button_main_nav_study.setIcon(QIcon("./src/gui/ico/button_main_nav_study.png"))
        self.button_main_nav_study.setIconSize(self.button_main_nav_study.size())
        # self.button_main_nav_home.setText("Home")

    def eventFilter(self, obj, event):
        if obj == self.label_main_background:
            if event.type() == event.MouseButtonPress and event.button() == Qt.LeftButton:
                self.gui_pos = event.globalPos() - self.frameGeometry().topLeft()
                return True
            elif event.type() == event.MouseMove and self.gui_pos:
                self.move(event.globalPos() - self.gui_pos)
                return True
            elif event.type() == event.MouseButtonRelease:
                self.gui_pos = None
                return True
        return super().eventFilter(obj, event)




app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
