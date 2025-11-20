from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFormLayout, QTextEdit, QListWidget, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from documents import (witness_report, silipsi, deltio_kat, apologia, rights, vas, transmission,
                       mutual,  silipsi_mutual, deltio_kat_mutual, apologia_mutual,  witness_report_adjudication,
                       transmission_adjudication, context)
from documents2 import arrest_aftoforo, seizure, arrest_aftoforo2, seizure2, deltio_kat2, transmission_sound
import os
import sys
from lawwindow import SoundLaw


class Sound(QWidget):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window
        self.setWindowTitle("Ηχομέτρηση")
        self.setGeometry(100, 100, 800, 600)

        main_layout=QHBoxLayout()

        def resource_path(relative_path):
            try:
                base_path=sys._MEIPASS
            except Exception:
                base_path=os.path.abspath(".")
            return os.path.join(base_path,relative_path)

            # Left side: Image and programmer info

        left_layout=QVBoxLayout()
        pixmap=QPixmap(resource_path("elas.jpg"))
        if pixmap.isNull() :
            self.image_label=QLabel("Εικόνα elas.jpg δεν βρέθηκε")
        else :
            self.image_label=QLabel()
            self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_layout.addWidget(self.image_label)
        programmer_info=QLabel(
            "<center>Software Developer<br>Αθανάσιος Γρηγόριος<br>Υπαστυνόμος Α<br>"
            "Αστυνομικό Τμήμα Θεσσαλονίκης<br>Διεύθυνση Αστυνομίας Θεσσαλονίκης<br>Version 1.0<br>"
            "© 2025 All Rights Reserved</center>"
        )
        programmer_info.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(programmer_info)
        main_layout.addLayout(left_layout, 1)

        # Right side: Options for bodily harm
        right_layout=QVBoxLayout()
        options=[
            "1. Αυτόφωρη διαδικασία ηχομέτρησης με προσωρινά υπεύθυνο",
            "2. Αυτόφωρη διαδικασία ηχομέτρησης με ιδιοκτήτη",
            "3. Νομος περί διατάραξης κοινής ησυχίας",
            "4. ← Πίσω"
        ]

        for option in options :
            button = QPushButton(option)
            button.setFixedSize(280, 60)
            if option == "1. Αυτόφωρη διαδικασία ηχομέτρησης με προσωρινά υπεύθυνο":
                button.clicked.connect(self.open_case_1)
            if option == "2. Αυτόφωρη διαδικασία ηχομέτρησης με ιδιοκτήτη":
                button.clicked.connect(self.open_case_2)
            elif option == "3. Νομος περί διατάραξης κοινής ησυχίας":
                button.clicked.connect(self.open_case_3)
            elif option == "4. ← Πίσω":
                button.clicked.connect(self.open_case_4)
            else :
                button.clicked.connect(lambda checked, opt=option : self.handle_option(opt))
            right_layout.addWidget(button)

        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def handle_option(self , option):
        # Placeholder for other options (can be expanded later)
        pass

    def open_case_1(self) :
        self.case_1_window=Case1Window()
        self.case_1_window.show()
        self.hide()

    def open_case_2(self) :
        self.case_1_window=Case2Window()
        self.case_1_window.show()
        self.hide()

    def open_case_3(self) :
        self.case_2_window= SoundLaw()
        self.case_2_window.show()
        self.hide()

    def open_case_4(self):
        self.go_back_to_start()

    def go_back_to_start(self):
        """Επιστροφή στην κύρια οθόνη"""
        if self.parent_window:
            self.parent_window.show()
            self.parent_window.raise_()
            self.parent_window.activateWindow()
        self.hide()


