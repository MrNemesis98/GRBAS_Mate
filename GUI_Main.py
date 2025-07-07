import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer, QPoint

# icons for buttons: https://icons8.de/icons/set/free-icons--style-glyph-neue

import GUI_Style_Sheets as GSS
import GUI_Text_Manager as GTM
import GUI_Sound_Manager as GSM


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window properties --------------------------------------------------------------------------------------------
        # self.setWindowTitle(GTM.window_title())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(1380, 800)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Flag & Startpunkt für Drag-Funktion
        self._drag_active = False
        self._drag_position = QPoint()

        # Labels for Background colours, headlines etc. ----------------------------------------------------------------
        self.label_main_background = QLabel(self)
        self.label_main_background.setGeometry(0, 0, 1380, 800)
        self.label_main_background.setStyleSheet(GSS.label_main_background())

        self.label_main_headline_background = QLabel(GTM.label_main_headline_background(), self)
        self.label_main_headline_background.setGeometry(0, 0, 1380, 80)
        self.label_main_headline_background.setStyleSheet(GSS.label_main_headline_background())
        self.label_main_headline_background.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_main_headline_background.mousePressEvent = self.headline_mouse_press
        self.label_main_headline_background.mouseMoveEvent = self.headline_mouse_move
        self.label_main_headline_background.mouseReleaseEvent = self.headline_mouse_release

        self.label_main_nav_bar_background = QLabel(self)
        self.label_main_nav_bar_background.setGeometry(0, 80, 80, 720)
        self.label_main_nav_bar_background.setStyleSheet(GSS.label_main_nav_bar_background())

        # Main GUI controls (4 buttons) --------------------------------------------------------------------------------
        # [Info, FAQ, Minimize, Exit]
        self.button_main_ctrl_info = QPushButton(self)
        self.button_main_ctrl_info.setGeometry(1180, 20, 40, 40)
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_info.clicked.connect(self.menu_info)

        self.button_main_ctrl_faq = QPushButton(self)
        self.button_main_ctrl_faq.setGeometry(1230, 20, 40, 40)
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
        self.button_main_ctrl_faq.clicked.connect(self.menu_faq)

        self.button_main_ctrl_minimize = QPushButton(self)
        self.button_main_ctrl_minimize.setGeometry(1280, 25, 30, 30)
        self.button_main_ctrl_minimize.setStyleSheet(GSS.button_main_ctrl_minimize())
        self.button_main_ctrl_minimize.clicked.connect(self.showMinimized)

        self.button_main_ctrl_exit = QPushButton(self)
        self.button_main_ctrl_exit.setGeometry(1325, 25, 30, 30)
        self.button_main_ctrl_exit.setStyleSheet(GSS.button_main_ctrl_exit())
        self.button_main_ctrl_exit.clicked.connect(self.close)

        # Main Navigation Bar (5 Buttons) ------------------------------------------------------------------------------
        # [Home, Description, Study, Training, Settings]
        self.button_main_nav_home = QPushButton(self)
        self.button_main_nav_home.setGeometry(10, 110, 60, 60)
        self.button_main_nav_home.clicked.connect(self.menu_home)

        self.button_main_nav_description = QPushButton(self)
        self.button_main_nav_description.setGeometry(10, 210, 60, 60)
        self.button_main_nav_description.clicked.connect(self.menu_description)

        self.button_main_nav_study = QPushButton(self)
        self.button_main_nav_study.setGeometry(10, 310, 60, 60)
        self.button_main_nav_study.clicked.connect(self.menu_study)

        self.button_main_nav_training = QPushButton(self)
        self.button_main_nav_training.setGeometry(10, 410, 60, 60)
        self.button_main_nav_training.clicked.connect(self.menu_training)

        self.button_main_nav_settings = QPushButton(self)
        self.button_main_nav_settings.setGeometry(10, 720, 60, 60)
        self.button_main_nav_settings.clicked.connect(self.menu_settings)

        # Text Labels --------------------------------------------------------------------------------------------------
        self.label_menu_title = QLabel(self)
        self.label_menu_title.setGeometry(130, 100, 430, 80)
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.label_text_1 = QLabel(self)
        self.label_text_1.setStyleSheet(GSS.label_text_1())
        self.label_text_1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_1.setWordWrap(True)
        self.label_text_1.setTextFormat(Qt.RichText)

        self.menu_home()

    def headline_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_active = True
            self._drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def headline_mouse_move(self, event):
        if self._drag_active and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_position)

    def headline_mouse_release(self, event):
        self._drag_active = False

    def menu_info(self):
        print("Info")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=True))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="info"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=True))

    def menu_faq(self):
        print("FAQ")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=True))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="faq"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=True))

    def menu_home(self):
        print("Home")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=True))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="home"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))

        self.label_text_1.setGeometry(130, 220, 1000, 300)
        self.label_text_1.setText(GTM.label_text_1(menu="home"))



    def menu_description(self):
        print("Description")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=True))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="description"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))

    def menu_study(self):
        print("Study")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=True))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="study"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))

    def menu_training(self):
        print("Training")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=True))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="training"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))

    def menu_settings(self):
        print("Settings")
        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=True))

        self.label_menu_title.setText(GTM.label_menu_title(menu="settings"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
