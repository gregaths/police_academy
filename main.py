import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTextEdit, QTextBrowser)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from start import StartWindow
from bodily_harm import BodilyHarmWindow
from biowindow import BioWindow
import os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_window = StartWindow()
        self.setWindowTitle("ΒΟΗΘΟΣ ΑΞΥΠ")
        self.setGeometry(100, 100, 800, 600)

        # Main layout (horizontal split)
        main_layout = QHBoxLayout()

        def resource_path(relative_path):
            try:
                base_path= sys._MEIPASS
            except Exception :
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)

        # Left side: Image and programmer info
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
            "<center>Program Developer<br>Αθανασιάδης Γρηγόριος<br>Υπαστυνόμος Α<br>"
            "Bsc Πληροφορική Ε.Α.Π<br> Msc Υπολογιστική Νοημοσύνη και Ψηφιακά Μέσα Α.Π.Θ <br>"
            "Αστυνομικό Τμήμα Θέρμης Θεσσαλονίκης<br>"
            "Διεύθυνση Αστυνομίας Θεσσαλονίκης<br>Version 2.0<br>© 2025 All Rights Reserved</center>"
        )
        programmer_info.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(programmer_info)
        main_layout.addLayout(left_layout, 1)

        bio_button = QPushButton( "bio" )
        bio_button.setFixedSize(150, 40)  # Μικρό κουμπί
        bio_button.clicked.connect(self.open_bio)
        left_layout.addWidget(bio_button,  alignment=Qt.AlignCenter)

        dif_button = QPushButton("Σχετικά")
        dif_button.setFixedSize(150, 40)  # Μικρό κουμπί
        dif_button.clicked.connect(self.open_bio)
        left_layout.addWidget(dif_button, alignment = Qt.AlignCenter )

        # Right side: Title
        right_layout = QVBoxLayout()
        title_label = QLabel("ΒΟΗΘΟΣ ΑΞΥΠ version 2.0")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        right_layout.addWidget(title_label)

        start_button = QPushButton("Έναρξη")
        start_button.clicked.connect(self.open_start)
        start_button.setFixedSize(200, 50)
        start_button.setStyleSheet("font-size: 20px solid; font-weight: bold;" )
        right_layout.addWidget(start_button, alignment=Qt.AlignCenter)
        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def open_start(self):
        self.start_window.show()
        self.hide()



    def open_bio(self):
        self.bio_window =BioWindow()
        self.bio_window.show()

    def relevant(self):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())