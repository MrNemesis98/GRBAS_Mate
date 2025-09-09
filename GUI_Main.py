import sys
import threading

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, QTimer, QAbstractAnimation, QEventLoop
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer, QPoint
import time

# icons for buttons: https://icons8.de/icons/set/free-icons--style-glyph-neue

import GUI_Style_Sheets as GSS
import GUI_Text_Manager as GTM
import GUI_Sound_Manager as GSM


def wait_ms(ms: int):
    loop = QEventLoop()
    QTimer.singleShot(ms, loop.quit)
    loop.exec_()


def disconnect_button(button):
    try:
        button.clicked.disconnect()
    except TypeError:
        pass


class MainWindow(QWidget):

    system_status = None

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

        # MENU EXTERNAL ************************************************************************************************
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

        # MENU INTERNAL ***************************************************************************************+++++++++
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

        self.label_text_2 = QLabel(self)
        self.label_text_2.setStyleSheet(GSS.label_text_1())
        self.label_text_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_2.setWordWrap(True)
        self.label_text_2.setTextFormat(Qt.RichText)

        self.label_text_3 = QLabel(self)
        self.label_text_3.setStyleSheet(GSS.label_text_1())
        self.label_text_3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_3.setWordWrap(True)
        self.label_text_3.setTextFormat(Qt.RichText)

        self.label_text_4 = QLabel(self)
        self.label_text_4.setStyleSheet(GSS.label_text_1())
        self.label_text_4.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_4.setWordWrap(True)
        self.label_text_4.setTextFormat(Qt.RichText)

        # Buttons (menu internal)
        self.button_switch_right = QPushButton(self)
        self.button_switch_left = QPushButton(self)

        # Animations ---------------------------------------------------------------------------------------------------
        self._anim_label_fade = None
        self._anim_label_slide = None

        self.menu_home()

    # Window Behaviour *************************************************************************************************
    def headline_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_active = True
            self._drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def headline_mouse_move(self, event):
        if self._drag_active and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_position)

    def headline_mouse_release(self, event):
        self._drag_active = False

    # Menu independent functions ***************************************************************************************
    def hide_all_menu_internal_elements(self):
        self.label_menu_title.hide()
        self.label_text_1.hide()
        self.label_text_2.hide()
        self.label_text_3.hide()
        self.label_text_4.hide()
        self.button_switch_right.hide()
        self.button_switch_left.hide()

    # Menu Layouts *****************************************************************************************************
    def menu_info(self):
        print("Info")
        self.system_status = "menu_info"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=True))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="info"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=True))
        self.label_menu_title.show()

    def menu_faq(self):
        print("FAQ")
        self.system_status = "menu_faq"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=True))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="faq"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=True))
        self.label_menu_title.show()

    def menu_home(self):
        print("Home")
        self.system_status = "menu_home_1"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=True))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="home"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

        self.label_text_1.setGeometry(130, 220, 1000, 320)
        self.label_text_1.setText(GTM.label_text_1(menu="home"))
        self.label_text_1.show()

        self.label_text_2.setGeometry(1350, 220, 1000, 320)
        self.label_text_2.setText(GTM.label_text_2(menu="home"))
        self.label_text_2.show()

        self.label_text_3.setGeometry(1350, 220, 1000, 320)
        self.label_text_3.setText(GTM.label_text_3(menu="home"))
        self.label_text_3.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_3.setOpenExternalLinks(True)
        self.label_text_3.show()

        self.label_text_4.setGeometry(480, 600, 300, 70)
        self.label_text_4.setText(GTM.label_text_4(menu="home", var_1=1))
        self.label_text_4.show()

        self.button_switch_right.setGeometry(805, 600, 70, 70)
        self.button_switch_right.show()

        self.button_switch_left.setGeometry(385, 600, 70, 70)
        self.button_switch_left.show()

        self.menu_home_switch_to_label_1(first_init=True)

    def menu_description(self):
        print("Description")
        self.system_status = "menu_description"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=True))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="description"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

    def menu_study(self):
        print("Study")
        self.system_status = "menu_study"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=True))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="study"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

    def menu_training(self):
        print("Training")
        self.system_status = "menu_training"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=True))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))

        self.label_menu_title.setText(GTM.label_menu_title(menu="training"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

    def menu_settings(self):
        print("Settings")
        self.system_status = "menu_settings"
        self.hide_all_menu_internal_elements()

        self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

        self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
        self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
        self.button_main_nav_study.setStyleSheet(GSS.button_main_nav_study(pressed=False))
        self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
        self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=True))

        self.label_menu_title.setText(GTM.label_menu_title(menu="settings"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

    # Animations *******************************************************************************************************
    def animation_label_fade(self, in_or_out, label_object: QLabel):
        if in_or_out == "in":
            start_value = 0.0
            end_value = 1.0
        else:
            start_value = 1.0
            end_value = 0.0

        effect = label_object.graphicsEffect()
        if not isinstance(effect, QGraphicsOpacityEffect):
            effect = QGraphicsOpacityEffect(label_object)
            label_object.setGraphicsEffect(effect)
            effect.setOpacity(start_value)

        fade = QPropertyAnimation(effect, b"opacity", self)
        fade.setDuration(800)
        fade.setStartValue(effect.opacity())
        fade.setEndValue(end_value)
        fade.setEasingCurve(QEasingCurve.InOutQuad)
        self._anim_label_fade = fade
        fade.start(QAbstractAnimation.DeleteWhenStopped)

    def animation_label_slide(self, in_or_out, label_object: QLabel):
        start_geom = None
        end_geom = None

        if in_or_out == "in":
            start_geom = label_object.geometry()
            end_geom = QRect(130,
                             start_geom.y(),
                             start_geom.width(),
                             start_geom.height())
        else:
            start_geom = label_object.geometry()
            end_geom = QRect(self.width() - 25,
                             start_geom.y(),
                             start_geom.width(),
                             start_geom.height())

        anim = QPropertyAnimation(label_object, b"geometry", self)
        anim.setDuration(800)
        anim.setStartValue(start_geom)
        anim.setEndValue(end_geom)
        anim.setEasingCurve(QEasingCurve.OutQuad)

        self._anim_label_slide = anim  # Referenz halten
        anim.start(QAbstractAnimation.DeleteWhenStopped)

    # Menu Functionality -----------------------------------------------------------------------------------------------

    def menu_home_switch_to_label_1(self, first_init=False):

        if not self.system_status.startswith("menu_home"):
            pass
        else:
            print("entering switch to label 1")

            # Pre-Consequence
            disconnect_button(self.button_switch_right)
            disconnect_button(self.button_switch_left)

            # Animations:
            if not first_init:
                QTimer.singleShot(0, lambda: self.animation_label_slide(
                    in_or_out="out", label_object=self.label_text_2))
                QTimer.singleShot(500, lambda: self.animation_label_fade(
                    in_or_out="in", label_object=self.label_text_1))
            else:
                QTimer.singleShot(0, lambda: self.animation_label_fade(
                    in_or_out="in", label_object=self.label_text_1))
                self.label_text_1.show()

            # Consequences:
            def execute_consequences():
                self.system_status = "menu_home_1"
                self.label_text_4.setText(GTM.label_text_4(menu="home", var_1=1))

                self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                self.button_switch_right.setEnabled(True)
                self.button_switch_right.clicked.connect(self.menu_home_switch_to_label_2, Qt.UniqueConnection)

                self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=False))
                self.button_switch_left.setEnabled(False)

            QTimer.singleShot(1300, execute_consequences) if not first_init else execute_consequences()

    def menu_home_switch_to_label_2(self):

        if not self.system_status.startswith("menu_home"):
            pass
        else:
            print("entering switch to label 2")

            # Pre-Consequence
            disconnect_button(self.button_switch_right)
            disconnect_button(self.button_switch_left)

            # Animations:
            if self.system_status == "menu_home_1":
                QTimer.singleShot(0, lambda: self.animation_label_fade(
                    in_or_out="out", label_object=self.label_text_1))
                QTimer.singleShot(500, lambda: self.animation_label_slide(
                    in_or_out="in", label_object=self.label_text_2))
            elif self.system_status == "menu_home_3":
                QTimer.singleShot(0, lambda: self.animation_label_slide(
                    in_or_out="out", label_object=self.label_text_3))
                QTimer.singleShot(500, lambda: self.animation_label_fade(
                    in_or_out="in", label_object=self.label_text_2))

            # Consequences:
            def execute_consequences():
                self.system_status = "menu_home_2"
                self.label_text_4.setText(GTM.label_text_4(menu="home", var_1=2))

                self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                self.button_switch_right.setEnabled(True)
                self.button_switch_right.clicked.connect(self.menu_home_switch_to_label_3, Qt.UniqueConnection)

                self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                self.button_switch_left.setEnabled(True)
                self.button_switch_left.clicked.connect(self.menu_home_switch_to_label_1, Qt.UniqueConnection)

            QTimer.singleShot(1300, execute_consequences)

    def menu_home_switch_to_label_3(self):
        if not self.system_status.startswith("menu_home"):
            pass
        else:
            print("entering switch to label 3")

            # Pre-Consequence
            disconnect_button(self.button_switch_right)
            disconnect_button(self.button_switch_left)

            # Animations:
            QTimer.singleShot(0, lambda: self.animation_label_fade(
                in_or_out="out", label_object=self.label_text_2))
            QTimer.singleShot(500, lambda: self.animation_label_slide(
                in_or_out="in", label_object=self.label_text_3))

            # Consequences:
            def execute_consequences():
                self.system_status = "menu_home_3"
                self.label_text_4.setText(GTM.label_text_4(menu="home", var_1=3))

                self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=False))
                self.button_switch_right.setEnabled(False)

                self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                self.button_switch_left.setEnabled(True)
                self.button_switch_left.clicked.connect(self.menu_home_switch_to_label_2, Qt.UniqueConnection)

            QTimer.singleShot(1300, execute_consequences)


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
