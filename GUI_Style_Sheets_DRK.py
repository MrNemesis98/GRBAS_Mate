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
from pathlib import Path


def resource_path(rel: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, rel)


def qss_path(rel: str) -> str:
    # -> C:/Users/.../button.png (ohne file:///)
    return Path(resource_path(rel)).resolve().as_posix()


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
        border-right: 3px solid rgba(12,14,17,255);
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


def label_text(dark_background=False, no_background=False, frame_only=False, top_module=False, settings=False):
    if settings:
        sst = """
            QLabel {
                color: rgb(220, 220, 220);
                background-color: transparent;
                font-size: 25px;
                border-radius: 20px;
                padding: 20px;
                border: 3px solid rgba(12, 14, 17, 255)
                }
            """
    elif dark_background:
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
    p0 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_info_0.png")
    p1 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_info_1.png")
    p2 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_info_2.png")

    if pressed:
        return f"""
            QPushButton {{
                border: none;
                border-image: url("{p2}") 0 0 0 0 stretch stretch;
            }}
            """
    else:
        return f"""
            QPushButton {{
                border: none;
                border-image: url("{p0}") 0 0 0 0 stretch stretch;
            }}
            QPushButton:hover {{
                border-image: url("{p1}") 0 0 0 0 stretch stretch;
            }}
            """


def button_main_ctrl_faq(pressed: bool) -> str:
    p0 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_faq_0.png")
    p1 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_faq_1.png")
    p2 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_faq_2.png")

    if pressed:
        return f"""
        QPushButton {{
            border: none;
            border-image: url("{p2}") 0 0 0 0 stretch stretch;
        }}
        """
    else:
        return f"""
        QPushButton {{
            border: none;
            border-image: url("{p0}") 0 0 0 0 stretch stretch;
        }}
        QPushButton:hover {{
            border-image: url("{p1}") 0 0 0 0 stretch stretch;
        }}
        """


def button_main_ctrl_minimize():
    p0 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_minimize_0.png")
    p1 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_minimize_1.png")

    return f"""
        QPushButton {{
            border: none;
            border-image: url("{p0}") 0 0 0 0 stretch stretch;
        }}
        QPushButton:hover {{
            border-image: url("{p1}") 0 0 0 0 stretch stretch;
        }}
        """


def button_main_ctrl_exit():
    p0 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_exit_0.png")
    p1 = qss_path("src/gui/ico/main_ctrl/button_main_ctrl_exit_1.png")

    return f"""
            QPushButton {{
                border: none;
                border-image: url("{p0}") 0 0 0 0 stretch stretch;
            }}
            QPushButton:hover {{
                border-image: url("{p1}") 0 0 0 0 stretch stretch;
            }}
            """


# Main Navigation Bar (5 Buttons) --------------------------------------------------------------------------------------
# [Home, Description, Recordings, Training, Settings]
def button_main_nav_home(pressed):
    p0 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_home_0.png")
    p1 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_home_1.png")

    if pressed:
        return f"""QPushButton {{
                    background-color: #FFFFFF;
                    border-image: url("{p1}") 0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }}"""
    else:
        return f"""
                QPushButton {{
                    background-color: rgba(25,30,36,255);
                    border-image: url("{p0}") 0 0 0 0 stretch stretch;
                    background-repeat: no-repeat;
                    background-position: center;
                    border: 2px solid rgba(25,30,36,255);
                    border-radius: 8px;
                }}
                QPushButton:hover {{
                    background-color: rgba(41,51,63,255);
                }}
            """


def button_main_nav_description(pressed):
    p0 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_description_0.png")
    p1 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_description_1.png")

    if pressed:
        return f"""QPushButton {{
                        background-color: #FFFFFF;
                        border-image: url("{p1}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}"""
    else:
        return f"""
                    QPushButton {{
                        background-color: rgba(25,30,36,255);
                        border-image: url("{p0}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}
                    QPushButton:hover {{
                        background-color: rgba(41,51,63,255);
                    }}
                """


def button_main_nav_recordings(pressed):
    p0 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_recordings_0.png")
    p1 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_recordings_1.png")

    if pressed:
        return f"""QPushButton {{
                        background-color: #FFFFFF;
                        border-image: url("{p1}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}"""
    else:
        return f"""
                    QPushButton {{
                        background-color: rgba(25,30,36,255);
                        border-image: url("{p0}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}
                    QPushButton:hover {{
                        background-color: rgba(41,51,63,255);
                    }}
                """


