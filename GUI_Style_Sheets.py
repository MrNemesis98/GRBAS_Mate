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
        font-size: 18px;
        font-weight: bold;
        border-top-left-radius: 100px;
        padding: 8px;
        }
    """
    return sst


def label_main_headline_background():
    sst = """
    QLabel {
        color: rgba(244,244,246,255);
        font-size: 30px;
        font-weight: bold;
        background-color: rgba(15,16,40,255);
        border-bottom: 2px solid rgb(64,72,82);
        border-top-left-radius: 100px;
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


def button_main_ctrl_exit():
    sst = """
            QPushButton {
                background-color: rgb(70, 130, 180);
                border: 2px solid rgb(90, 90, 90);
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgb(100, 160, 210);
                border: 2px solid rgb(90, 90, 90);
            }
            QPushButton:pressed {
                background-color: rgb(50, 110, 160);
                border: 2px solid rgb(90, 90, 90);
            }
        """
    return sst


def buttons_main_nav():
    sst = """
            QPushButton {
                background-color: rgba(25,30,36,255);
                border: 2px solid rgba(25,30,36,255);
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgba(41,51,63,255);
                border: 2px solid rgba(41,51,63,255);
            }
            QPushButton:pressed {
                background-color: rgba(25,30,36,255);
                border: 2px solid rgba(25,30,36,255);
            }
        """
    return sst


def button_main_nav_settings():
    sst = """
            QPushButton {
                background-color: rgba(25,30,36,255);
                border: 2px solid rgba(25,30,36,255);
                border-radius: 8px;
                background-image: url(./src/gui/ico/button_main_nav_settings_1.png);
                background-repeat: no-repeat;
                background-position: center;
                
            }
            QPushButton:hover {
                background-color: rgba(41,51,63,255);
                border: 2px solid rgba(41,51,63,255);
                background-image: url(./src/gui/ico/button_main_nav_settings_2.png);
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:pressed {
                background-color: rgba(25,30,36,255);
                border: 2px solid rgba(25,30,36,255);
                background-image: url(./src/gui/ico/button_main_nav_settings_2.png);
                background-repeat: no-repeat;
                background-position: center;
            }
        """
    return sst