class Case1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ηχομέτρηση αυτόφωρο")
        self.setGeometry(100, 100, 600, 800)
        self.context = context
        # Main layout
        main_layout = QVBoxLayout()

        # Form for inputs with scrollbar
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        form_widget = QWidget()
        form_layout = QFormLayout()
        form_widget.setLayout(form_layout)
        scroll.setWidget(form_widget)
        self.inputs={}
        fields=[
            ("place", "Σε ποιο Αστυνομικό Τμήμα?"),
            ("date_num", "Ημερομηνία αριθμητικά?"),
            ("month", "Μήνας?"),
            ("year", "Έτος?"),
            ("day", "Ημέρα?"),
            ("hour", "Ώρα?"),
            ("officer", "Αστυνομικός που συνέλαβε?"),
            ("policeStation2", "Υπηρεσία?"),
            ('hourOfCrime', 'Ώρα εγκλήματος'),
            ('dateOfCrime', 'Ημερομηνία εγκλήματος'),
            ('placeOfCrime', 'Τοποθεσία εγκλήματος?'),
            ("surnamePerperator", "Επώνυμο υπεύθυνου?"),
            ("namePerperator", "Όνομα υπεύθυνου?"),
            ("fathernamePerperator", "Πατρώνυμο υπεύθυνου?"),
            ("mothernamePerperator", "Μητρώνυμο υπεύθυνου?"),
            ("dateOfBirthPerperator", "Ημερ. γέννησης υπεύθυνου?"),
            ("placeOfBirthPerperator", "Τοποθεσία γέννησης υπεύθυνου?"),
            ("addressPerperator", "Διεύθυνση υπεύθυνου?"),
            ("telPreperator", "Τηλέφωνο υπεύθυνου?"),
            ("emailPreperator", "Email υπεύθυνου?"),
            ("DATperperator", "Δ.Α.Τ υπεύθυνου?"),
            ("issuedPerperator", "Πότε εκδόθηκε ΔΑΤ υπεύθυνου?"),
            ("place_issuedPerperator", "Που εκδόθηκε ΔΑΤ υπεύθυνου?"),
            ("afmPreperator", "ΑΦΜ υπεύθυνου?"),
            ("doyPrep", "ΔΟΥ υπεύθυνου?"),
            ('typeOfStore', 'Είδος καταστήματος'),
            ('nameOfStore', 'Όνομα Καταστήματος?'),
            ("surname", "Επώνυμο ιδιοκτήτη?"),
            ("name", "Όνομα ιδιοκτήτη?"),
            ("fathername", "Όνομα πατέρα ιδιοκτήτη?"),
            ("mothername", "Όνομα μητέρας ιδιοκτήτη?"),
            ("dateOfBirth", "Ημερομηνία Γέννησης ιδιοκτήτη?"),
            ("placeOfBirth", "Μέρος Γέννησης ιδιοκτήτη?"),
            ("address", "Διεύθυνση ιδιοκτήτη?"),
            ("tel", "Αριθμός τηλεφώνου ιδιοκτήτη?"),
            ("email", "Ηλεκτρονικό Ταχυδρομείο ιδιοκτήτη?"),
            ("DAT", "Δ.Α.Τ ιδιοκτήτη?"),
            ("issued", "Πότε εκδόθηκε ιδιοκτήτη?"),
            ("place_issued", "Που εκδόθηκε ιδιοκτήτη?"),
            ("afm", "Αριθμός ΑΦΜ ιδιοκτήτη?"),
            ("doy", "Δ.Ο.Υ ιδιοκτήτη?"),
            ("measurement", "Μέγιστη Ηχοστάθμη ολογράφως"),
            ('measurNum', 'Ηχοστάθμη αριθμ π.χ (85.5)'),
            ('hourOfReportFinished', 'Πότε τελείωσε η έκθεση?'),
            ("hourSeizure", "Ώρα έναρξης κατάσχεσης"),
            ('first_officer', '1ος Ανακριτικός Υπάλληλος'),
            ('policeStation', 'Υπηρεσία?'),
            ('sec_officer', '2oς Ανακριτικός Υπάλληλος?'),
            ('seizure', 'Προιόν κατάσχεσης?'),
            ("hourOfSeizureFinished", "Ώρα λήξης κατάσχεσης"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?"),



        ]

        for key, label in fields:
            self.inputs[ key ]=QTextEdit()
            if key in [ "place", "date_num", "month", "year", "day", "hour", "first_officer", "policeStation",
                        "sec_officer",
                        "surname", "name", "fathername", "mothername", "dateOfBirth", "placeOfBirth", "address",
                        "tel",
                        "email", "DAT", "issued", "place_issued", "afm", "doy", "dateOfCrime", "hourOfCrime",
                        "placeOfCrime",
                        "surnamePerperator", "namePerperator", "fathernamePerperator", "mothernamePerperator",
                        "dateOfBirthPerperator", "placeOfBirthPerperator", "addressPerperator", "telPreperator",
                        "emailPreperator", "DATperperator", "issuedPerperator", "place_issuedPerperator",
                        "afmPreperator",
                        "doyPrep" ]:
                self.inputs[ key ].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            else:
                self.inputs[ key ].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            form_layout.addRow(QLabel(label), self.inputs[ key ])



        # Generate button
        generate_button = QPushButton("Δημιουργία Εγγράφων")
        generate_button.clicked.connect(self.generate_documents)
        main_layout.addWidget(generate_button)

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)



    def generate_documents(self) :
            for key, widget in self.inputs.items() :
                if isinstance(widget, QTextEdit) :
                    self.context[key]=widget.toPlainText()
                else :
                    self.context[key] =widget.text()


            arrest_aftoforo()
            seizure()
            deltio_kat()
            deltio_kat2()
            transmission_sound()


