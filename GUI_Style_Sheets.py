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


def label_main_headline_background():
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


def label_text_1():
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
# [Home, Description, Study, Training, Settings]
def button_main_nav_home(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: rgba(107,109,113,255);
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
                    background-color: rgba(107,109,113,255);
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


def button_main_nav_study(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: rgba(107,109,113,255);
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


def button_main_nav_training(pressed):
    if pressed:
        sst = """QPushButton {
                    background-color: rgba(107,109,113,255);
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_training_1.png) 
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
                    border-image: url(./src/gui/ico/main_nav_bar/button_main_nav_training_0.png) 
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
                    background-color: rgba(107,109,113,255);
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