def button_main_nav_training(pressed):
    p0 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_study_0.png")
    p1 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_study_1.png")

    if pressed:
        return f"""QPushButton {{
                        background-color: #FFFFFF;
                        border-image: url("{p1}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}"""
    else:
        return f"""
                    QPushButton {{
                        background-color: rgba(25,30,36,255);
                        border-image: url("{p0}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}
                    QPushButton:hover {{
                        background-color: rgba(41,51,63,255);
                    }}
                """


def button_main_nav_settings(pressed):
    p0 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_settings_0.png")
    p1 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_settings_1.png")
    p2 = qss_path("src/gui/ico/main_nav_bar/button_main_nav_settings_2.png")

    if pressed:
        return f"""QPushButton {{
                        background-color: #FFFFFF;
                        border-image: url("{p2}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}"""
    else:
        return f"""
                    QPushButton {{
                        background-color: rgba(25,30,36,255);
                        border-image: url("{p0}") 0 0 0 0 stretch stretch;
                        background-repeat: no-repeat;
                        background-position: center;
                        border: 2px solid rgba(25,30,36,255);
                        border-radius: 8px;
                    }}
                    QPushButton:hover {{
                        background-color: rgba(41,51,63,255);
                        border-image: url("{p1}") 0 0 0 0 stretch stretch;
                    }}
                """


# Miscellaneous Buttons ------------------------------------------------------------------------------------------------
def button_switch_right(active, waiting=False):
    p0 = qss_path("src/gui/ico/miscellaneous/button_switch_right_0.png")
    p1 = qss_path("src/gui/ico/miscellaneous/button_switch_right_1.png")
    p2 = qss_path("src/gui/ico/miscellaneous/button_switch_right_2.png")
    p3 = qss_path("src/gui/ico/miscellaneous/button_switch_right_3.png")

    if waiting:
        return f"""QPushButton {{
                            border-image: url("{p3}") 0 0 0 0 stretch stretch;
                        }}"""
    elif not active:
        return f"""QPushButton {{
                    border-image: url("{p0}") 0 0 0 0 stretch stretch;
                }}"""
    else:
        return f"""QPushButton {{
                    border-image: url("{p1}") 0 0 0 0 stretch stretch;
                }}
                QPushButton:hover {{
                    border-image: url("{p2}") 0 0 0 0 stretch stretch;
                }}
            """


def button_switch_left(active, waiting=False):
    p0 = qss_path("src/gui/ico/miscellaneous/button_switch_left_0.png")
    p1 = qss_path("src/gui/ico/miscellaneous/button_switch_left_1.png")
    p2 = qss_path("src/gui/ico/miscellaneous/button_switch_left_2.png")
    p3 = qss_path("src/gui/ico/miscellaneous/button_switch_left_3.png")

    if waiting:
        return f"""QPushButton {{
                                border-image: url("{p3}") 0 0 0 0 stretch stretch;
                            }}"""
    elif not active:
        return f"""QPushButton {{
                        border-image: url("{p0}") 0 0 0 0 stretch stretch;
                    }}"""
    else:
        return f"""QPushButton {{
                        border-image: url("{p1}") 0 0 0 0 stretch stretch;
                    }}
                    QPushButton:hover {{
                        border-image: url("{p2}") 0 0 0 0 stretch stretch;
                    }}
                """


