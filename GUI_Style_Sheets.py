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

"""🧱
1. solid bei border ----------------------------------------------------------------------------------------------------

border: 2px solid rgb(180, 180, 180);
→ solid ist der Linientyp der Umrandung:

Wert	Bedeutung
solid	durchgehende Linie
dashed	gestrichelte Linie
dotted	gepunktete Linie
double	doppelte Linie
none keine Linie

2. border-radius

border-radius: 8px;
→ border-radius steuert die Abrundung der Ecken.

Wert	Wirkung
0px	ganz eckig (kein Radius)
5px	leicht gerundet
50 %	komplett rund (Kreis bei Quadrat)
64px z.B.	maximale Rundung bei 64×64-Button

➡️ Es gibt keine harte Obergrenze, aber:

Wenn border-radius >= min(width, height)/2, dann wird das Objekt kreisförmig.

Bei Buttons mit 64x64 wäre 32px der Maximalwert, um einen Kreis zu erzeugen.
"""


def label_main_background():
    sst = """
    QLabel {
        color: rgb(30, 30, 30);
        background-color: rgba(33,39,47,255);
        background: qlineargradient(
            spread:pad, x1:0, y1:0, x2:5.5, y2:5.5,
            stop:0 rgba(33,39,47,255),  
            stop:1 rgba(25,30,36,255)
            );
        border-top-left-radius: 80px;
        }
    """
    return sst


def label_main_headline_background(highlight=False):
    if highlight:
        sst = """
            QLabel {
                color: rgba(244,244,246,255);
                font-size: 20px;
                font-weight: bold;
                background: qlineargradient(
                    spread:pad, x1:1, y1:0, x2:1, y2:1,
                    stop:0 rgba(10,37,54,255),  
                    stop:1 rgba(25,30,36,255)
                    );
                border-bottom: 2px solid rgb(64,72,82);
                border-top-left-radius: 80px;
                padding: 8px;
            }
            """
    else:
        sst = """
        QLabel {
            color: rgba(124,124,126,255);
            font-size: 20px;
            font-weight: bold;
            background: qlineargradient(
                spread:pad, x1:1, y1:0, x2:1, y2:1,
                stop:0 rgba(10,37,54,255),  
                stop:1 rgba(25,30,36,255)
                );
            border-bottom: 2px solid rgb(64,72,82);
            border-top-left-radius: 80px;
            padding: 8px;
        }
        """
    return sst


def label_main_nav_bar_background():
    sst = """
    QLabel {
        background-color: rgba(25,30,36,255);
        border-right: 2px solid rgba(12,14,17,255);
        }
    """
    return sst


def label_menu_title(main_ctrl):
    if main_ctrl:
        sst = """
            QLabel {
                color: rgb(11, 131, 156);
                background-color: rgba(33,39,47,255);
                font-size: 35px;
                font-weight: bold;
                }
            """
    else:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                background-color: rgba(33,39,47,255);
                font-size: 35px;
                font-weight: bold;
                }
            """
    return sst


def label_text(dark_background=False, no_background=False, frame_only=False, top_module=False):
    if dark_background:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                background-color: rgba(25,30,36,255);
                font-size: 25px;
                border-radius: 20px;
                padding: 20px;
                }
            """
    elif no_background:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                font-size: 22px;
                }
            """
    elif frame_only:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                font-size: 25px;
                border: 4px solid rgba(41,51,63,255);
                border-radius: 20px;
                padding: 20px;
                }
            """
    elif top_module:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                background-color: rgba(25,30,36,255);
                font-size: 25px;
                border-top-left-radius: 50px;
                border-top-right-radius: 50px;
                padding: 5px;
                }
            """
    else:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                background-color: rgba(41,51,63,255);
                font-size: 25px;
                border-radius: 20px;
                padding: 20px;
                }
            """
    return sst


# Main GUI Controls (4 Buttons) ----------------------------------------------------------------------------------------
# [Info, FAQ, Minimize, Exit]
def button_main_ctrl_info(pressed):
    if pressed:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_info_2.png) 0 0 0 0 stretch stretch;
                }"""
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_info_0.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_info_1.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst


def button_main_ctrl_faq(pressed):
    if pressed:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_faq_2.png) 0 0 0 0 stretch stretch;
                }"""
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_faq_0.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_faq_1.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst


def button_main_ctrl_minimize():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_minimize_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_minimize_1.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_main_ctrl_exit():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_exit_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/main_ctrl/button_main_ctrl_exit_1.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


