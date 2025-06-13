"""
Minimal‑Beispiel einer GRBAS‑Notiz‑GUI
======================================

getestet mit Python 3.11 + PyQt5

pip install PyQt5
"""

import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)

PARAM_WIDTH = 120          # Zielbreite des ausgefahrenen Parameter‑Bereichs (px)
ANIM_DURATION = 250        # Animationsdauer (ms)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GRBAS‑Note")
        self.resize(850, 500)

        # ---------- Zentrales Widget + Haupt‑Layouts ----------
        central = QWidget()
        self.setCentralWidget(central)

        main_hbox = QHBoxLayout(central)         # links Leiste, rechts Inhalt
        main_hbox.setContentsMargins(0, 0, 0, 0)
        main_hbox.setSpacing(0)

        # ---------- linke Navigation ----------
        nav_widget = QWidget()
        nav_widget.setFixedWidth(120)
        nav_vbox = QVBoxLayout(nav_widget)
        nav_vbox.setContentsMargins(0, 0, 0, 0)
        nav_vbox.setSpacing(0)

        # vier Haupt‑Buttons
        self.btn_home    = self.nav_button("Home",    nav_vbox)
        self.btn_grbas   = self.nav_button("GRBAS",   nav_vbox, self.toggle_parameters)
        self.btn_audio   = self.nav_button("Audio",   nav_vbox)
        nav_vbox.addStretch(1)                       # Flex‑Platz
        self.btn_settings = self.nav_button("Settings", nav_vbox)
        main_hbox.addWidget(nav_widget)

        # ---------- Parameter‑Container (standardmäßig eingefahren) ----------
        self.param_container = QWidget()
        self.param_container.setMaximumWidth(0)      # startet „zugeklappt“
        self.param_container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        param_vbox = QVBoxLayout(self.param_container)
        param_vbox.setContentsMargins(4, 4, 4, 4)
        param_vbox.setSpacing(4)

        for label in ("I", "G", "R", "B", "A", "S", "✓"):
            btn = QPushButton(label)
            btn.setFixedHeight(36)
            btn.setCursor(Qt.PointingHandCursor)
            param_vbox.addWidget(btn)

        main_hbox.addWidget(self.param_container)

        # ---------- Platzhalter für den Restinhalt ----------
        placeholder = QLabel(" … hier könnte später Ihre Diagnostik‑Ansicht stehen …")
        placeholder.setAlignment(Qt.AlignCenter)
        main_hbox.addWidget(placeholder, 1)

        # ---------- Animation vorbereiten ----------
        self.anim = QPropertyAnimation(self.param_container, b"maximumWidth", self)
        self.anim.setDuration(ANIM_DURATION)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)

        # simples Styling
        self.setStyleSheet("""
            QPushButton {
                border: none;
                padding: 8px;
                text-align: left;
            }
            QPushButton:hover {
                background: #dddddd;
            }
            /* Parameter‑Buttons */
            QWidget QPushButton {
                text-align: center;
                border-radius: 4px;
                background: #f1f1f1;
            }
        """)

    # ---------------------------------------------------------
    # Hilfs‑Methoden
    # ---------------------------------------------------------
    @staticmethod
    def nav_button(text, layout, slot=None):
        btn = QPushButton(text)
        btn.setFixedHeight(44)
        btn.setCursor(Qt.PointingHandCursor)
        if slot:
            btn.clicked.connect(slot)
        layout.addWidget(btn)
        return btn

    def toggle_parameters(self):
        """Parameter‑Bereich ein‑/ausblenden mit Slide‑Animation."""
        collapsed = self.param_container.maximumWidth() == 0
        start_w = 0 if collapsed else PARAM_WIDTH
        end_w   = PARAM_WIDTH if collapsed else 0

        self.anim.stop()
        self.anim.setStartValue(start_w)
        self.anim.setEndValue(end_w)
        self.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
