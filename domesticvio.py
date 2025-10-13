from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFormLayout, QTextEdit, QListWidget, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import sys


class DomesticVioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ενδοοικογενειακή Βία")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QHBoxLayout()

        def resource_path(relative_path):
            try:
                base_path=sys._MEIPASS
            except Exception:
                base_path=os.path.abspath(".")
            return os.path.join(base_path,relative_path)

        # Left side: Image and programmer info
        left_layout=QVBoxLayout()
        pixmap=QPixmap(resource_path("elas.jpg"))
        if pixmap.isNull():
            self.image_label = QLabel("Εικόνα elas.jpg δεν βρέθηκε")
        else:
            self.image_label = QLabel()
            self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_layout.addWidget(self.image_label)

        programmer_info = QLabel (
            "<center>Program Editor<br>Αθανάσιος Γρηγόριος<br>Υπαστυνόμος Α<br>"
            "Αστυνομικό Τμήμα Θεσσαλονίκης<br>Διεύθυνση Αστυνομίας Θεσσαλονίκης<br>Version 1.0<br>"
            "© 2025 All Rights Reserved</center>"
        )
        programmer_info.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(programmer_info)
        main_layout.addLayout(left_layout, 1)

        # Right side: Options for bodily harm
        right_layout = QVBoxLayout()
        options = [
            "1. Μήνυση κατά αγνώστου" ,
            "2. Μήνυση με γνωστό δράστη" ,
            "3. Μήνυση με γνωστό δράστη και σύλληψη?" ,
            "4. Αλληλομήνυση"
        ]
        for option in options:
            button = QPushButton( option )
            if option == "1. Μήνυση κατά αγνώστου":
                button.clicked.connect(self.open_case_1)
            elif option == "2. Μήνυση με γνωστό δράστη?":
                button.clicked.connect(self.open_case_2)
            elif option == "3. Μήνυση με γνωστό δράστη και σύλληψη?":
                button.clicked.connect(self.open_case_3a)
            elif option == "4. Αλληλομήνυση":
                button.clicked.connect( self.open_case_4 )
            else:
                button.clicked.connect(lambda checked, opt=option: self.handle_option(opt))
            right_layout.addWidget(button)

        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def open_case_1(self):
        self.case_1_window = Case1Window()
        self.case_1_window.show()
        self.hide()

    def open_case_2(self):
        self.case_2_window = Case2Window( )
        self.case_2_window.show( )
        self.hide( )

    def open_case_3a(self):
        self.case_3a_window = Case3Window( )
        self.case_3a_window.show( )
        self.hide( )

    def open_case_4(self):
        self.case_4_window = Case4Window( )
        self.case_4_window.show( )
        self.hide( )

class Case1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mήνυση κατά αγνώστου")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        label = QLabel("Περιεχόμενο για Μήνυση κατά αγνώστου" )
        layout.addWidget(label)

        # Back button
        back_button = QPushButton("Επιστροφή")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        self.hide()
        # You'll need to handle going back to main window


class Case2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μήνυση με γνωστό δράστη")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
        label = QLabel("Περιεχόμενο για Μήνυση με γνωστό δράστη?" )
        layout.addWidget(label)

        # Back button
        back_button = QPushButton("Επιστροφή")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        self.hide( )
        # You'll need to handle going back to main window



class Case3Window(QWidget):
    def __init__(self):
        super( ).__init__( )
        self.setWindowTitle( "Μήνυση με γνωστό δράστη και σύλληψη" )
        self.setGeometry( 100 , 100 , 600 , 400 )

        layout = QVBoxLayout( )
        label = QLabel( "Περιεχόμενο για Μήνυση με γνωστό δράστη και σύλληψη" )
        layout.addWidget( label )

        # Back button
        back_button = QPushButton( "Επιστροφή" )
        back_button.clicked.connect( self.go_back )
        layout.addWidget( back_button )

        self.setLayout( layout )

    def go_back(self):
        self.hide( )
        # You'll need to handle going back to main window


class Case4Window(QWidget):
    def __init__(self):
        super( ).__init__( )
        self.setWindowTitle( "Αλληλομήνυση" )
        self.setGeometry( 100 , 100 , 600 , 400 )

        layout = QVBoxLayout( )
        label = QLabel( "Αλληλομήνυση" )
        layout.addWidget( label )

        # Back button
        back_button = QPushButton( "Επιστροφή" )
        back_button.clicked.connect( self.go_back )
        layout.addWidget( back_button )

        self.setLayout( layout )

    def go_back(self):
        self.hide( )
        # You'll need to handle going back to main window