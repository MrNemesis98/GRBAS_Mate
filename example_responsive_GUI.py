import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ResponsiveGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.button = None
        self.label = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Responsive PyQt5 GUI")
        self.showFullScreen()  # Start im Vollbildmodus

        # ----- LABEL -----
        self.label = QLabel("Willkommen!", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # ----- BUTTON -----
        self.button = QPushButton("Beenden", self)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button.clicked.connect(self.close)  # Fenster schließen

        # ----- LAYOUT -----
        layout = QVBoxLayout()
        layout.addStretch()              # Platz oben
        layout.addWidget(self.label)
        layout.addSpacing(20)            # Abstand zwischen Label und Button
        layout.addWidget(self.button)
        layout.addStretch()              # Platz unten

        self.setLayout(layout)

        # Erste Schriftgröße setzen
        self.update_fonts()

    def resizeEvent(self, event):
        if self.label is not None and self.button is not None:
            self.update_fonts()
        super().resizeEvent(event)

    def update_fonts(self):
        # Schriftgrößen relativ zur Fenstergröße berechnen
        w = self.width()
        label_font_size = max(w // 20, 12)
        button_font_size = max(w // 30, 10)

        self.label.setFont(QFont("Arial", label_font_size))
        self.button.setFont(QFont("Arial", button_font_size))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.showNormal()  # Vollbild verlassen


# ---- App starten ----
app = QApplication(sys.argv)
window = ResponsiveGUI()
window.show()
sys.exit(app.exec_())
