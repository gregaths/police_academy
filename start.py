# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from bodily_harm import BodilyHarmWindow
from domesticvio import DomesticVioWindow
from courtorder import courtOrder
from gunlaw import GunPos
from soundmeter import Sound
from oblig import Obligation
from complaint import Complaint
import os
import sys

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ΒΟΗΘΟΣ ΑΞΥΠ - Επιλογές")
        self.setGeometry(200, 200, 800, 600)
        # Main layout (horizontal split)
        main_layout = QHBoxLayout()

        def resource_path(relative_path):
            try:
                base_path= sys._MEIPASS
            except Exception :
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)


        # Left side: Same as main window
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(resource_path("elas.jpg"))
        if pixmap.isNull():
            self.image_label = QLabel("Εικόνα elas.jpg δεν βρέθηκε")
        else:
            self.image_label = QLabel()
            self.image_label.setPixmap(pixmap.scaled(400, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_layout.addWidget(self.image_label)

        programmer_info = QLabel(
            "<center>Software Developer<br>Αθανασιάδης Γρηγόριος<br>Υπαστυνόμος Α<br>"
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
            "3. Αυτόφωρο ηχομέτρησης",
            "4. Νόμος Περί Όπλων",
            "5. Παραβίαση Δικαστικής Απόφασης",
            "6. Παραβίαση Υποχρέωσης Διατροφής",
            "7. Μήνυση Ιδιώτη",
            "8. Άρθρα Ποινικού Κώδικα",
            "9. Μήνυση για δάγκωμα σκύλου",
            "10. Παράνομη είσοδος Αλλοδαπών"
        ]
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(280, 60)
            if button_text == "1. Σωματικές Βλάβες":
                button.clicked.connect(self.open_bodily_harm)
            elif button_text == "2. Ενδοοικογενειακή Βία":
                button.clicked.connect(self.open_domesticvio)
            elif button_text == "3. Αυτόφωρο ηχομέτρησης":
                button.clicked.connect(self.open_sound)
            elif button_text == "4. Νόμος Περί Όπλων":
                button.clicked.connect(self.open_gunpos)
            elif button_text == "5. Παραβίαση Δικαστικής Απόφασης":
                button.clicked.connect(self.open_courtordervio)
            elif button_text == "6. Παραβίαση Υποχρέωσης Διατροφής":
                button.clicked.connect(self.open_oblig)
            elif button_text == "7. Μήνυση Ιδιώτη":
                button.clicked.connect(self.open_complaint)
            right_layout.addWidget(button)

        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def open_bodily_harm(self):
        if not hasattr(self,'bodily_window') or not self.bodily_window:
            self.bodily_window = BodilyHarmWindow(parent_window = self)
        self.bodily_window.show()
        self.hide()

    def open_domesticvio(self):
        if not hasattr(self,'domestic_window') or not self.domestic_window:
            self.domestic_window = DomesticVioWindow(parent_window = self)
        self.domestic_window.show()
        self.hide()


    def open_sound(self):
        if not hasattr(self,'sound_window ') or not self.sound_window:
            self.sound_window = Sound(parent_window=self)
        self.sound_window.show()
        self.hide()


    def open_courtordervio(self):
        if not hasattr(self,'courtorder_window ') or not self.courtorder_window:
            self.courtorder_window = courtOrder(parent_window=self)
        self.courtorder_window.show()
        self.hide()

    def open_gunpos(self):
        if not hasattr(self,'gunpos_window') or not self.gunpos_window:
            self.gunpos_window = GunPos(parent_window = self)
        self.gunpos_window.show()
        self.hide()

    def open_oblig(self):
        if not hasattr(self,'oblig_window ') or not self.oblig_window :
            self.oblig_window = Obligation(parent_window=self)
        self.oblig_window.show()
        self.hide()

    def open_complaint(self):
        if not hasattr(self, 'complaint_window ') or not self.complaint_window:
            self.complaint_window = Complaint(parent_window = self)
        self.complaint_window.show()
        self.hide()



