"""
Copyright © MrNemesis98, GitHub, 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files, to deal in the software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, and to
permit persons to whom the software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
software. The program is provided “as is”, without warranty of any kind, express or implied, including but not
limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
In no event shall the author(s) or copyright holder(s) be liable for any claim, damages or other liability, whether
in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or
other dealings in the software.

By using GRBAS_Mate or one of its components you agree to all these conditions.

------------------------------------------------------------------------------------------------------------------------

This software contains partially modified audio material from the Perceptual Voice Quality Database:
https://data.mendeley.com/datasets/9dz247gnyb/4.
Walden, Patrick R. (2022), “Perceptual Voice Qualities Database (PVQD)”, Mendeley Data, V4, doi: 10.17632/9dz247gnyb.4


CC BY 4.0 licence description (https://creativecommons.org/licenses/by/4.0/)
The files associated with this dataset are licensed under a Creative Commons Attribution 4.0 International licence.
What does this mean?

You can share, copy and modify this dataset so long as you give appropriate credit, provide a link to the CC BY license,
and indicate if changes were made, but you may not do so in a way that suggests the rights holder has endorsed you or
your use of the dataset. Note that further permission may be required for any content within the dataset that is
identified as belonging to a third party.
"""
import os, sys

from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGraphicsOpacityEffect, QComboBox, \
    QStyledItemDelegate, QStyleOptionComboBox, QStylePainter, QStyle, QListWidget, QScrollArea, QFrame, QSizePolicy, \
    QSlider
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, QAbstractAnimation, QEventLoop, QVariantAnimation, \
    QSignalBlocker
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from PyQt5.QtCore import QSequentialAnimationGroup, QPauseAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

# icons for buttons: https://icons8.de/icons/set/free-icons--style-glyph-neue


import GUI_Style_Sheets as GSS
import savedata_manager as SDM

import audiodata_manager as ADM
import audiodata_visualizer as ADV

if SDM.get_current_language() == "en":
    import GUI_Text_Manager_EN as GTM
else:
    pass
    # import GUI_Text_Manager_DE as GTM


def wait_ms(ms: int):
    loop = QEventLoop()
    QTimer.singleShot(ms, loop.quit)
    loop.exec_()


def disconnect_button(button):
    try:
        button.clicked.disconnect()
    except TypeError:
        pass


class CenteredComboBox(QComboBox):
    def paintEvent(self, event):
        opt = QStyleOptionComboBox()
        self.initStyleOption(opt)

        p = QStylePainter(self)
        # 1) Rahmen + Pfeil normal zeichnen
        p.drawComplexControl(QStyle.CC_ComboBox, opt)

        # 2) Rechteck der Textfläche holen
        text_rect = self.style().subControlRect(
            QStyle.CC_ComboBox, opt, QStyle.SC_ComboBoxEditField, self
        )

        text = opt.currentText
        text = p.fontMetrics().elidedText(text, Qt.ElideRight, text_rect.width())

        align = Qt.AlignHCenter | Qt.AlignVCenter
        p.drawItemText(
            text_rect,
            align,
            opt.palette,
            self.isEnabled(),
            text,
            QPalette.ButtonText
        )


def submenu_recordings_time_format_fmt_ms_mmssmmm(ms: int) -> str:
    ms = max(0, ms)
    minutes = ms // 60000
    seconds = (ms % 60000) // 1000
    millis = ms % 1000
    return f"{minutes:02d}:{seconds:02d}.{millis:03d}"


def update_filter_selection(filter_object, idx):
    for i in range(filter_object.count()):
        filter_object.setItemData(i, Qt.AlignLeft, Qt.TextAlignmentRole)
        filter_object.setItemData(i, None, Qt.ForegroundRole)
    if idx >= 0:
        # Header (0) → mittig + grau, echte Werte → mittig + weiß
        if idx == 0:
            filter_object.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
            filter_object.setItemData(0, QColor("#aaaaaa"), Qt.ForegroundRole)
        else:
            filter_object.setItemData(idx, Qt.AlignCenter, Qt.TextAlignmentRole)
            filter_object.setItemData(idx, QColor("#ffffff"), Qt.ForegroundRole)


