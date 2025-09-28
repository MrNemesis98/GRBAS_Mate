import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGraphicsOpacityEffect
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, QAbstractAnimation, QEventLoop
from PyQt5.QtCore import Qt, QTimer, QPoint

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

        self.button_main_ctrl_faq = QPushButton(self)
        self.button_main_ctrl_faq.setGeometry(1230, 20, 40, 40)
        self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))

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

        self.button_main_nav_description = QPushButton(self)
        self.button_main_nav_description.setGeometry(10, 210, 60, 60)

        self.button_main_nav_study = QPushButton(self)
        self.button_main_nav_study.setGeometry(10, 310, 60, 60)

        self.button_main_nav_training = QPushButton(self)
        self.button_main_nav_training.setGeometry(10, 410, 60, 60)

        self.button_main_nav_settings = QPushButton(self)
        self.button_main_nav_settings.setGeometry(10, 720, 60, 60)

        self.disconnect_main_menu_buttons(connect_instead=True)

        # Parameter Elements (8 Buttons) -------------------------------------------------------------------------------
        # [Start, Instability, Fluency, Grade, Roughness, Breathyness, Asthenia, Strain]
        self.button_param_start = QPushButton(self)
        self.button_param_start.setGeometry(130, self.height()-80, 160, 70)
        self.button_param_start.setText("Intro")

        self.button_param_instability = QPushButton(self)
        self.button_param_instability.setGeometry(460, self.height()-80, 60, 70)
        self.button_param_instability.setText("I")

        self.button_param_fluency = QPushButton(self)
        self.button_param_fluency.setGeometry(520, self.height() - 80, 60, 70)
        self.button_param_fluency.setText("F")

        self.button_param_extension = QPushButton(self)
        self.button_param_extension.setGeometry(580, self.height() - 80, 60, 70)
        self.button_param_extension.setText("-")

        self.button_param_grade = QPushButton(self)
        self.button_param_grade.setGeometry(640, self.height() - 80, 60, 70)
        self.button_param_grade.setText("G")

        self.button_param_roughness = QPushButton(self)
        self.button_param_roughness.setGeometry(700, self.height()-80, 60, 70)
        self.button_param_roughness.setText("R")

        self.button_param_breathyness = QPushButton(self)
        self.button_param_breathyness.setGeometry(760, self.height() - 80, 60, 70)
        self.button_param_breathyness.setText("B")

        self.button_param_asthenia = QPushButton(self)
        self.button_param_asthenia.setGeometry(820, self.height() - 80, 60, 70)
        self.button_param_asthenia.setText("A")

        self.button_param_strain = QPushButton(self)
        self.button_param_strain.setGeometry(880, self.height() - 80, 60, 70)
        self.button_param_strain.setText("S")

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
        self.button_switch_down = QPushButton(self)
        self.button_switch_up = QPushButton(self)

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
        self.button_switch_down.hide()
        self.button_switch_up.hide()

        self.button_param_start.hide()
        self.button_param_instability.hide()
        self.button_param_fluency.hide()
        self.button_param_extension.hide()
        self.button_param_grade.hide()
        self.button_param_roughness.hide()
        self.button_param_breathyness.hide()
        self.button_param_asthenia.hide()
        self.button_param_strain.hide()

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

        self.label_text_2.setGeometry(self.width()-20, 220, 1000, 320)
        self.label_text_2.setText(GTM.label_text_2(menu="home"))
        self.label_text_2.show()

        self.label_text_3.setGeometry(self.width()-20, 220, 1000, 320)
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
        self.system_status = "menu_description_1"
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

        self.label_text_1.setGeometry(130, 220, 1000, 320)
        self.label_text_1.show()

        """
        self.label_text_4.setGeometry(230, 600, 300, 70)
        self.label_text_4.setText(GTM.label_text_4(menu="description", var_1=1))
        self.label_text_4.hide()
        """

        self.button_switch_left.setGeometry(1170, 345, 70, 70)
        self.button_switch_left.show()

        self.button_switch_right.setGeometry(1260, 345, 70, 70)
        self.button_switch_right.show()

        self.button_param_start.show()
        self.button_param_instability.show()
        self.button_param_fluency.show()
        self.button_param_extension.show()
        self.button_param_grade.show()
        self.button_param_roughness.show()
        self.button_param_breathyness.show()
        self.button_param_asthenia.show()
        self.button_param_strain.show()

        self.button_switch_down.setGeometry(1290, 720, 70, 70)
        self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False))
        self.button_switch_down.show()
        self.button_switch_up.setGeometry(1000, 700, 70, 70)
        self.button_switch_up.hide()

        self.menu_description_switch(to="start", first_call=True)

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
    def animation_label_fade(self, in_or_out, label_object: QLabel, duration=800):
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
        fade.setDuration(duration)
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
            end_geom = QRect(self.width() - 20,
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

    # Menu Functionality - Button control functions --------------------------------------------------------------------

    def disconnect_main_menu_buttons(self, connect_instead=False):

        if not connect_instead:
            disconnect_button(self.button_main_ctrl_info)
            disconnect_button(self.button_main_ctrl_faq)

            disconnect_button(self.button_main_nav_home)
            disconnect_button(self.button_main_nav_description)
            disconnect_button(self.button_main_nav_study)
            disconnect_button(self.button_main_nav_training)
            disconnect_button(self.button_main_nav_settings)

        else:
            self.button_main_ctrl_info.clicked.connect(self.menu_info)
            self.button_main_ctrl_faq.clicked.connect(self.menu_faq)

            self.button_main_nav_home.clicked.connect(self.menu_home)
            self.button_main_nav_description.clicked.connect(self.menu_description)
            self.button_main_nav_study.clicked.connect(self.menu_study)
            self.button_main_nav_training.clicked.connect(self.menu_training)
            self.button_main_nav_settings.clicked.connect(self.menu_settings)

    def disconnect_parameter_buttons(self, connect_instead=False, menu="", selected_button="Start"):
        if not connect_instead:
            disconnect_button(self.button_param_start)
            disconnect_button(self.button_param_instability)
            disconnect_button(self.button_param_fluency)
            disconnect_button(self.button_param_extension)
            disconnect_button(self.button_param_grade)
            disconnect_button(self.button_param_roughness)
            disconnect_button(self.button_param_breathyness)
            disconnect_button(self.button_param_asthenia)
            disconnect_button(self.button_param_strain)

            self.button_param_start.setStyleSheet(GSS.button_param_start(selected=False))
            self.button_param_instability.setStyleSheet(GSS.button_param_I(selected=False))
            self.button_param_fluency.setStyleSheet(GSS.buttons_param_F_to_A(
                part_of_scale_extension=True,selected=False))
            self.button_param_extension.setStyleSheet(GSS.buttons_param_F_to_A(
                part_of_scale_extension=True, selected=False))
            self.button_param_grade.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_roughness.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_breathyness.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_asthenia.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_strain.setStyleSheet(GSS.button_param_S(selected=False))

        else:
            if menu == "description":
                self.button_param_start.clicked.connect(lambda: self.menu_description_switch(to="start"))
                self.button_param_instability.clicked.connect(lambda: self.menu_description_switch(to="I"))
                self.button_param_fluency.clicked.connect(lambda: self.menu_description_switch(to="F"))
                self.button_param_extension.clicked.connect(lambda: self.menu_description_switch(to="ex"))
                self.button_param_grade.clicked.connect(lambda: self.menu_description_switch(to="G"))
                self.button_param_roughness.clicked.connect(lambda: self.menu_description_switch(to="R"))
                self.button_param_breathyness.clicked.connect(lambda: self.menu_description_switch(to="B"))
                self.button_param_asthenia.clicked.connect(lambda: self.menu_description_switch(to="A"))
                self.button_param_strain.clicked.connect(lambda: self.menu_description_switch(to="S"))

            elif menu == "study":
                pass

            if selected_button.lower() == "start":
                self.button_param_start.setStyleSheet(GSS.button_param_start(selected=True))
            elif selected_button == "I":
                self.button_param_instability.setStyleSheet(GSS.button_param_I(selected=True))
            elif selected_button == "F":
                self.button_param_fluency.setStyleSheet(GSS.buttons_param_F_to_A(
                    part_of_scale_extension=True, selected=True))
            elif selected_button.lower() == "ex":
                self.button_param_extension.setStyleSheet(GSS.buttons_param_F_to_A(
                    part_of_scale_extension=True, selected=True))
            elif selected_button == "G":
                self.button_param_grade.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
            elif selected_button == "R":
                self.button_param_roughness.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
            elif selected_button == "B":
                self.button_param_breathyness.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
            elif selected_button == "A":
                self.button_param_asthenia.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
            else:
                self.button_param_strain.setStyleSheet(GSS.button_param_S(selected=True))

    # Menu Functionality - Submenus ------------------------------------------------------------------------------------
    def menu_home_switch_to_label_1(self, first_init=False):

        if not self.system_status.startswith("menu_home"):
            pass
        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons()

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
                QTimer.singleShot(0, lambda: self.animation_label_fade(
                    in_or_out="in", label_object=self.label_text_2))
                QTimer.singleShot(0, lambda: self.animation_label_fade(
                    in_or_out="in", label_object=self.label_text_3))
                self.label_text_1.show()
                self.label_text_2.show()
                self.label_text_3.show()

            # Consequences:
            def execute_consequences():
                self.system_status = "menu_home_1"
                self.label_text_4.setText(GTM.label_text_4(menu="home", var_1=1))

                self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                self.button_switch_right.setEnabled(True)
                self.button_switch_right.clicked.connect(self.menu_home_switch_to_label_2, Qt.UniqueConnection)

                self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=False))
                self.button_switch_left.setEnabled(False)

                self.disconnect_main_menu_buttons(connect_instead=True)

            QTimer.singleShot(1300, execute_consequences) if not first_init else execute_consequences()

    def menu_home_switch_to_label_2(self):

        if not self.system_status.startswith("menu_home"):
            pass
        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons()

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

                self.disconnect_main_menu_buttons(connect_instead=True)

            QTimer.singleShot(1300, execute_consequences)

    def menu_home_switch_to_label_3(self):
        if not self.system_status.startswith("menu_home"):
            pass
        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons()

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

                self.disconnect_main_menu_buttons(connect_instead=True)

            QTimer.singleShot(1300, execute_consequences)

    def menu_description_switch(self, to, first_call=False):

        if not self.system_status.startswith("menu_description"):
            pass

        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons()
            self.disconnect_parameter_buttons()

            disconnect_button(self.button_switch_left)
            disconnect_button(self.button_switch_right)
            disconnect_button(self.button_switch_up)
            disconnect_button(self.button_switch_down)

            # Animations
            if not first_call:
                QTimer.singleShot(0, lambda: self.animation_label_fade(
                    in_or_out="out", label_object=self.label_text_1, duration=500))
            else:
                QTimer.singleShot(0, lambda: self.animation_label_fade(
                    in_or_out="out", label_object=self.label_text_1, duration=0))

            QTimer.singleShot(700, lambda: self.animation_label_fade(
                in_or_out="in", label_object=self.label_text_1, duration=500))

            def execute_consequences(final_changes_for_submenu=to):

                if final_changes_for_submenu.lower() == "start":

                    self.system_status = "menu_description_1"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=1))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=False))
                    self.button_switch_left.setEnabled(False)

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="I"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="start")

                elif final_changes_for_submenu == "I":
                    self.system_status = "menu_description_2"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=2))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="start"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="F"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="I")

                elif final_changes_for_submenu == "F":
                    self.system_status = "menu_description_3"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=3))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="I"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="ex"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="F")

                elif final_changes_for_submenu.lower() == "ex":
                    self.system_status = "menu_description_4"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=4))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="F"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="G"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="ex")

                elif final_changes_for_submenu == "G":
                    self.system_status = "menu_description_5"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=5))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="ex"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="R"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="G")

                elif final_changes_for_submenu == "R":
                    self.system_status = "menu_description_6"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=6))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="G"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="B"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="R")

                elif final_changes_for_submenu == "B":
                    self.system_status = "menu_description_7"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=7))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="R"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="A"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="B")

                elif final_changes_for_submenu == "A":
                    self.system_status = "menu_description_8"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=8))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="B"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.menu_description_switch(to="S"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="A")

                elif final_changes_for_submenu == "S":
                    self.system_status = "menu_description_9"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=9))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.menu_description_switch(to="A"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=False))
                    self.button_switch_right.setEnabled(False)

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="S")
                else:
                    pass

                self.disconnect_main_menu_buttons(connect_instead=True)

            QTimer.singleShot(700, execute_consequences)


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())
