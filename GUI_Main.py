import sys
import threading

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, QTimer, QAbstractAnimation
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QTimer, QPoint
import time

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

        self.label_text_2 = QLabel(self)
        self.label_text_2.setStyleSheet(GSS.label_text_1())
        self.label_text_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_2.setWordWrap(True)
        self.label_text_2.setTextFormat(Qt.RichText)

        # Buttons (menu internal)
        self.button_menu_internal_1 = QPushButton(self)
        self.

        # Animations ---------------------------------------------------------------------------------------------------
        self._anim_label_fade = None
        self._anim_label_slide = None

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

        self.label_text_1.hide()

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

        self.label_text_1.hide()

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
        self.label_text_1.show()

        self.label_text_2.setGeometry(1350, 220, 1000, 300)
        self.label_text_2.setText(GTM.label_text_2(menu="home"))
        self.label_text_2.show()

        QTimer.singleShot(5000, lambda: self.animation_label_fade(
            in_or_out="out", label_object=self.label_text_1))
        QTimer.singleShot(5500, lambda: self.animation_label_slide(
            in_or_out="in", label_object=self.label_text_2))

        QTimer.singleShot(10000, lambda: self.animation_label_slide(
            in_or_out="out", label_object=self.label_text_2))
        QTimer.singleShot(10500, lambda: self.animation_label_fade(
            in_or_out="in", label_object=self.label_text_1))

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

        self.label_text_1.hide()

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

        self.label_text_1.hide()

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

        self.label_text_1.hide()

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

        self.label_text_1.hide()

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


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