# Main Navigation Bar (5 Buttons) --------------------------------------------------------------------------------------
# [Home, Description, Recordings, Training, Settings]
def button_main_nav_home(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: #FFFFFF;
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_home_1.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }"""
    else:
        sst = """
                QPushButton {
                    background-color: rgba(25,30,36,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_home_0.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(41,51,63,255);
                }
            """
    return sst


def button_main_nav_description(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: #FFFFFF;
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_description_1.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }"""
    else:
        sst = """
                QPushButton {
                    background-color: rgba(25,30,36,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_description_0.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(41,51,63,255);
                }
            """
    return sst


def button_main_nav_recordings(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: #FFFFFF;
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_recordings_1.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }"""
    else:
        sst = """
                QPushButton {
                    background-color: rgba(25,30,36,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_recordings_0.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(41,51,63,255);
                }
            """
    return sst


def button_main_nav_training(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: #FFFFFF;
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_study_1.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }"""
    else:
        sst = """
                QPushButton {
                    background-color: rgba(25,30,36,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_study_0.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(41,51,63,255);
                }
            """
    return sst


def button_main_nav_settings(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: #FFFFFF;
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_settings_2.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }"""
    else:
        sst = """
                QPushButton {
                    background-color: rgba(25,30,36,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_settings_0.png) 
                    0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(41,51,63,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_settings_1.png) 
                    0 0 0 0 stretch stretch;
                }
            """
    return sst


# Miscellaneous Buttons ------------------------------------------------------------------------------------------------
def button_switch_right(active, waiting=False):
    if waiting:
        sst = """QPushButton {
                            border-image: url(./src/gui/ico/miscellaneous/button_switch_right_3.png) 
                            0 0 0 0 stretch stretch;
                        }"""
    elif not active:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_right_0.png) 0 0 0 0 stretch stretch;
                }"""
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_right_1.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_right_2.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst


def button_switch_left(active, waiting=False):
    if waiting:
        sst = """QPushButton {
                            border-image: url(./src/gui/ico/miscellaneous/button_switch_left_3.png) 
                            0 0 0 0 stretch stretch;
                        }"""
    elif not active:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_left_0.png) 0 0 0 0 stretch stretch;
                }"""
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_left_1.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_left_2.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst


def button_switch_down(active, waiting=False, dress_as_recording=False):
    if not dress_as_recording:
        if waiting:
            sst = """QPushButton {
                                border-image: url(./src/gui/ico/miscellaneous/button_switch_down_3.png) 
                                0 0 0 0 stretch stretch;
                            }"""
        elif not active:
            sst = """QPushButton {
                        border-image: url(./src/gui/ico/miscellaneous/button_switch_down_0.png) 0 0 0 0 stretch stretch;
                    }"""
        else:
            sst = """QPushButton {
                        border-image: url(./src/gui/ico/miscellaneous/button_switch_down_1.png) 0 0 0 0 stretch stretch;
                    }
                    QPushButton:hover {
                        border-image: url(./src/gui/ico/miscellaneous/button_switch_down_2.png) 0 0 0 0 stretch stretch;
                    }
                """
    else:
        if not active:
            sst = """QPushButton {
                    background-color: #191E24;
                    border-radius: 35px;
                    border-image: url(./src/gui/ico/miscellaneous/button_recordings_0.png) -5 -5 -5 -5 stretch stretch;
                    }"""
        else:
            sst = """QPushButton {
                    background-color: #191E24;
                    border-radius: 35px;
                    border-image: url(./src/gui/ico/miscellaneous/button_recordings_1.png) -5 -5 -5 -5 stretch stretch;
                    }
                    QPushButton:hover {
                    background-color: #191E24;
                    border-radius: 35px;
                    border-image: url(./src/gui/ico/miscellaneous/button_recordings_2.png) -5 -5 -5 -5 stretch stretch;
                    }"""
    return sst


def button_switch_up(active, waiting=False):
    if waiting:
        sst = """QPushButton {
                            border-image: url(./src/gui/ico/miscellaneous/button_switch_up_3.png) 
                            0 0 0 0 stretch stretch;
                        }"""
    elif not active:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_up_0.png) 0 0 0 0 stretch stretch;
                }"""
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_up_1.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/miscellaneous/button_switch_up_2.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst


def button_assistance_1(selected):
    if selected:
        sst = f"""QPushButton {{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #0B839C;
                            border: 0px;
                            border-bottom-left-radius: 35px;
                            border-top-left-radius: 35px;
                            }}"""
    else:
        sst = f"""QPushButton{{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 0px;
                            border-bottom-left-radius: 35px;
                            border-top-left-radius: 35px;
                            }}
                    QPushButton:hover {{
                    background-color: #191E24;
                    background-repeat: no-repeat;
                    background-position: center;
                    font-size: 25px;
                    font-weight: bold;
                    color: #0B839C;
                    border: 0px;
                    border-bottom-left-radius: 35px;
                    border-top-left-radius: 35px;
                    }}"""
    return sst