def button_switch_down(active, waiting=False, dress_as_recording=False):
    p0 = qss_path("src/gui/ico/miscellaneous/button_switch_down_0.png")
    p1 = qss_path("src/gui/ico/miscellaneous/button_switch_down_1.png")
    p2 = qss_path("src/gui/ico/miscellaneous/button_switch_down_2.png")
    p3 = qss_path("src/gui/ico/miscellaneous/button_switch_down_3.png")

    r0 = qss_path("src/gui/ico/miscellaneous/button_recordings_0.png")
    r1 = qss_path("src/gui/ico/miscellaneous/button_recordings_1.png")
    r2 = qss_path("src/gui/ico/miscellaneous/button_recordings_2.png")

    if not dress_as_recording:
        if waiting:
            return f"""QPushButton {{
                        border-image: url("{p3}") 0 0 0 0 stretch stretch;
                    }}"""
        elif not active:
            return f"""QPushButton {{
                        border-image: url("{p0}") 0 0 0 0 stretch stretch;
                    }}"""
        else:
            return f"""QPushButton {{
                        border-image: url("{p1}") 0 0 0 0 stretch stretch;
                    }}
                    QPushButton:hover {{
                        border-image: url("{p2}") 0 0 0 0 stretch stretch;
                    }}
                """
    else:
        if not active:
            return f"""QPushButton {{
                    background-color: #191E24;
                    border-radius: 35px;
                    border-image: url("{r0}") 0 0 0 0 stretch stretch;
                    }}"""
        else:
            return f"""QPushButton {{
                    background-color: #191E24;
                    border-radius: 35px;
                    border-image: url("{r1}") 0 0 0 0 stretch stretch;
                    }}
                    QPushButton:hover {{
                    background-color: #191E24;
                    border-radius: 35px;
                    border-image: url("{r2}") 0 0 0 0 stretch stretch;
                    }}"""


def button_switch_up(active, waiting=False):
    p0 = qss_path("src/gui/ico/miscellaneous/button_switch_up_0.png")
    p1 = qss_path("src/gui/ico/miscellaneous/button_switch_up_1.png")
    p2 = qss_path("src/gui/ico/miscellaneous/button_switch_up_2.png")
    p3 = qss_path("src/gui/ico/miscellaneous/button_switch_up_3.png")

    if waiting:
        return f"""QPushButton {{
                            border-image: url("{p3}") 0 0 0 0 stretch stretch;
                        }}"""
    elif not active:
        return f"""QPushButton {{
                            border-image: url("{p0}") 0 0 0 0 stretch stretch;
                        }}"""
    else:
        return f"""QPushButton {{
                            border-image: url("{p1}") 0 0 0 0 stretch stretch;
                        }}
                        QPushButton:hover {{
                            border-image: url("{p2}") 0 0 0 0 stretch stretch;
                        }}
                    """


