import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


class SimpleGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Farben definieren (RGB)
        background_color = QColor(30, 30, 60)  # dunkelblau
        text_color = QColor(255, 255, 255)     # weiß
        button_color = QColor(70, 130, 180)    # stahlblau

        # Farbpalette anwenden
        palette = QPalette()
        palette.setColor(QPalette.Window, background_color)
        palette.setColor(QPalette.WindowText, text_color)
        self.setPalette(palette)

        # Label
        self.label = QLabel("Hallo, PyQt5!", self)
        self.label.setStyleSheet(f"color: rgb({text_color.red()}, {text_color.green()}, {text_color.blue()});")
        self.label.setAlignment(Qt.AlignCenter)

        # Button
        self.button = QPushButton("Klick mich!", self)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: rgb(70, 130, 180);
                color: white;
                font-weight: bold;
                padding: 10px;
                border: 2px solid white;
                border-radius: 8px;
                }
            QPushButton:hover {
                background-color: rgb(100, 160, 210);
                border: 2px solid yellow;
                }
            QPushButton:pressed {
            background-color: rgb(40, 90, 140);
            border: 2px solid red;
            }

        """)
        self.button.clicked.connect(self.on_button_click)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Fenster-Eigenschaften
        self.setWindowTitle("Simple RGB GUI")
        self.resize(300, 150)

    def on_button_click(self):
        self.label.setText("Button wurde geklickt!")


# Main Application
app = QApplication(sys.argv)
gui = SimpleGUI()
gui.show()
sys.exit(app.exec_())
