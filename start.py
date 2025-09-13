# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from bodily_harm import BodilyHarmWindow
from domesticvio import DomesticVioWindow


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ΒΟΗΘΟΣ ΑΞΥΠ - Επιλογές")
        self.setGeometry(200, 200, 800, 600)

        # Main layout (horizontal split)
        main_layout = QHBoxLayout()

        # Left side: Same as main window
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("elas.jpg")
        if pixmap.isNull():
            self.image_label = QLabel("Εικόνα elas.jpg δεν βρέθηκε")
        else:
            self.image_label = QLabel()
            self.image_label.setPixmap(pixmap.scaled(400, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_layout.addWidget(self.image_label)

        programmer_info = QLabel(
            "<center>Program Editor<br>Αθανασιάδης Γρηγόριος<br>Υπαστυνόμος Α<br>"
            "Αστυνομικό Τμήμα Θέρμης Θεσσαλονίκης<br>Διεύθυνση Αστυνομίας Θεσσαλονίκης<br>Version 2.0<br>"
            "© 2025 All Rights Reserved</center>"
        )
        programmer_info.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(programmer_info)
        main_layout.addLayout(left_layout, 1)

        # Right side: Buttons
        right_layout = QVBoxLayout()
        buttons = [
            "1. Σωματικές Βλάβες",
            "2. Ενδοοικογενειακή Βία",
            "3. Εργατικά Ατυχήματα",
            "4. Νόμος Περί Όπλων",
            "5. Παραβίαση Δικαστικής Απόφασης",
            "6. Παραβίαση Υποχρεώσεων Διαρρήκτη",
            "7. Ατμόπλοιο-Αυτοκίνητα",
            "8. Certificates",
            "9. Αυτόφωρο ηχομέτρησης",
            "10. Παράνομη είσοδος Αλλοδαπών"
        ]
        for button_text in buttons:
            button = QPushButton(button_text)
            if button_text == "1. Σωματικές Βλάβες":
                button.clicked.connect(self.open_bodily_harm)
            elif button_text == "2. Ενδοοικογενειακή Βία":
                button.clicked.connect(self.open_domesticvio)
            right_layout.addWidget(button)

        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def open_bodily_harm(self):
        self.bodily_window = BodilyHarmWindow()
        self.bodily_window.show()
        self.hide()

    def open_domesticvio(self):
        self.domestic_window = DomesticVioWindow()
        self.domestic_window.show()
        self.hide()