class Case2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ηχομέτρηση αυτόφωρο")
        self.setGeometry(100, 100, 600, 800)
        self.context = context
        # Main layout
        main_layout = QVBoxLayout()

        # Form for inputs with scrollbar
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        form_widget = QWidget()
        form_layout = QFormLayout()
        form_widget.setLayout(form_layout)
        scroll.setWidget(form_widget)
        self.inputs = {}
        fields = [
            ("place", "Σε ποιο Αστυνομικό Τμήμα?"),
            ("date_num", "Ημερομηνία αριθμητικά?"),
            ("month", "Μήνας?"),
            ("year", "Έτος?"),
            ("day", "Ημέρα?"),
            ("hour", "Ώρα?"),
            ("officer", "Αστυνομικός π[ου συνέλαβε?"),
            ("policeStation", "Αστυνομικό Τμήμα?"),
            ('hourOfCrime', 'Ώρα εγκλήματος'),
            ('dateOfCrime', 'Ημερομηνία εγκλήματος'),
            ('placeOfCrime', 'Τοποθεσία εγκλήματος?'),
            ("surnamePerperator", "Επώνυμο υπεύθυνου?"),
            ("namePerperator", "Όνομα υπεύθυνου?"),
            ("fathernamePerperator", "Πατρόνυμο υπεύθυνου?"),
            ("mothernamePerperator", "Μητρόνυμο υπεύθυνου?"),
            ("dateOfBirthPerperator", "Ημερ. γέννησης υπεύθυνου?"),
            ("placeOfBirthPerperator", "Τοποθεσία γέννησης υπεύθυνου?"),
            ("addressPerperator", "Διεύθυνση υπεύθυνου?"),
            ("telPreperator", "Τηλέφωνο υπεύθυνου?"),
            ("emailPreperator", "Email υπεύθυνου?"),
            ("DATperperator", "Δ.Α.Τ υπεύθυνου?"),
            ("issuedPerperator", "Πότε εκδόθηκε ΔΑΤ υπεύθυνου?"),
            ("place_issuedPerperator", "Που εκδόθηκε ΔΑΤ υπεύθυνου?"),
            ("afmPreperator", "ΑΦΜ υπεύθυνου?"),
            ("doyPrep", "ΔΟΥ υπεύθυνου?"),
            ('typeOfStore', 'Είδος καταστήματος'),
            ('nameOfStore', 'Όνομα Καταστήματος?'),
            ("surname", "Επώνυμο ιδιοκτήτη?"),
            ("name", "Όνομα ιδιοκτήτη?"),
            ("fathername", "Όνομα πατέρα ιδιοκτήτη?"),
            ("mothername", "Όνομα μητέρας ιδιοκτήτη?"),
            ("dateOfBirth", "Ημερομηνία Γέννησης ιδιοκτήτη?"),
            ("placeOfBirth", "Μέρος Γέννησης ιδιοκτήτη?"),
            ("address", "Διεύθυνση ιδιοκτήτη?"),
            ("tel", "Αριθμός τηλεφώνου ιδιοκτήτη?"),
            ("email", "Ηλεκτρονικό Ταχυδρομείο ιδιοκτήτη?"),
            ("DAT", "Δ.Α.Τ ιδιοκτήτη?"),
            ("issued", "Πότε εκδόθηκε ιδιοκτήτη?"),
            ("place_issued", "Που εκδόθηκε ιδιοκτήτη?"),
            ("afm", "Αριθμός ΑΦΜ ιδιοκτήτη?"),
            ("doy", "Δ.Ο.Υ ιδιοκτήτη?"),
            ("measurement", "Μέγιστη Ηχοστάθμη ολογράφως"),
            ('measurNum', 'Ηχοστάθμη αριθμ π.χ (85.5)'),
            ('hourOfReportFinished', 'Πότε τελείωσε η έκθεση?'),
            ("hourSeizure", "Ώρα έναρξης κατάσχεσης"),
            ('first_officer', '1ος Ανακριτικός Υπάλληλος'),
            ('policeStation', 'Υπηρεσία?'),
            ('sec_officer', '2oς Ανακριτικός Υπάλληλος?'),
            ('seizure', 'Προιόν κατάσχεσης?'),
            ("hourOfSeizureFinished", "Ώρα λήξης κατάσχεσης"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?"),


        ]


        # Generate button
        generate_button = QPushButton("Δημιουργία Εγγράφων")
        generate_button.clicked.connect(self.generate_documents)
        main_layout.addWidget(generate_button)

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def add_offence(self):
        offence = self.offence_input.toPlainText().strip()
        if offence:
            self.offences_list.addItem(offence)
            self.offence_input.clear()  # Καθαρίζει μετά την προσθήκη

    def generate_documents(self):
        for key, widget in self.inputs.items():
            if isinstance(widget, QTextEdit):
                self.context[ key ] = widget.toPlainText()
            else:
                self.context[ key ] = widget.text()
        self.context[ 'offences' ] = [ self.offences_list.item(i).text() for i in
                                       range(self.offences_list.count()) ]

        arrest_aftoforo2()
        seizure2()
        silipsi()
        deltio_kat()
        apologia()
        rights()