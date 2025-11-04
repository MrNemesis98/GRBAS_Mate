"""
Copyright © MrNemesis98, GitHub, 2025

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
"""
from fractions import Fraction

from wuggy import WuggyGenerator


g = WuggyGenerator()
g.load("orthographic_english")
for match in g.generate_classic(
    ["Klo", "Bürste"],
    ncandidates_per_sequence=30, max_search_time_per_sequence=2):
    print(match["pseudoword"])
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox
from PyQt5.QtGui import QFont

class StyledComboDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled QComboBox")

        combo = QComboBox()
        combo.addItems(["None", "G", "R", "B", "A", "S", "I", "F"])

        # Schrift über QFont
        combo.setFont(QFont("Noto Sans", 12))

        # Farben und Rahmen über QSS
        combo.setStyleSheet("""
            QComboBox {
                background-color: #2b2b2b;
                color: #f0f0f0;
                border: 2px solid #3c3c3c;
                border-radius: 8px;
                padding: 5px 10px;
                selection-background-color: #555555;
            }
            QComboBox::drop-down {
                border: 0px;
                width: 25px;
                background: #3c3c3c;
                border-top-right-radius: 8px;
                border-bottom-right-radius: 8px;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 12px;
                height: 12px;
            }
            QComboBox QAbstractItemView {
                background-color: #1e1e1e;
                color: #ffffff;
                selection-background-color: #505050;
                selection-color: #ffffff;
            }
        """)
        def return_value():
            print(combo.currentText())

        combo.currentTextChanged.connect(return_value)

        layout = QVBoxLayout()
        layout.addWidget(combo)
        self.setLayout(layout)


app = QApplication([])
window = StyledComboDemo()
window.show()
app.exec_()




