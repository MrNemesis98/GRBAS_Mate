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
        background-color: rgb(30, 30, 30);
        font-size: 18px;
        font-weight: bold;
        border: 2px solid rgb(45, 45, 45);
        border-top-left-radius: 100px;
        padding: 8px;
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
                background-color: rgb(30, 30, 30);
                border: 2px solid rgb(30, 30, 30);
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgb(30, 30, 30);
                border: 2px solid rgb(30, 30, 30);
            }
            QPushButton:pressed {
                background-color: rgb(30, 30, 30);
                border: 2px solid rgb(30self.button.setIconSize(self.button.size()), 30, 30);
            }
        """
    return sst