def button_assistance_2(selected):
    if selected:
        sst = f"""QPushButton {{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #0B839C;
                            border: 0px;
                            }}"""
    else:
        sst = f"""QPushButton{{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 0px;
                            }}
                    QPushButton:hover {{
                    background-color: #191E24;
                    background-repeat: no-repeat;
                    background-position: center;
                    font-size: 25px;
                    font-weight: bold;
                    color: #0B839C;
                    border: 0px;
                    }}"""
    return sst


def button_assistance_3(selected):
    if selected:
        sst = f"""QPushButton {{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #DB8004;
                            border: 0px;
                            border-bottom-right-radius: 35px;
                            border-top-right-radius: 35px;
                            }}"""
    else:
        sst = f"""QPushButton{{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 0px;
                            border-bottom-right-radius: 35px;
                            border-top-right-radius: 35px;
                            }}
                    QPushButton:hover {{
                    background-color: #191E24;
                    background-repeat: no-repeat;
                    background-position: center;
                    font-size: 25px;
                    font-weight: bold;
                    color: #DB8004;
                    border: 0px;
                    border-bottom-right-radius: 35px;
                    border-top-right-radius: 35px;
                    }}"""
    return sst


# Buttons for Parameters -----------------------------------------------------------------------------------------------

def button_param_start(selected=False):

    if selected:
        sst = f"""QPushButton {{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #0B839C;
                                border: 0px;
                                border-top-left-radius: 35px;
                                border-top-right-radius: 35px;
                                border-bottom-left-radius: 35px;
                                border-bottom-right-radius: 35px;
                            }}"""
    else:
        sst = f"""QPushButton{{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 0px;
                            border-top-left-radius: 35px;
                            border-top-right-radius: 35px;
                            border-bottom-left-radius: 35px;
                            border-bottom-right-radius: 35px;
                        }}
                QPushButton:hover {{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #0B839C;
                            border: 0px;
                            border-top-left-radius: 35px;
                            border-top-right-radius: 35px;
                            border-bottom-left-radius: 35px;
                            border-bottom-right-radius: 35px;
                }}"""

    return sst


def button_param_I(selected=False):

    if selected:
        sst = f"""QPushButton {{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #7030A0;
                                border: 0px;
                                border-top-left-radius: 35px;
                                border-bottom-left-radius: 35px;
                            }}"""
    else:
        sst = f"""QPushButton{{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 0px;
                            border-top-left-radius: 35px;
                            border-bottom-left-radius: 35px;
                        }}
                QPushButton:hover {{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #7030A0;
                            border: 0px;
                            border-top-left-radius: 35px;
                            border-bottom-left-radius: 35px;
                }}"""

    return sst


def buttons_param_F_to_A(part_of_scale_extension=False, selected=False):

    if part_of_scale_extension:
        if selected:
            sst = f"""QPushButton {{
                                    background-color: #191E24;
                                    background-repeat: no-repeat;
                                    background-position: center;
                                    font-size: 25px;
                                    font-weight: bold;
                                    color: #7030A0;
                                    border: 0px;
                                }}"""
        else:
            sst = f"""QPushButton{{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #FFFFFF;
                                border: 0px;
                            }}
                    QPushButton:hover {{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #7030A0;
                                border: 0px;
                    }}"""

    else:
        if selected:
            sst = f"""QPushButton {{
                                    background-color: #191E24;
                                    background-repeat: no-repeat;
                                    background-position: center;
                                    font-size: 25px;
                                    font-weight: bold;
                                    color: #0B839C;
                                    border: 0px;
                                }}"""
        else:
            sst = f"""QPushButton{{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #FFFFFF;
                                border: 0px;
                            }}
                    QPushButton:hover {{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #0B839C;
                                border: 0px;
                    }}"""

    return sst


def button_param_S(selected=False):

    if selected:
        sst = f"""QPushButton {{
                                background-color: #191E24;
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #0B839C;
                                border: 0px;
                                border-top-right-radius: 35px;
                                border-bottom-right-radius: 35px;
                            }}"""
    else:
        sst = f"""QPushButton{{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 0px;
                            border-top-right-radius: 35px;
                            border-bottom-right-radius: 35px;
                        }}
                QPushButton:hover {{
                            background-color: #191E24;
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #0B839C;
                            border: 0px;
                            border-top-right-radius: 35px;
                            border-bottom-right-radius: 35px;
                }}"""

    return sst