class MainWindow(QWidget):
    system_status = None
    software_version = "v1.0"

    # Settings variables (to be saved in savedata.txt) *****************************************************************
    gui_language = "eng"

    colour_theme_dark = True

    show_copyright_notice_in_gui_headline = True
    show_copyright_notice_in_home_menu = True

    remember_filtered_audio_files = True    # -> is handled as false if shortcut at descriptions menu is used
    remember_media_player_settings = True
    audio_render_quality = 33

    # system variables for media player control ------------------------------------------------------------------------
    audio_replay = False
    audio_loaded = False
    audio_filtered = False
    audio_played_completely_manually_before = False
    audio_currently_playing = False
    _duration_ms = 0

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

        self.label_main_headline_background = QLabel(self)
        self.label_main_headline_background.setText(GTM.label_main_headline_background(with_copyright=True)) \
            if self.show_copyright_notice_in_gui_headline \
            else self.label_main_headline_background.setText(GTM.label_main_headline_background(with_copyright=False))
        self.label_main_headline_background.setFont(QFont('Noto Sans IPA', 28, QFont.Bold))
        self.label_main_headline_background.setGeometry(0, 0, 1380, 80)
        self.label_main_headline_background.setStyleSheet(GSS.label_main_headline_background(highlight=True))
        self.label_main_headline_background.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_main_headline_background.mousePressEvent = self.headline_mouse_press
        self.label_main_headline_background.mouseMoveEvent = self.headline_mouse_move
        self.label_main_headline_background.mouseReleaseEvent = self.headline_mouse_release
        QTimer.singleShot(4000, lambda: self.label_main_headline_background.setStyleSheet(
            GSS.label_main_headline_background(highlight=False)))

        self.label_main_nav_bar_background = QLabel(self)
        self.label_main_nav_bar_background.setGeometry(0, 80, 80, 720)
        self.label_main_nav_bar_background.setStyleSheet(GSS.label_main_nav_bar_background())

        # Main GUI controls (4 buttons) --------------------------------------------------------------------------------
        # [Info, FAQ, Minimize, Exit]
        self.button_main_ctrl_info = QPushButton(self)
        self.button_main_ctrl_info.setGeometry(1181, 21, 38, 38)
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
        # [Home, Description, Recordings, Training, Settings]
        self.button_main_nav_home = QPushButton(self)
        self.button_main_nav_home.setGeometry(10, 110, 60, 60)

        self.button_main_nav_description = QPushButton(self)
        self.button_main_nav_description.setGeometry(10, 210, 60, 60)

        self.button_main_nav_recordings = QPushButton(self)
        self.button_main_nav_recordings.setGeometry(10, 310, 60, 60)

        self.button_main_nav_training = QPushButton(self)
        self.button_main_nav_training.setGeometry(10, 410, 60, 60)

        self.button_main_nav_settings = QPushButton(self)
        self.button_main_nav_settings.setGeometry(10, 720, 60, 60)

        self.disconnect_main_menu_buttons(connect_instead=True)

        # Parameter Elements (8 Buttons) -------------------------------------------------------------------------------
        # [Start, Instability, Fluency, Grade, Roughness, Breathyness, Asthenia, Strain]
        self.button_param_start = QPushButton(self)
        self.button_param_start.setGeometry(130, self.height() - 80, 160, 70)
        self.button_param_start.setText("Intro")

        self.button_param_instability = QPushButton(self)
        self.button_param_instability.setGeometry(460, self.height() - 80, 60, 70)
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
        self.button_param_roughness.setGeometry(700, self.height() - 80, 60, 70)
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
        self.label_menu_title.setGeometry(130, 100, 415, 80)
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        # for normal text
        self.label_text_1 = QLabel(self)
        self.label_text_1.setStyleSheet(GSS.label_text())
        self.label_text_1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_1.setWordWrap(True)
        self.label_text_1.setTextFormat(Qt.RichText)
        self.label_text_1.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_1.setOpenExternalLinks(True)

        # for normal text
        self.label_text_2 = QLabel(self)
        self.label_text_2.setStyleSheet(GSS.label_text())
        self.label_text_2.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_2.setWordWrap(True)
        self.label_text_2.setTextFormat(Qt.RichText)
        self.label_text_2.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_2.setOpenExternalLinks(True)

        # for normal text
        self.label_text_3 = QLabel(self)
        self.label_text_3.setStyleSheet(GSS.label_text())
        self.label_text_3.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label_text_3.setWordWrap(True)
        self.label_text_3.setTextFormat(Qt.RichText)
        self.label_text_3.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_3.setOpenExternalLinks(True)

        # for headlines
        self.label_text_4 = QLabel(self)
        self.label_text_4.setStyleSheet(GSS.label_text())
        self.label_text_4.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_4.setWordWrap(True)
        self.label_text_4.setTextFormat(Qt.RichText)
        self.label_text_4.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_4.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_5 = QLabel(self)
        self.label_text_5.setStyleSheet(GSS.label_text())
        self.label_text_5.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_5.setWordWrap(True)
        self.label_text_5.setTextFormat(Qt.RichText)
        self.label_text_5.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_5.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_6 = QLabel(self)
        self.label_text_6.setStyleSheet(GSS.label_text())
        self.label_text_6.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_6.setWordWrap(True)
        self.label_text_6.setTextFormat(Qt.RichText)
        self.label_text_6.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_6.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_7 = QLabel(self)
        self.label_text_7.setStyleSheet(GSS.label_text())
        self.label_text_7.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_7.setWordWrap(True)
        self.label_text_7.setTextFormat(Qt.RichText)
        self.label_text_7.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_7.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_8 = QLabel(self)
        self.label_text_8.setStyleSheet(GSS.label_text())
        self.label_text_8.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_8.setWordWrap(True)
        self.label_text_8.setTextFormat(Qt.RichText)
        self.label_text_8.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_8.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_9 = QLabel(self)
        self.label_text_9.setStyleSheet(GSS.label_text())
        self.label_text_9.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_9.setWordWrap(True)
        self.label_text_9.setTextFormat(Qt.RichText)
        self.label_text_9.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_9.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_10 = QLabel(self)
        self.label_text_10.setStyleSheet(GSS.label_text())
        self.label_text_10.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_10.setWordWrap(True)
        self.label_text_10.setTextFormat(Qt.RichText)
        self.label_text_10.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_10.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_11 = QLabel(self)
        self.label_text_11.setStyleSheet(GSS.label_text())
        self.label_text_11.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_11.setWordWrap(True)
        self.label_text_11.setTextFormat(Qt.RichText)
        self.label_text_11.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_11.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_12 = QLabel(self)
        self.label_text_12.setStyleSheet(GSS.label_text())
        self.label_text_12.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_12.setWordWrap(True)
        self.label_text_12.setTextFormat(Qt.RichText)
        self.label_text_12.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_12.setTextFormat(Qt.RichText)

        # for headlines
        self.label_text_13 = QLabel(self)
        self.label_text_13.setStyleSheet(GSS.label_text())
        self.label_text_13.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.label_text_13.setWordWrap(True)
        self.label_text_13.setTextFormat(Qt.RichText)
        self.label_text_13.setTextInteractionFlags(Qt.TextBrowserInteraction)  # Links & Selektion
        self.label_text_13.setTextFormat(Qt.RichText)

        # Buttons (menu internal) --------------------------------------------------------------------------------------
        self.button_switch_right = QPushButton(self)
        self.button_switch_left = QPushButton(self)
        self.button_switch_down = QPushButton(self)
        self.button_switch_up = QPushButton(self)

        # Additional buttons for menu functions assistance (menu internal)
        self.button_assistance_1 = QPushButton(self)
        self.button_assistance_2 = QPushButton(self)
        self.button_assistance_3 = QPushButton(self)
        self.button_assistance_4 = QPushButton(self)

        # QComboBoxes for Recording Filtering --------------------------------------------------------------------------
        self.parameter_filter = CenteredComboBox(self)
        self.parameter_filter.setStyleSheet(GSS.recording_filter_boxes())
        (self.parameter_filter.view()).setSpacing(6)
        self.parameter_filter.setFont(QFont("Arial", int(self.parameter_filter.height() / 2.5)))
        self.parameter_filter.addItems(GTM.QComboBox_parameter_filter())
        self.parameter_filter.setCurrentIndex(7)
        self.parameter_filter.currentIndexChanged.connect(
            lambda: self.submenu_recordings_filter(initiated_by="p"))

        self.severity_filter = CenteredComboBox(self)
        self.severity_filter.setStyleSheet(GSS.recording_filter_boxes())
        (self.severity_filter.view()).setSpacing(6)
        self.severity_filter.setFont(QFont("Arial", int(self.severity_filter.height() / 2.5)))
        self.severity_filter.addItems(GTM.QComboBox_severity_filter())
        self.severity_filter.setCurrentIndex(5)
        self.severity_filter.currentIndexChanged.connect(
            lambda: self.submenu_recordings_filter(initiated_by="s"))

        self.gender_filter = CenteredComboBox(self)
        self.gender_filter.setStyleSheet(GSS.recording_filter_boxes())
        (self.gender_filter.view()).setSpacing(6)
        self.gender_filter.setFont(QFont("Arial", int(self.gender_filter.height() / 2.5)))
        self.gender_filter.addItems(GTM.QComboBox_gender_filter())
        self.gender_filter.setCurrentIndex(2)
        self.gender_filter.currentIndexChanged.connect(
            lambda: self.submenu_recordings_filter(initiated_by="g"))

        self.articulation_filter = CenteredComboBox(self)
        self.articulation_filter.setStyleSheet(GSS.recording_filter_boxes())
        (self.articulation_filter.view()).setSpacing(6)
        self.articulation_filter.setFont(QFont("Arial", int(self.articulation_filter.height() / 2.5)))
        self.articulation_filter.addItems(GTM.QComboBox_articulation_filter())
        self.articulation_filter.setCurrentIndex(3)
        self.articulation_filter.currentIndexChanged.connect(
            lambda: self.submenu_recordings_filter(initiated_by="a"))

        self.audio_file_display = QListWidget(self)
        self.audio_file_display.setStyleSheet(GSS.audio_file_display())
        self.audio_file_display.setFont(QFont("Robo", 13))

        # Scroll Bar ---------------------------------------------------------------------------------------------------

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.NoFrame)

        # Animations ---------------------------------------------------------------------------------------------------
        self._anim_label_fade = None
        self._anim_label_slide = None

        # Objects for Media Player and Audio File Management -----------------------------------------------------------
        self.media_player = QMediaPlayer(self)

        self.audio_file_names = None
        self.audio_file_paths = None
        self.name_of_selected_files = None
        self.path_of_selected_file = None

        self.waveform = ADV.WaveformWidget(self)
        self.waveform.seekRequested.connect(self.media_player.setPosition)

        self._wave_timer = QTimer(self)
        self._wave_timer.setInterval(int(self.audio_render_quality))
        self._wave_timer.timeout.connect(self._tick_waveform)

        self.media_player.stateChanged.connect(self._on_player_state_changed)
        self.media_player.mediaStatusChanged.connect(self.submenu_recordings_check_for_audio_replay)
        self.media_player.setVolume(75)

        self.slider_volume = QSlider(Qt.Horizontal, self)
        self.slider_volume.setRange(0, 100)
        self.slider_volume.setSingleStep(1)
        self.slider_volume.setValue(75)
        self.slider_volume.setStyleSheet(GSS.volume_slider())
        self.slider_volume.valueChanged.connect(self.media_player.setVolume)
        self.slider_volume.valueChanged.connect(self.submenu_recordings_update_volume_display)

        self._peaks_cache = {}  # dict[path -> list[float]]

        self.button_media_play_and_pause = QPushButton(self)
        self.button_media_play_and_pause.setStyleSheet(GSS.button_media_play())

        self.button_media_stop = QPushButton(self)
        self.button_media_stop.setStyleSheet(GSS.button_media_stop())

        self.button_media_previous = QPushButton(self)
        self.button_media_previous.setStyleSheet(GSS.button_media_previous())

        self.button_media_next = QPushButton(self)
        self.button_media_next.setStyleSheet(GSS.button_media_next())

        self.button_media_replay = QPushButton(self)
        self.button_media_replay.setStyleSheet(GSS.button_media_replay())

        # Objects for Settings Menu ------------------------------------------------------------------------------------


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

    # Connection with WaveformWidget ***********************************************************************************
    def _on_player_state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            self._wave_timer.start()
        else:
            self._wave_timer.stop()

    def _tick_waveform(self):
        dur = self.media_player.duration()
        if dur <= 0:
            return
        pos = self.media_player.position()

        self.waveform.setDuration(dur)
        self.waveform.setPosition(pos)

        self.submenu_recordings_update_time_displays(pos)

    # Player Time Management *******************************************************************************************
    def _on_duration_changed(self, ms: int):
        self._duration_ms = max(0, ms)
        # direkt einmal aktualisieren (z.B. nach dem Laden)
        self.submenu_recordings_update_time_displays(self.media_player.position())

    def _on_position_changed(self, ms: int):
        self.submenu_recordings_update_time_displays(ms)

    # Menu independent functions ***************************************************************************************
    def hide_all_menu_internal_elements(self):
        self.label_menu_title.hide()

        self.label_text_1.hide()
        self.label_text_2.hide()
        self.label_text_3.hide()
        self.label_text_4.hide()
        self.label_text_5.hide()
        self.label_text_6.hide()
        self.label_text_7.hide()
        self.label_text_8.hide()
        self.label_text_9.hide()
        self.label_text_10.hide()
        self.label_text_11.hide()
        self.label_text_12.hide()
        self.label_text_13.hide()

        self.button_switch_right.hide()
        self.button_switch_left.hide()
        self.button_switch_down.hide()
        self.button_switch_up.hide()

        self.button_assistance_1.hide()
        self.button_assistance_2.hide()
        self.button_assistance_3.hide()
        self.button_assistance_4.hide()

        self.button_param_start.hide()
        self.button_param_instability.hide()
        self.button_param_fluency.hide()
        self.button_param_extension.hide()
        self.button_param_grade.hide()
        self.button_param_roughness.hide()
        self.button_param_breathyness.hide()
        self.button_param_asthenia.hide()
        self.button_param_strain.hide()

        self.parameter_filter.hide()
        self.severity_filter.hide()
        self.gender_filter.hide()
        self.articulation_filter.hide()

        self.audio_file_display.hide()
        self.waveform.hide()
        self.slider_volume.hide()
        self.submenu_recordings_stop_audio()

        self.button_media_previous.hide()
        self.button_media_replay.hide()
        self.button_media_play_and_pause.hide()
        self.button_media_stop.hide()
        self.button_media_next.hide()

    # Main Menu Layouts ************************************************************************************************
    def menu_info(self):
        self.system_status = "menu_info"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="info")
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="info"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=True))
        self.label_menu_title.show()

        self.button_assistance_1.setGeometry(250, 680, 300, 70)
        self.button_assistance_1.setStyleSheet(GSS.button_assistance_1(selected=True))
        self.button_assistance_1.setText(GTM.button_assistance_1(menu="info"))
        self.button_assistance_1.disconnect()
        self.button_assistance_1.clicked.connect(lambda: self.submenus_info(engaged_by_button_assistance_nr=1))
        self.button_assistance_1.show()

        self.button_assistance_2.setGeometry(550, 680, 300, 70)
        self.button_assistance_2.setStyleSheet(GSS.button_assistance_2(selected=False))
        self.button_assistance_2.setText(GTM.button_assistance_2(menu="info"))
        self.button_assistance_2.disconnect()
        self.button_assistance_2.clicked.connect(lambda: self.submenus_info(engaged_by_button_assistance_nr=2))
        self.button_assistance_2.show()

        self.button_assistance_3.setGeometry(850, 680, 350, 70)
        self.button_assistance_3.setStyleSheet(GSS.button_assistance_3(selected=False))
        self.button_assistance_3.setText(GTM.button_assistance_3(menu="info"))
        self.button_assistance_3.disconnect()
        self.button_assistance_3.clicked.connect(lambda: self.submenus_info(engaged_by_button_assistance_nr=3))
        self.button_assistance_3.show()

        self.label_text_1.setGeometry(130, 175, 1100, 465)
        self.label_text_1.setStyleSheet(GSS.label_text(no_background=True))
        self.animation_label_fade(in_or_out="in", label_object=self.label_text_1, duration=0)
        self.submenus_info(engaged_by_button_assistance_nr=0, first_call=True)

    def menu_faq(self):
        self.system_status = "menu_faq"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="faq")
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="faq"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=True))
        self.label_menu_title.show()

    def menu_home(self):
        self.system_status = "menu_home_1"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="home")
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="home"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

        self.label_text_1.setGeometry(130, 220, 1000, 320)
        self.label_text_1.setText(GTM.label_text_1(menu="home"))
        self.label_text_1.show()

        self.label_text_2.setGeometry(self.width() - 20, 220, 1000, 320)
        self.label_text_2.setText(GTM.label_text_2(menu="home"))
        self.label_text_2.show()

        self.label_text_3.setGeometry(self.width() - 20, 220, 1000, 320)
        self.label_text_3.setText(GTM.label_text_3(menu="home"))
        self.label_text_3.show()

        self.label_text_4.setGeometry(480, 600, 300, 70)
        self.label_text_4.setText(GTM.label_text_4(menu="home", var_1=1))
        self.label_text_4.show()

        if self.show_copyright_notice_in_home_menu:
            self.label_text_5.setGeometry(130, 720, 1000, 70)
            self.label_text_5.setStyleSheet(GSS.label_text(dark_background=False, no_background=True))
            self.label_text_5.setText(GTM.label_text_5(menu="home"))
            QTimer.singleShot(0, lambda: self.animation_label_fade(
                in_or_out="out", label_object=self.label_text_5, duration=0))
            self.label_text_5.show()
            QTimer.singleShot(2000, lambda: self.animation_label_fade(
                in_or_out="in", label_object=self.label_text_5, duration=1000))

        self.button_switch_right.setGeometry(805, 600, 70, 70)
        self.button_switch_right.show()

        self.button_switch_left.setGeometry(385, 600, 70, 70)
        self.button_switch_left.show()

        self.submenu_home_1(first_call=True)

    def menu_description(self):
        self.system_status = "menu_description_1"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="description")
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="description"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

        self.label_text_1.setGeometry(130, 220, 1000, 340)
        self.label_text_1.show()

        self.button_switch_left.setGeometry(1170, 355, 70, 70)
        self.button_switch_left.show()

        self.button_switch_right.setGeometry(1260, 355, 70, 70)
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

        # Down Button serves as shortcut to recordings here
        self.button_switch_down.setGeometry(1130, 720, 70, 70)
        self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                     dress_as_recording=True))
        self.button_switch_down.show()
        self.button_switch_up.setGeometry(1000, 700, 70, 70)
        self.button_switch_up.hide()

        self.submenus_description(to="start", first_call=True)

    def menu_recordings(self, initiated_by_descriptions_shortcut = False, parameter_to_filter=""):
        self.system_status = "menu_recordings"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="recordings")
        self.disconnect_media_player_elements()
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="recordings"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

        # set filter frame ---------------------------------------------
        self.label_text_1.setGeometry(130, 230, 1200, 120)
        self.label_text_1.setStyleSheet(GSS.label_text(frame_only=True))
        self.label_text_1.clear()
        self.label_text_1.show()

        self.label_text_4.setGeometry(580, 180, 300, 50)
        self.label_text_4.setStyleSheet(GSS.label_text(top_module=True))
        self.label_text_4.setText(GTM.label_text_4(menu="recordings"))
        self.label_text_4.show()

        # set filters
        self.label_text_7.setGeometry(150, 250, 200, 30)
        self.label_text_7.setText(GTM.label_text_7(menu="recordings"))
        self.label_text_7.setStyleSheet(GSS.label_text(no_background=True))
        self.label_text_7.show()

        self.parameter_filter.setGeometry(150, 280, 200, 50)
        # self.parameter_filter.setFont(QFont("Arial", int(self.parameter_filter.height() / 3.5)))
        self.parameter_filter.show()

        self.label_text_8.setGeometry(470, 250, 200, 30)
        self.label_text_8.setText(GTM.label_text_8(menu="recordings"))
        self.label_text_8.setStyleSheet(GSS.label_text(no_background=True))
        self.label_text_8.show()

        self.severity_filter.setGeometry(470, 280, 200, 50)
        # self.severity_filter.setFont(QFont("Arial", int(self.severity_filter.height() / 3)))
        self.severity_filter.show()

        self.label_text_9.setGeometry(790, 250, 200, 30)
        self.label_text_9.setText(GTM.label_text_9(menu="recordings"))
        self.label_text_9.setStyleSheet(GSS.label_text(no_background=True))
        self.label_text_9.show()

        self.gender_filter.setGeometry(790, 280, 200, 50)
        # self.gender_filter.setFont(QFont("Arial", int(self.gender_filter.height() / 2.7)))
        self.gender_filter.show()

        self.label_text_10.setGeometry(1110, 250, 200, 30)
        self.label_text_10.setText(GTM.label_text_10(menu="recordings"))
        self.label_text_10.setStyleSheet(GSS.label_text(no_background=True))
        self.label_text_10.show()

        self.articulation_filter.setGeometry(1110, 280, 200, 50)
        # self.articulation_filter.setFont(QFont("Arial", int(self.articulation_filter.height() / 2.7)))
        self.articulation_filter.show()

        # set files list frame -----------------------------------------
        self.label_text_2.setGeometry(130, 450, 575, 300)
        self.label_text_2.setStyleSheet(GSS.label_text(frame_only=True))
        self.label_text_2.clear()
        self.label_text_2.show()

        self.label_text_5.setGeometry(247, 400, 340, 50)
        self.label_text_5.setStyleSheet(GSS.label_text(top_module=True))
        self.label_text_5.setText(GTM.label_text_5(menu="recordings"))
        self.label_text_5.show()

        self.audio_file_display.setGeometry(133, 453, 569, 294)
        self.audio_file_display.clicked.connect(self.submenu_recordings_load_audio)
        self.audio_file_display.show()

        # set "Media Player" frame ----------------------------------
        self.label_text_3.setGeometry(755, 450, 575, 300)
        self.label_text_3.setStyleSheet(GSS.label_text(frame_only=True))
        self.label_text_3.clear()
        self.label_text_3.show()

        self.label_text_6.setGeometry(872, 400, 340, 50)
        self.label_text_6.setStyleSheet(GSS.label_text(top_module=True))
        self.label_text_6.setText(GTM.label_text_6(menu="recordings"))
        self.label_text_6.show()

        # volume
        self.label_text_11.setGeometry(892, 465, 301, 30)
        self.label_text_11.setStyleSheet(GSS.label_text(no_background=True))
        self.label_text_11.show()

        self.slider_volume.setGeometry(892, 495, 301, 30)
        self.slider_volume.show()
        self.submenu_recordings_update_volume_display()

        # time displays
        self.label_text_12.setGeometry(755, 465, 125, 60)
        self.label_text_12.setStyleSheet(GSS.label_text(no_background=True))
        self.label_text_12.setText("00:00:000")
        self.label_text_12.show()

        self.label_text_13.setGeometry(1205, 465, 125, 60)
        self.label_text_13.setStyleSheet(GSS.label_text_time_display_layout())
        self.label_text_13.setText("-00:00:000")
        self.label_text_13.show()

        self.waveform.setGeometry(755, 530, 575, 140)
        self.waveform.setStyleSheet(GSS.waveform())
        self.media_player.positionChanged.connect(self.waveform.setPosition)
        self.media_player.durationChanged.connect(self.waveform.setDuration)
        self.media_player.durationChanged.connect(self._on_duration_changed)
        self.media_player.positionChanged.connect(self._on_position_changed)
        self.waveform.show()

        # self.media_player.mediaStatusChanged.connect(self.submenu_recordings_check_for_audio_replay)

        self.button_media_previous.setGeometry(817, 685, 50, 50)
        self.button_media_previous.clicked.connect(self.submenu_recordings_previous_audio)
        self.button_media_previous.show()

        self.button_media_replay.setGeometry(917, 685, 50, 50)
        self.button_media_replay.clicked.connect(self.submenu_recordings_replay_audio_ctrl)
        self.button_media_replay.show()

        self.button_media_play_and_pause.setGeometry(1017, 685, 50, 50)
        self.button_media_play_and_pause.clicked.connect(self.submenu_recordings_play_and_pause_audio)
        self.button_media_play_and_pause.show()

        self.button_media_stop.setGeometry(1117, 685, 50, 50)
        self.button_media_stop.clicked.connect(self.submenu_recordings_stop_audio)
        self.button_media_stop.show()

        self.button_media_next.setGeometry(1217, 685, 50, 50)
        self.button_media_next.clicked.connect(self.submenu_recordings_next_audio)
        self.button_media_next.show()

        if not self.remember_filtered_audio_files:
            self.parameter_filter.setCurrentIndex(7)
            self.severity_filter.setCurrentIndex(5)
            self.gender_filter.setCurrentIndex(2)
            self.articulation_filter.setCurrentIndex(3)
            self.audio_file_display.clear()
            self.audio_loaded = False
            self.audio_filtered = False

        if not self.remember_media_player_settings:
            self.media_player.setVolume(75)
            self.slider_volume.setValue(75)
            self.submenu_recordings_replay_audio_ctrl(set_offline=True)

        if initiated_by_descriptions_shortcut:
            self.severity_filter.setCurrentIndex(5)
            self.gender_filter.setCurrentIndex(2)
            self.articulation_filter.setCurrentIndex(3)
            self.audio_file_display.clear()
            self.audio_loaded = False
            self.audio_filtered = False

            if parameter_to_filter == "I":
                self.parameter_filter.setCurrentIndex(0)
            elif parameter_to_filter == "F":
                self.parameter_filter.setCurrentIndex(1)
            elif parameter_to_filter == "G":
                self.parameter_filter.setCurrentIndex(2)
            elif parameter_to_filter == "R":
                self.parameter_filter.setCurrentIndex(3)
            elif parameter_to_filter == "B":
                self.parameter_filter.setCurrentIndex(4)
            elif parameter_to_filter == "A":
                self.parameter_filter.setCurrentIndex(5)
            elif parameter_to_filter == "S":
                self.parameter_filter.setCurrentIndex(6)
            else:
                self.parameter_filter.setCurrentIndex(7)

            self.submenu_recordings_filter(initiated_by="descriptions_shortcut")

    def menu_training(self):
        self.system_status = "menu_training"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="training")
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="training"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

        self.label_text_4.setGeometry(550, 200, 200, 70)
        self.label_text_4.setStyleSheet(GSS.label_text(dark_background=True))
        self.label_text_4.setText(GTM.label_text_4(menu="training"))

        self.label_text_1.setGeometry(130, 300, 1100, 300)
        self.label_text_1.setText(GTM.label_text_1(menu="training"))
        self.label_text_1.setStyleSheet(GSS.label_text(no_background=False))

        QTimer.singleShot(0, lambda: self.animation_label_fade(
            in_or_out="out", label_object=self.label_text_4, duration=0))
        QTimer.singleShot(0, lambda: self.animation_label_fade(
            in_or_out="out", label_object=self.label_text_1, duration=0))
        self.label_text_4.show()
        self.label_text_1.show()
        QTimer.singleShot(500, lambda: self.animation_label_fade(
            in_or_out="in", label_object=self.label_text_4, duration=1000))
        QTimer.singleShot(1000, lambda: self.animation_label_fade(
            in_or_out="in", label_object=self.label_text_1, duration=1000))

    def menu_settings(self):
        self.system_status = "menu_settings"
        self.hide_all_menu_internal_elements()
        self.disconnect_main_menu_buttons(connect_instead=True, current_menu="settings")
        self.reset_text_label_stylesheets()

        self.label_menu_title.setText(GTM.label_menu_title(menu="settings"))
        self.label_menu_title.setStyleSheet(GSS.label_menu_title(main_ctrl=False))
        self.label_menu_title.show()

        self.label_text_1.setGeometry(110, 360, 180, 240)
        self.label_text_1.setStyleSheet(GSS.label_settings_zero())
        self.label_text_1.setText("")
        self.label_text_1.show()

        self.label_text_2.setGeometry(540, 160, 600, 200)
        self.label_text_2.setStyleSheet(GSS.label_settings_frame_top())
        self.label_text_2.setText("")
        self.label_text_2.show()

        self.label_text_3.setGeometry(720, 480, 600, 200)
        self.label_text_3.setStyleSheet(GSS.label_settings_frame_bottom())
        self.label_text_3.setText("")
        self.label_text_3.show()

        self.label_text_4.setGeometry(570, 190, 720, 460)
        self.label_text_4.setStyleSheet(GSS.label_text(dark_background=True))
        self.label_text_4.setText("")
        self.label_text_4.show()

        self.label_text_5.setGeometry(570, 705, 720, 70)
        self.label_text_5.setStyleSheet(GSS.label_text(dark_background=True))
        self.animation_label_fade(in_or_out="out", label_object=self.label_text_5, duration=0)
        self.label_text_5.setText(GTM.label_text_5(menu="settings"))
        self.label_text_5.hide()

        self.button_assistance_1.setGeometry(135, 275, 300, 80)
        self.button_assistance_1.setStyleSheet(GSS.button_assistance_1(selected=False, settings=True))
        self.button_assistance_1.setText(GTM.button_assistance_1(menu="settings"))
        self.button_assistance_1.disconnect()
        self.button_assistance_1.clicked.connect(lambda: self.submenus_settings(setting=1))
        self.button_assistance_1.show()

        self.button_assistance_2.setGeometry(135, 385, 300, 80)
        self.button_assistance_2.setStyleSheet(GSS.button_assistance_2(selected=False, settings=True))
        self.button_assistance_2.setText(GTM.button_assistance_2(menu="settings"))
        self.button_assistance_2.disconnect()
        self.button_assistance_2.clicked.connect(lambda: self.submenus_settings(setting=2))
        self.button_assistance_2.show()

        self.button_assistance_3.setGeometry(135, 495, 300, 80)
        self.button_assistance_3.setStyleSheet(GSS.button_assistance_3(selected=False, settings=True))
        self.button_assistance_3.setText(GTM.button_assistance_3(menu="settings"))
        self.button_assistance_3.disconnect()
        self.button_assistance_3.clicked.connect(lambda: self.submenus_settings(setting=3))
        self.button_assistance_3.show()

        self.button_assistance_4.setGeometry(135, 650, 300, 80)
        self.button_assistance_4.setStyleSheet(GSS.button_assistance_4(settings=True))
        self.button_assistance_4.setText(GTM.button_assistance_4(menu="settings"))
        self.button_assistance_4.disconnect()
        self.button_assistance_4.clicked.connect(lambda: self.submenu_setting_restart())
        self.button_assistance_4.show()



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

    def disconnect_main_menu_buttons(self, connect_instead=False, current_menu=""):

        # manage button functions
        if not connect_instead:

            disconnect_button(self.button_main_ctrl_info)
            disconnect_button(self.button_main_ctrl_faq)
            disconnect_button(self.button_main_nav_home)
            disconnect_button(self.button_main_nav_description)
            disconnect_button(self.button_main_nav_recordings)
            disconnect_button(self.button_main_nav_training)
            disconnect_button(self.button_main_nav_settings)

        else:
            self.button_main_ctrl_info.clicked.connect(self.menu_info)
            self.button_main_ctrl_faq.clicked.connect(self.menu_faq)
            self.button_main_nav_home.clicked.connect(self.menu_home)
            self.button_main_nav_description.clicked.connect(self.menu_description)
            self.button_main_nav_recordings.clicked.connect(self.menu_recordings)
            self.button_main_nav_training.clicked.connect(self.menu_training)
            self.button_main_nav_settings.clicked.connect(self.menu_settings)

            # manage stylesheets
            if current_menu == "info":
                disconnect_button(self.button_main_ctrl_info)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=True))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "copyright":
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "faq":
                disconnect_button(self.button_main_ctrl_faq)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=True))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "home":
                disconnect_button(self.button_main_nav_home)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=True))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "description":
                disconnect_button(self.button_main_nav_description)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=True))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "recordings":
                disconnect_button(self.button_main_nav_recordings)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=True))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "training":
                disconnect_button(self.button_main_nav_training)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=True))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=False))
            elif current_menu == "settings":
                disconnect_button(self.button_main_nav_settings)
                self.button_main_ctrl_info.setStyleSheet(GSS.button_main_ctrl_info(pressed=False))
                self.button_main_ctrl_faq.setStyleSheet(GSS.button_main_ctrl_faq(pressed=False))
                self.button_main_nav_home.setStyleSheet(GSS.button_main_nav_home(pressed=False))
                self.button_main_nav_description.setStyleSheet(GSS.button_main_nav_description(pressed=False))
                self.button_main_nav_recordings.setStyleSheet(GSS.button_main_nav_recordings(pressed=False))
                self.button_main_nav_training.setStyleSheet(GSS.button_main_nav_training(pressed=False))
                self.button_main_nav_settings.setStyleSheet(GSS.button_main_nav_settings(pressed=True))

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
                part_of_scale_extension=True, selected=False))
            self.button_param_extension.setStyleSheet(GSS.buttons_param_F_to_A(
                part_of_scale_extension=True, selected=False))
            self.button_param_grade.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_roughness.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_breathyness.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_asthenia.setStyleSheet(GSS.buttons_param_F_to_A(selected=False))
            self.button_param_strain.setStyleSheet(GSS.button_param_S(selected=False))

        else:
            if menu == "description":
                self.button_param_start.clicked.connect(lambda: self.submenus_description(to="start"))
                self.button_param_instability.clicked.connect(lambda: self.submenus_description(to="I"))
                self.button_param_fluency.clicked.connect(lambda: self.submenus_description(to="F"))
                self.button_param_extension.clicked.connect(lambda: self.submenus_description(to="ex"))
                self.button_param_grade.clicked.connect(lambda: self.submenus_description(to="G"))
                self.button_param_roughness.clicked.connect(lambda: self.submenus_description(to="R"))
                self.button_param_breathyness.clicked.connect(lambda: self.submenus_description(to="B"))
                self.button_param_asthenia.clicked.connect(lambda: self.submenus_description(to="A"))
                self.button_param_strain.clicked.connect(lambda: self.submenus_description(to="S"))

                self.button_param_start.setEnabled(True)
                self.button_param_instability.setEnabled(True)
                self.button_param_fluency.setEnabled(True)
                self.button_param_extension.setEnabled(True)
                self.button_param_grade.setEnabled(True)
                self.button_param_roughness.setEnabled(True)
                self.button_param_breathyness.setEnabled(True)
                self.button_param_asthenia.setEnabled(True)
                self.button_param_strain.setEnabled(True)

            elif menu == "recordings":
                pass

            if selected_button.lower() == "start":
                self.button_param_start.setStyleSheet(GSS.button_param_start(selected=True))
                self.button_param_start.setEnabled(False)
            elif selected_button == "I":
                self.button_param_instability.setStyleSheet(GSS.button_param_I(selected=True))
                self.button_param_instability.setEnabled(False)
            elif selected_button == "F":
                self.button_param_fluency.setStyleSheet(GSS.buttons_param_F_to_A(
                    part_of_scale_extension=True, selected=True))
                self.button_param_fluency.setEnabled(False)
            elif selected_button.lower() == "ex":
                self.button_param_extension.setStyleSheet(GSS.buttons_param_F_to_A(
                    part_of_scale_extension=True, selected=True))
                self.button_param_extension.setEnabled(False)
            elif selected_button == "G":
                self.button_param_grade.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
                self.button_param_grade.setEnabled(False)
            elif selected_button == "R":
                self.button_param_roughness.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
                self.button_param_roughness.setEnabled(False)
            elif selected_button == "B":
                self.button_param_breathyness.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
                self.button_param_breathyness.setEnabled(False)
            elif selected_button == "A":
                self.button_param_asthenia.setStyleSheet(GSS.buttons_param_F_to_A(selected=True))
                self.button_param_asthenia.setEnabled(False)
            else:
                self.button_param_strain.setStyleSheet(GSS.button_param_S(selected=True))
                self.button_param_strain.setEnabled(False)

    def disconnect_media_player_elements(self):
        self.audio_file_display.disconnect()
        self.button_media_play_and_pause.disconnect()
        self.button_media_stop.disconnect()
        self.button_media_replay.disconnect()
        self.button_media_previous.disconnect()
        self.button_media_next.disconnect()

    def disable_filter_checkboxes(self, enable_instead=False):
        self.parameter_filter.setEnabled(enable_instead)
        self.severity_filter.setEnabled(enable_instead)
        self.gender_filter.setEnabled(enable_instead)
        self.articulation_filter.setEnabled(enable_instead)

    def reset_text_label_stylesheets(self):
        self.label_text_1.setStyleSheet(GSS.label_text())
        self.label_text_2.setStyleSheet(GSS.label_text())
        self.label_text_3.setStyleSheet(GSS.label_text())
        self.label_text_4.setStyleSheet(GSS.label_text())

    # Menu Functionality - Submenus ------------------------------------------------------------------------------------

    def submenus_info(self, engaged_by_button_assistance_nr, first_call=False):
        if not self.system_status.startswith("menu_info"):
            pass
        else:
            if engaged_by_button_assistance_nr == 1 or first_call:
                self.system_status = "menu_info_1"
                self.button_assistance_1.setStyleSheet(GSS.button_assistance_1(selected=True))
                self.button_assistance_2.setStyleSheet(GSS.button_assistance_2(selected=False))
                self.button_assistance_3.setStyleSheet(GSS.button_assistance_3(selected=False))
                self.label_text_1.show()
                self.label_text_1.setText(GTM.label_text_1(menu="info", var_1=1,
                                                           software_version=self.software_version))
            elif engaged_by_button_assistance_nr == 2:
                self.system_status = "menu_info_2"
                self.button_assistance_1.setStyleSheet(GSS.button_assistance_1(selected=False))
                self.button_assistance_2.setStyleSheet(GSS.button_assistance_2(selected=True))
                self.button_assistance_3.setStyleSheet(GSS.button_assistance_3(selected=False))
                self.label_text_1.show()
                self.label_text_1.setText(GTM.label_text_1(menu="info", var_1=2,
                                                           software_version=self.software_version))
            else:
                self.system_status = "menu_info_3"
                self.button_assistance_1.setStyleSheet(GSS.button_assistance_1(selected=False))
                self.button_assistance_2.setStyleSheet(GSS.button_assistance_2(selected=False))
                self.button_assistance_3.setStyleSheet(GSS.button_assistance_3(selected=True))
                self.label_text_1.show()
                self.label_text_1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
                self.label_text_1.setWordWrap(True)
                self.label_text_1.setText(GTM.label_text_1(menu="info", var_1=3,
                                                           software_version=self.software_version))

    def submenu_home_1(self, first_call=False):

        if not self.system_status.startswith("menu_home"):
            pass
        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons(connect_instead=False, current_menu="home")

            disconnect_button(self.button_switch_right)
            disconnect_button(self.button_switch_left)

            # Animations:
            if not first_call:
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
                self.button_switch_right.clicked.connect(self.submenu_home_2, Qt.UniqueConnection)

                self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=False))
                self.button_switch_left.setEnabled(False)

                self.disconnect_main_menu_buttons(connect_instead=True, current_menu="home")

            QTimer.singleShot(1300, execute_consequences) if not first_call else execute_consequences()

    def submenu_home_2(self):

        if not self.system_status.startswith("menu_home"):
            pass
        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons(connect_instead=False, current_menu="home")

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
                self.button_switch_right.clicked.connect(self.submenu_home_3, Qt.UniqueConnection)

                self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                self.button_switch_left.setEnabled(True)
                self.button_switch_left.clicked.connect(self.submenu_home_1, Qt.UniqueConnection)

                self.disconnect_main_menu_buttons(connect_instead=True, current_menu="home")

            QTimer.singleShot(1300, execute_consequences)

    def submenu_home_3(self):
        if not self.system_status.startswith("menu_home"):
            pass
        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons(connect_instead=False, current_menu="home")

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
                self.button_switch_left.clicked.connect(self.submenu_home_2, Qt.UniqueConnection)

                self.disconnect_main_menu_buttons(connect_instead=True, current_menu="home")

            QTimer.singleShot(1300, execute_consequences)

    def submenus_description(self, to, first_call=False):

        if not self.system_status.startswith("menu_description"):
            pass

        else:
            # Pre-Consequence
            self.disconnect_main_menu_buttons(connect_instead=False, current_menu="description")
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
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="I"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=False, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(False)

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="start")

                elif final_changes_for_submenu == "I":
                    self.system_status = "menu_description_2"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=2))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="start"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="F"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="I"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="I")

                elif final_changes_for_submenu == "F":
                    self.system_status = "menu_description_3"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=3))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="I"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="ex"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="F"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="F")

                elif final_changes_for_submenu.lower() == "ex":
                    self.system_status = "menu_description_4"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=4))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="F"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="G"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=False, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(False)

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="ex")

                elif final_changes_for_submenu == "G":
                    self.system_status = "menu_description_5"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=5))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="ex"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="R"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="G"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="G")

                elif final_changes_for_submenu == "R":
                    self.system_status = "menu_description_6"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=6))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="G"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="B"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="R"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="R")

                elif final_changes_for_submenu == "B":
                    self.system_status = "menu_description_7"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=7))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="R"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="A"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="B"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="B")

                elif final_changes_for_submenu == "A":
                    self.system_status = "menu_description_8"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=8))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="B"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=True))
                    self.button_switch_right.setEnabled(True)
                    self.button_switch_right.clicked.connect(lambda: self.submenus_description(to="S"))

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="A"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="A")

                elif final_changes_for_submenu == "S":
                    self.system_status = "menu_description_9"
                    self.label_text_1.setText(GTM.label_text_1(menu="description", var_1=9))

                    self.button_switch_left.setStyleSheet(GSS.button_switch_left(active=True))
                    self.button_switch_left.setEnabled(True)
                    self.button_switch_left.clicked.connect(lambda: self.submenus_description(to="A"))

                    self.button_switch_right.setStyleSheet(GSS.button_switch_right(active=False))
                    self.button_switch_right.setEnabled(False)

                    self.button_switch_down.setStyleSheet(GSS.button_switch_down(active=True, waiting=False,
                                                                                 dress_as_recording=True))
                    self.button_switch_down.setEnabled(True)
                    self.button_switch_down.clicked.connect(
                        lambda: self.menu_recordings(initiated_by_descriptions_shortcut=True, parameter_to_filter="S"))

                    self.disconnect_parameter_buttons(connect_instead=True, menu="description", selected_button="S")
                else:
                    pass

                self.disconnect_main_menu_buttons(connect_instead=True, current_menu="description")

            QTimer.singleShot(700, execute_consequences)

    def submenu_recordings_filter(self, initiated_by=""):

        if not self.system_status.startswith("menu_recordings"):
            pass

        else:

            # simple case distinction for every filter shall ensure
            # stability of filter reading even if the texts for the QComboboxes are changed
            # -> the call for ADM.get_param_recs() is therefore based on the filters´ indexes, not textual descriptions
            parameter = None
            if self.parameter_filter.currentIndex() == 0:
                parameter = "I"
            elif self.parameter_filter.currentIndex() == 1:
                parameter = "F"
            elif self.parameter_filter.currentIndex() == 2:
                parameter = "G"
            elif self.parameter_filter.currentIndex() == 3:
                parameter = "R"
            elif self.parameter_filter.currentIndex() == 4:
                parameter = "B"
            elif self.parameter_filter.currentIndex() == 5:
                parameter = "A"
            elif self.parameter_filter.currentIndex() == 6:
                parameter = "S"
            else:
                pass

            severity = str(self.severity_filter.currentIndex()) \
                if self.severity_filter.currentIndex() != 5 else None
            # (-> special case "ascending severity levels", treated as "theoretical level 4")

            gender = str(self.gender_filter.currentIndex()) \
                if self.gender_filter.currentIndex() != 2 else None

            articulation = str(self.articulation_filter.currentIndex()) \
                if self.articulation_filter.currentIndex() != 3 else None

            def update_audio_file_selection_display():
                if self.audio_currently_playing:
                    self.submenu_recordings_stop_audio()

                self.audio_file_names, self.audio_file_paths = ADM.get_param_recs(parameter=parameter,
                                                                                  severity_level=severity,
                                                                                  gender=gender,
                                                                                  articulation=articulation)

                self.audio_file_display.setUpdatesEnabled(False)
                self.audio_file_display.clear()

                for file in self.audio_file_names:
                    self.audio_file_display.addItem(file)

                self.audio_file_display.setUpdatesEnabled(True)
                self.audio_file_display.repaint()

                self.audio_filtered = True
                self.audio_loaded = False

                self.waveform.setPeaks([])
                self.waveform.setDuration(1)
                self.waveform.setPosition(0)

            # check dependencies -------------------------------------------------------------

            # 1) A selection of severity to "Level 0" resets parameter to "All Options"
            if initiated_by == "s" and severity == "0" and self.parameter_filter.currentIndex() != 7:
                self.audio_file_display.clear()
                self.disable_filter_checkboxes()
                self.parameter_filter.setStyleSheet(GSS.recording_filter_boxes(red=True))
                self.parameter_filter.blockSignals(True)
                QTimer.singleShot(800, lambda: self.parameter_filter.setCurrentIndex(7))
                QTimer.singleShot(800, lambda: self.parameter_filter.setStyleSheet(
                    GSS.recording_filter_boxes(green=True)))
                QTimer.singleShot(1500, lambda: self.parameter_filter.blockSignals(False))
                QTimer.singleShot(1500, lambda: self.parameter_filter.setStyleSheet(GSS.recording_filter_boxes()))
                QTimer.singleShot(1500, lambda: self.disable_filter_checkboxes(enable_instead=True))
                parameter = None

                QTimer.singleShot(800, lambda: update_audio_file_selection_display())

            # 2) If parameter is set and severity is 0, severity will be reset to "All Options"
            elif initiated_by == "p" and self.parameter_filter.currentIndex() != 7 and severity == "0":
                self.audio_file_display.clear()
                self.disable_filter_checkboxes()
                self.severity_filter.setStyleSheet(GSS.recording_filter_boxes(red=True))
                self.severity_filter.blockSignals(True)
                QTimer.singleShot(800, lambda: self.severity_filter.setCurrentIndex(5))
                QTimer.singleShot(800, lambda: self.severity_filter.setStyleSheet(
                    GSS.recording_filter_boxes(green=True)))
                QTimer.singleShot(1500, lambda: self.severity_filter.blockSignals(False))
                QTimer.singleShot(1500, lambda: self.severity_filter.setStyleSheet(GSS.recording_filter_boxes()))
                QTimer.singleShot(1500, lambda: self.disable_filter_checkboxes(enable_instead=True))
                severity = None

                QTimer.singleShot(800, lambda: update_audio_file_selection_display())

            elif initiated_by == "descriptions_shortcut":
                self.audio_file_display.clear()
                self.parameter_filter.blockSignals(True)
                QTimer.singleShot(0, lambda: self.parameter_filter.setStyleSheet(
                    GSS.recording_filter_boxes(red=True)))
                QTimer.singleShot(800, lambda: self.parameter_filter.setStyleSheet(
                    GSS.recording_filter_boxes(green=True)))
                QTimer.singleShot(1500, lambda: self.parameter_filter.setStyleSheet(
                    GSS.recording_filter_boxes()))
                QTimer.singleShot(1500, lambda: self.parameter_filter.blockSignals(False))

                QTimer.singleShot(800, lambda: update_audio_file_selection_display())

            else:
                update_audio_file_selection_display()

    def submenu_recordings_load_audio(self):
        if self.system_status.startswith("menu_recordings"):

            if self.audio_currently_playing:
                self.button_media_play_and_pause.setStyleSheet(GSS.button_media_play())

            self._wave_timer.stop()
            self.waveform.setPeaks([])
            self.waveform.setDuration(1)
            self.waveform.setPosition(0)

            self.media_player.stop()
            self.media_player.setPosition(0)

            name_of_selected_file = self.audio_file_display.currentItem().text()
            path_of_selected_file = self.audio_file_paths[self.audio_file_names.index(name_of_selected_file)]
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(path_of_selected_file)))
            self.media_player.durationChanged.connect(self.waveform.setDuration)

            # peaks = ADV.compute_peaks_wav_16bit(path_of_selected_file, target_points=max(300, self.waveform.width()))
            # self.waveform.setPeaks(peaks)

            if path_of_selected_file not in self._peaks_cache:
                target = max(300, self.waveform.width())
                self._peaks_cache[path_of_selected_file] = ADV.compute_peaks_wav_16bit(
                    path_of_selected_file, target_points=target)

            self.waveform.setPeaks(self._peaks_cache[path_of_selected_file])
            self.audio_played_completely_manually_before = False
            self.audio_loaded = True

    def submenu_recordings_play_and_pause_audio(self):

        if self.system_status.startswith("menu_recordings"):

            # play:
            if not self.audio_currently_playing and self.audio_filtered and self.audio_loaded:
                self.media_player.play()
                self.button_media_play_and_pause.setStyleSheet(GSS.button_media_pause())
                self.audio_played_completely_manually_before = True
                self.audio_currently_playing = True

            # pause:
            elif self.audio_currently_playing:
                self.media_player.pause()
                self.button_media_play_and_pause.setStyleSheet(GSS.button_media_play())
                self.audio_currently_playing = False

    def submenu_recordings_stop_audio(self, do_not_reset_audio_played_completely_var=False):
        if self.audio_currently_playing:
            self.media_player.stop()
            self.button_media_play_and_pause.setStyleSheet(GSS.button_media_play())
            self.audio_currently_playing = False

            if hasattr(self, "_wave_timer"):
                self._wave_timer.stop()

        self.waveform.setPosition(0)
        self.submenu_recordings_update_time_displays(0)

        self.media_player.setPosition(0)
        if not do_not_reset_audio_played_completely_var:
            self.audio_played_completely_manually_before = False

    def submenu_recordings_previous_audio(self):
        if self.system_status.startswith("menu_recordings"):

            self.submenu_recordings_stop_audio()

            if self.audio_filtered and self.audio_loaded and self.media_player.mediaStatus() != QMediaPlayer.NoMedia:
                if self.audio_file_display.currentRow() == 0:
                    self.audio_file_display.setCurrentRow(len(self.audio_file_names) - 1)
                else:
                    self.audio_file_display.setCurrentRow(self.audio_file_display.currentRow() - 1)

                self.submenu_recordings_load_audio()

    def submenu_recordings_next_audio(self):
        if self.system_status.startswith("menu_recordings"):

            self.submenu_recordings_stop_audio()

            if self.audio_filtered and self.audio_loaded and self.media_player.mediaStatus() != QMediaPlayer.NoMedia:
                if self.audio_file_display.currentRow() == len(self.audio_file_names) - 1:
                    self.audio_file_display.setCurrentRow(0)
                else:
                    self.audio_file_display.setCurrentRow(self.audio_file_display.currentRow() + 1)

                self.submenu_recordings_load_audio()

    def submenu_recordings_check_for_audio_replay(self):

        # end of file
        if self.media_player.mediaStatus() == 7:
            self.submenu_recordings_stop_audio(do_not_reset_audio_played_completely_var=True)

            if self.audio_replay:
                self.submenu_recordings_play_and_pause_audio()
                self.button_media_play_and_pause.setStyleSheet(GSS.button_media_pause())

    def submenu_recordings_replay_audio_ctrl(self, set_offline):
        if self.system_status.startswith("menu_recordings"):
            if set_offline:
                self.audio_replay = False
                self.button_media_replay.setStyleSheet(GSS.button_media_replay(locked=False))
            else:
                if self.audio_replay:
                    self.audio_replay = False
                    self.button_media_replay.setStyleSheet(GSS.button_media_replay(locked=False))
                else:
                    self.audio_replay = True
                    self.button_media_replay.setStyleSheet(GSS.button_media_replay(locked=True))

    def submenu_recordings_update_volume_display(self):
        if self.system_status.startswith("menu_recordings"):
            text = "Volume: " + str(self.slider_volume.value()) + "%"
            self.label_text_11.setText(text)

    def submenu_recordings_update_time_displays(self, pos_ms: int):
        pos_ms = max(0, pos_ms)
        dur_ms = max(0, self._duration_ms)

        self.label_text_12.setText(submenu_recordings_time_format_fmt_ms_mmssmmm(pos_ms))

        remaining = max(0, dur_ms - pos_ms)
        self.label_text_13.setText("-" + submenu_recordings_time_format_fmt_ms_mmssmmm(remaining))

    def submenus_settings(self, setting=0):
        if self.system_status.startswith("menu_settings"):
            pass

    def submenu_setting_restart(self):
        if self.system_status.startswith("menu_settings"):
            python = sys.executable
            args = sys.argv[:]
            os.execv(python, [python] + args)


app = QApplication(sys.argv)
gui = MainWindow()
gui.show()
sys.exit(app.exec_())

# ideas for settings:

# general GUI settings:
#                         color_theme:  dark / light (two GSS versions)
#                         languages:    en, de, it, es, fr, po (six GTM versions)

# copyright options:
#                       show copyright warning in home menu (checkbox)
#                       show copyright in headline (checkbox)

# media player:
#               remember filtered audio files (checkbox, will be questioned when calling recordings_menu)
#               remember media player settings (checkbox, will be questioned when calling recordings_menu)
#               audio_render_quality:      Debug: 1FPS (1000),
#                                          Eco: 10 FPS (100ms),
#                                          Normal: 30 FPS (33ms),
#                                          High: 60 FPS (16ms),
#                                          Ultra: 100 FPS (10ms)