def button_assistance_1(selected=False, settings=False):
    if settings:
        if selected:
            sst = f"""QPushButton {{
                            background: qlineargradient(
                                spread:pad, x1:1, y1:0, x2:1, y2:1,
                                stop:0   rgba(25,30,36,255), 
                                stop:0.85 rgba(25,30,36,255), 
                                stop:0.97  #0B839C,           
                                stop:1.0  #0B839C              
                                );
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 3px solid rgba(12,14,17,255);
                            }}"""
        else:
            sst = f"""QPushButton{{
                               background: qlineargradient(
                                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                                    stop:0   rgba(25,30,36,255),  
                                    stop:0.85 rgba(25,30,36,255),  
                                    stop:0.97  #0B839C,            
                                    stop:1.0  #0B839C         
                                    );
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: rgba(124,124,126,255);
                                border: 3px solid rgba(12,14,17,255);
                                }}
                    QPushButton:hover {{
                                    background: qlineargradient(
                                        spread:pad, x1:1, y1:0, x2:1, y2:1,
                                        stop:0   rgba(25,30,36,255),  
                                        stop:0.85 rgba(25,30,36,255), 
                                        stop:0.97  #0B839C            
                                        stop:1.0  #0B839C             
                                    );
                                    background-repeat: no-repeat;
                                    background-position: center;
                                    font-size: 25px;
                                    font-weight: bold;
                                    color: rgba(124,124,126,255);
                                    border: 3px solid rgba(12,14,17,255);
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


def button_assistance_2(selected=False, settings=False):
    if settings:
        if selected:
            sst = f"""QPushButton {{
                                background: qlineargradient(
                                    spread:pad, x1:1, y1:0, x2:1, y2:1,
                                    stop:0   rgba(25,30,36,255), 
                                    stop:0.85 rgba(25,30,36,255),  
                                    stop:0.97  #DB8004,            
                                    stop:1.0  #DB8004            
                                    );
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: #FFFFFF;
                                border: 3px solid rgba(12,14,17,255);
                                }}"""
        else:
            sst = f"""QPushButton{{
                               background: qlineargradient(
                                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                                    stop:0   rgba(25,30,36,255),  
                                    stop:0.85 rgba(25,30,36,255),  
                                    stop:0.97  #DB8004,            
                                    stop:1.0  #DB8004         
                                    );
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: rgba(124,124,126,255);
                                border: 3px solid rgba(12,14,17,255);
                                }}
                    QPushButton:hover {{
                                    background: qlineargradient(
                                        spread:pad, x1:1, y1:0, x2:1, y2:1,
                                        stop:0   rgba(25,30,36,255),  
                                        stop:0.85 rgba(25,30,36,255), 
                                        stop:0.97  #DB8004,            
                                        stop:1.0  #DB8004             
                                    );
                                    background-repeat: no-repeat;
                                    background-position: center;
                                    font-size: 25px;
                                    font-weight: bold;
                                    color: rgba(124,124,126,255);
                                    border: 3px solid rgba(12,14,17,255);
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


def button_assistance_3(selected=False, settings=False):
    if settings:
        if selected:
            sst = f"""QPushButton {{
                            background: qlineargradient(
                                spread:pad, x1:1, y1:0, x2:1, y2:1,
                                stop:0   rgba(25,30,36,255),   
                                stop:0.85 rgba(25,30,36,255),  
                                stop:0.97  #7030A0,             
                                stop:1.0  #7030A0             
                                );
                            background-repeat: no-repeat;
                            background-position: center;
                            font-size: 25px;
                            font-weight: bold;
                            color: #FFFFFF;
                            border: 3px solid rgba(12,14,17,255);
                            }}"""
        else:
            sst = f"""QPushButton{{
                               background: qlineargradient(
                                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                                    stop:0   rgba(25,30,36,255),  
                                    stop:0.85 rgba(25,30,36,255),  
                                    stop:0.97  #7030A0,            
                                    stop:1.0  #7030A0         
                                    );
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: rgba(124,124,126,255);
                                border: 3px solid rgba(12,14,17,255);
                                }}
                    QPushButton:hover {{
                                    background: qlineargradient(
                                        spread:pad, x1:1, y1:0, x2:1, y2:1,
                                        stop:0   rgba(25,30,36,255),  
                                        stop:0.85 rgba(25,30,36,255), 
                                        stop:0.97  #7030A0,            
                                        stop:1.0  #7030A0             
                                    );
                                    background-repeat: no-repeat;
                                    background-position: center;
                                    font-size: 25px;
                                    font-weight: bold;
                                    color: rgba(124,124,126,255);
                                    border: 3px solid rgba(12,14,17,255);
                                    }}"""
    else:
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


def button_assistance_4(deactivated=False, settings=False):
    if settings:
        if deactivated:
            sst = f"""QPushButton{{
                       background: qlineargradient(
                            spread:pad, x1:0, y1:0, x2:1, y2:1,
                            stop:0   rgba(25,30,36,255),  
                            stop:0.85 rgba(25,30,36,255),  
                            stop:0.97  rgba(41,51,63,255),            
                            stop:1.0  rgba(41,51,63,255)         
                            );
                        background-repeat: no-repeat;
                        background-position: center;
                        font-size: 25px;
                        font-weight: bold;
                        color: rgba(124,124,126,255);
                        border: 3px solid rgba(12,14,17,255);
                        }}"""
        else:
            sst = f"""QPushButton{{
                               background: qlineargradient(
                                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                                    stop:0   rgba(25,30,36,255),  
                                    stop:0.85 rgba(25,30,36,255),  
                                    stop:0.97  #8B0000,            
                                    stop:1.0  #8B0000         
                                    );
                                background-repeat: no-repeat;
                                background-position: center;
                                font-size: 25px;
                                font-weight: bold;
                                color: rgba(124,124,126,255);
                                border: 3px solid rgba(12,14,17,255);
                                }}
                    QPushButton:hover {{
                                    background: qlineargradient(
                                        spread:pad, x1:1, y1:0, x2:1, y2:1,
                                        stop:0   rgba(25,30,36,255),  
                                        stop:0.85 rgba(25,30,36,255), 
                                        stop:0.97  #8B0000,            
                                        stop:1.0  #8B0000             
                                    );
                                    background-repeat: no-repeat;
                                    background-position: center;
                                    font-size: 25px;
                                    font-weight: bold;
                                    color: #8B0000;
                                    border: 3px solid rgba(12,14,17,255);
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
                border-image: url(./src/gui/ico/media/button_media_play_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_play_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_play_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_pause():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_pause_2.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_pause_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_pause_0.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_stop():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_stop_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_stop_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_stop_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_previous():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_previous_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_previous_0.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:pressed {
                border-image: url(./src/gui/ico/media/button_media_previous_2.png) 0 0 0 0 stretch stretch;
            }
        """
    return sst


def button_media_next():
    sst = """QPushButton {
                border-image: url(./src/gui/ico/media/button_media_next_1.png) 0 0 0 0 stretch stretch;
            }
            QPushButton:hover {
                border-image: url(./src/gui/ico/media/button_media_next_0.png) 0 0 0 0 stretch stretch;
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
                """
    else:
        sst = """QPushButton {
                    border-image: url(./src/gui/ico/media/button_media_replay_1.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:hover {
                    border-image: url(./src/gui/ico/media/button_media_replay_0.png) 0 0 0 0 stretch stretch;
                }
                QPushButton:pressed {
                    border-image: url(./src/gui/ico/media/button_media_replay_3.png) 0 0 0 0 stretch stretch;
                }
            """
    return sst


def volume_slider():
    sst = """QSlider::groove:horizontal {
            height: 8px;
            background: #191E24;
            border-radius: 3px;
        }
        
        QSlider::handle:horizontal {
            width: 14px;
            margin: -4px 0;
            border-radius: 7px;
            background: #DB8004;
        }
        
        QSlider::sub-page:horizontal {
            background: #0B839C;
            border-radius: 3px;
        }
        
        QSlider::add-page:horizontal {
            background: #191E24;
            border-radius: 3px;
        }
        """
    return sst


def label_text_time_display_layout():
    sst = """
        QLabel {
            color: #DB8004;
            font-size: 22px;
            }
        """
    return sst


def label_settings_zero():
    sst = """
            QLabel {
                background-color: transparent;
                border-left: 5px solid rgba(12,14,17,255);
                border-bottom: 5px solid rgba(12,14,17,255);
            }"""
    return sst


def label_settings_frame_top(highlight_for_setting=0):
    if highlight_for_setting == 1:
        sst = """
            QLabel {
                background-color: transparent;
                border-left: 5px solid #0B839C;
                border-top: 5px solid #0B839C;
            }"""
    elif highlight_for_setting == 2:
        sst = """
            QLabel {
                background-color: transparent;
                border-left: 5px solid #DB8004;
                border-top: 5px solid #DB8004;
            }"""
    elif highlight_for_setting == 3:
        sst = """
            QLabel {
                background-color: transparent;
                border-left: 5px solid #7030A0;
                border-top: 5px solid #7030A0;
            }"""
    else:
        sst = """
            QLabel {
                background-color: transparent;
                border-left: 5px solid rgba(12,14,17,255);
                border-top: 5px solid rgba(12,14,17,255);
            }"""
    return sst


def label_settings_frame_bottom(highlight_for_setting=0):
    if highlight_for_setting == 1:
        sst = """
            QLabel {
                background-color: transparent;
                border-right: 5px solid #0B839C;
                border-bottom: 5px solid #0B839C;
            }"""
    elif highlight_for_setting == 2:
        sst = """
            QLabel {
                background-color: transparent;
                border-right: 5px solid #DB8004;
                border-bottom: 5px solid #DB8004;
            }"""
    elif highlight_for_setting == 3:
        sst = """
            QLabel {
                background-color: transparent;
                border-right: 5px solid #7030A0;
                border-bottom: 5px solid #7030A0;
            }"""
    else:
        sst = """
            QLabel {
                background-color: transparent;
                border-right: 5px solid rgba(12,14,17,255);
                border-bottom: 5px solid rgba(12,14,17,255);
            }"""
    return sst


def language_and_colour_choice():
    sst = """   
             QComboBox {
                background-color:  #191E24;
                color: #f0f0f0;   
                border: 3px solid #0B839C;
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
            }
        """
    return sst


def checkboxes_copyright():
    return """
    QCheckBox {
        color: #E0E0E0;
        spacing: 8px;
        font-size: 13px;
    }
    QCheckBox::indicator {
        width: 16px;
        height: 16px;
        border-radius: 4px;
        border: 1px solid #666;
        background: #1e1e1e;
    }
    QCheckBox::indicator:checked {
        background: #43A047;
        border: 1px solid #66BB6A;
    }
    QCheckBox::indicator:unchecked {
        background: #141414;
    }
    QCheckBox::indicator:hover {
        border: 1px solid #FFFFFF;
    }
    """