# QComboBoxes (Recording Filters) --------------------------------------------------------------------------------------
def recording_filter_boxes(red=False, green=False):
    sst = """   
             QComboBox {
                background-color:  #191E24;
                color: #f0f0f0;
                border: 3px solid rgba(41,51,63,255);
                border-radius: 200px;
                padding: 3px 5px;
            }
            /* Dropdown-Bereich rechts (mit Pfeil) */
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 0px;                  
                background-color: #191E24;
            }
            QComboBox QAbstractItemView {
                background-color: #191E24;
                color: #ffffff;
                selection-background-color: rgba(41,51,63,255);
                selection-color: #0B839C;
                border-bottom-left-radius: 8px;
                border-bottom-right-radius: 8px;
            }
        """
    if red:
        sst = """   
                     QComboBox {
                        background-color:  #191E24;
                        color: #DC143C;
                        border: 3px solid rgba(41,51,63,255);
                        border-radius: 200px;
                        padding: 3px 5px;
                    }
                    /* Dropdown-Bereich rechts (mit Pfeil) */
                    QComboBox::drop-down {
                        subcontrol-origin: padding;
                        subcontrol-position: top right;
                        width: 0px;                  
                        background-color: #191E24;
                    }
                    QComboBox QAbstractItemView {
                        background-color: #191E24;
                        color: #ffffff;
                        padding: 8px;
                        selection-background-color: rgba(41,51,63,255);
                        selection-color: #0B839C;
                        border-bottom-left-radius: 8px;
                        border-bottom-right-radius: 8px;
                        text-align:left;
                    }
                """
    elif green:
        sst = """   
                     QComboBox {
                        background-color:  #191E24;
                        color: #228B22;
                        border: 3px solid rgba(41,51,63,255);
                        border-radius: 200px;
                        padding: 3px 5px;
                    }
                    /* Dropdown-Bereich rechts (mit Pfeil) */
                    QComboBox::drop-down {
                        subcontrol-origin: padding;
                        subcontrol-position: top right;
                        width: 0px;                  
                        background-color: #191E24;
                    }
                    QComboBox QAbstractItemView {
                        background-color: #191E24;
                        color: #ffffff;
                        padding: 8px;
                        selection-background-color: rgba(41,51,63,255);
                        selection-color: #0B839C;
                        border-bottom-left-radius: 8px;
                        border-bottom-right-radius: 8px;
                        text-align:left;
                    }
                """
    return sst


# Audio_File_display (QListWidget) -------------------------------------------------------------------------------------
def audio_file_display():
    sst = """
        QListWidget {
            background: #191E24;
            border: 1px solid #191E24;
            border-radius: 20px;
            padding: 4px;
        }
        
        QListWidget::item {
            color: #ffffff;
            padding: 6px 10px;
            border-radius: 4px;
        }
        
        /* Hover-Effekt */
        QListWidget::item:hover {
            background: rgba(41,51,63,255);
        }
        
        /* Aktuell ausgewähltes Item */
        QListWidget::item:selected {
            background: rgba(41,51,63,255);
            color: #0B839C;
            font-weight: bold;
            border: none;
        }
        
        /* Fokusrahmen entfernen (optional) */
        QListWidget:focus {
            outline: none;
        }
        """
    return sst


def waveform():
    return """
    WaveformWidget {
        background-color: #191E24;
        border: 4px solid rgba(41,51,63,255);

        qproperty-playedColor: #0B839C;
        qproperty-unplayedColor: rgba(41,51,63,255);
        qproperty-playheadColor: #DB8004;
    }
    """


# Media Buttons --------------------------------------------------------------------------------------------------------

def button_media_play():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_play_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_play_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_play_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_pause():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_pause_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_pause_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_pause_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_stop():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_stop_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_stop_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_stop_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_previous():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_previous_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_previous_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_previous_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_next():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_next_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_next_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_next_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_replay(locked=False):
    if locked:
        sst = """QPushButton {
                        border-image: url(./src/gui/ico/media/button_media_replay_3.png) 0 0 0 0 stretch stretch;
                    }
                    QPushButton:hover {
                        border-image: url(./src/gui/ico/media/button_media_replay_1.png) 0 0 0 0 stretch stretch;
                    }
                """
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/media/button_media_replay_0.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/media/button_media_replay_1.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:pressed {
                    border-image: url(./src/gui/ico/media/button_media_replay_3.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst