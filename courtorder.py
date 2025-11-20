from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFormLayout, QTextEdit, QListWidget, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from documents import (witness_report, silipsi, deltio_kat, apologia, rights, vas, transmission,
                       mutual,  silipsi_mutual, deltio_kat_mutual, apologia_mutual,  witness_report_adjudication,
                       transmission_adjudication, context)
from lawwindow import CourtOrder
import sys
import os


class courtOrder(QWidget):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window=parent_window
        self.setWindowTitle("Μήνυση για Παραβίαση Δικαστικής Απόφασης")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QHBoxLayout()

        def resource_path(relative_path):
            try:
                base_path= sys._MEIPASS
            except Exception :
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)


        # Left side: Image and programmer info
        left_layout = QVBoxLayout()
        pixmap = QPixmap(resource_path("elas.jpg"))
        if pixmap.isNull():
            self.image_label = QLabel("Εικόνα elas.jpg δεν βρέθηκε")
        else:
            self.image_label = QLabel()
            self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_layout.addWidget(self.image_label)
        programmer_info = QLabel(
            "<center>Software Developer<br>Αθανάσιος Γρηγόριος<br>Υπαστυνόμος Α<br>"
            "Αστυνομικό Τμήμα Θεσσαλονίκης<br>Διεύθυνση Αστυνομίας Θεσσαλονίκης<br>Version 1.0<br>"
            "© 2025 All Rights Reserved</center>"
        )
        programmer_info.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(programmer_info)
        main_layout.addLayout(left_layout, 1)

        # Right side: Options for bodily harm
        right_layout = QVBoxLayout( )
        options = [
            "1. Μήνυση για παραβίαση της απόφασης",
            "2. Μήνυση με γνωστό δράστη και σύλληψη",
            "3. Άρθρο 169Α του Π.Κ - Ανάλυση",
            "4. ← Πίσω"
        ]

        for option in options:
            button = QPushButton(option)
            button.setFixedSize(280, 60)
            if option == "1. Μήνυση για παραβίαση της απόφασης":
                button.clicked.connect(self.open_case_1)
            elif option == "2. Μήνυση με γνωστό δράστη και σύλληψη":
                button.clicked.connect(self.open_case_2)
            elif option == "3. Άρθρο 169Α του Π.Κ - Ανάλυση":
                button.clicked.connect(self.open_case_3a)
            elif option == "4. ← Πίσω":
                button.clicked.connect(self.open_case_4)
            else:
                button.clicked.connect(lambda checked, opt=option: self.handle_option(opt))
            right_layout.addWidget(button)

        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def handle_option(self , option):
        # Placeholder for other options (can be expanded later)
        pass

    def open_case_1(self):
        self.case_1_window = Case1Window()
        self.case_1_window.show()
        self.hide()

    def open_case_2(self):
        self.case_2_window = Case2Window()
        self.case_2_window.show()
        self.hide()

    def open_case_3a(self):
        self.case_3a_window = CourtOrder()
        self.case_3a_window.show()
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
        self.setWindowTitle("Μήνυση για παραβίαση της απόφασης")
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
            ("first_officer", "1ος Ανακριτικός Υπάλληλος?"),
            ("policeStation", "Αστυνομικό Τμήμα?"),
            ("sec_officer", "2ος Ανακριτικός Υπάλληλος?"),
            ("surname", "Επώνυμο?"),
            ("name", "Όνομα?"),
            ("fathername", "Όνομα πατέρα?"),
            ("mothername", "Όνομα μητέρας?"),
            ("dateOfBirth", "Ημερομηνία Γέννησης?"),
            ("placeOfBirth", "Μέρος Γέννησης?"),
            ("address", "Διεύθυνση?"),
            ("tel", "Αριθμός τηλεφώνου?"),
            ("email", "Ηλεκτρονικό Ταχυδρομείο?"),
            ("DAT", "Δ.Α.Τ?"),
            ("issued", "Πότε εκδόθηκε?"),
            ("place_issued", "Που εκδόθηκε?"),
            ("afm", "Αριθμός ΑΦΜ?"),
            ("doy", "Δ.Ο.Υ?"),
            ("dateOfCrime", "Πότε-Ημερομηνία που έγινε το δίκημα?"),
            ("hourOfCrime", "Ακριβής ώρα αδικήματος?"),
            ("placeOfCrime", "Τοποθεσία αδικήματος?"),
            ("surnamePerperator", "Επώνυμο δράστη?"),
            ("namePerperator", "Όνομα δράστη?"),
            ("fathernamePerperator", "Πατρόνυμο δράστη?"),
            ("mothernamePerperator", "Μητρόνυμο δράστη?"),
            ("dateOfBirthPerperator", "Ημερ. γέννησης δράστη?"),
            ("placeOfBirthPerperator", "Τοποθεσία γέννησης δράστη?"),
            ("addressPerperator", "Διεύθυνση δράστη?"),
            ("telPreperator", "Τηλέφωνο δράστη?"),
            ("emailPreperator", "Email δράστη?"),
            ("DATperperator", "Δ.Α.Τ δράστη?"),
            ("issuedPerperator", "Πότε εκδόθηκε ΔΑΤ δράστη?"),
            ("place_issuedPerperator", "Που εκδόθηκε ΔΑΤ δράστη?"),
            ("afmPreperator", "ΑΦΜ δράστη?"),
            ("doyPrep", "ΔΟΥ δράστη?"),
            ("dateOfSeparation", "Πότε χωρίσατε?"),
            ("numberOfChildren", "Πόσα παιδι-ά  αποκτήσατε?"),
            ("numberOfChildren", "Ονόματα ηλικίες?"),
            ("numberOfAdjudication", "Αριθμός Δικαστικής Απόφασης"),
            ("dateOfAdjudication", "Ημερομηνία Δικαστικής Απόφασης?"),
            ("nameOfAdjudication", "Ονοματολογία Δικαστικής Απόφασης"),
            ("Adjudicationr", "Τι προέβλεπε και παραβιάστηκε στην απόφαση"),
            ("whatHappened", "Τι έγινε?"),
            ("add_something", "Θέλεις να προσθέσεις κάτι?"),
            ("hourOfReportFinished", "Τι ώρα τελείωσε η έκθεση μάρτυρα?"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?")
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

        # Offences section with larger textarea
        offences_layout = QHBoxLayout()
        self.offence_input = QTextEdit()
        self.offence_input.setFixedHeight(100)  # Ομοιόμορφο ύψος
        add_button = QPushButton("Προσθήκη Αδικήματος")
        add_button.clicked.connect(self.add_offence)
        offences_layout.addWidget(self.offence_input)
        offences_layout.addWidget(add_button)
        form_layout.addRow("Αδικήματα:", offences_layout)

        self.offences_list = QListWidget()
        self.offences_list.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list)

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
                self.context[key] = widget.toPlainText()
            else:
                self.context[key] = widget.text()
        self.context['offences'] = [self.offences_list.item(i).text() for i in
                                    range(self.offences_list.count())]

        witness_report_adjudication()
        deltio_kat()
        transmission_adjudication()


class Case2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μήνυση με γνωστό δράστη και σύλληψη")
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
            ("place" , "Σε ποιο Αστυνομικό Τμήμα?") ,
            ("date_num" , "Ημερομηνία αριθμητικά?") ,
            ("month" , "Μήνας?") ,
            ("year" , "Έτος?") ,
            ("day" , "Ημέρα?") ,
            ("hour" , "Ώρα?") ,
            ("first_officer" , "1ος Ανακριτικός Υπάλληλος?") ,
            ("policeStation" , "Αστυνομικό Τμήμα?") ,
            ("sec_officer" , "2ος Ανακριτικός Υπάλληλος?") ,
            ("surname" , "Επώνυμο?") ,
            ("name" , "Όνομα?") ,
            ("fathername" , "Όνομα πατέρα?") ,
            ("mothername" , "Όνομα μητέρας?") ,
            ("dateOfBirth" , "Ημερομηνία Γέννησης?") ,
            ("placeOfBirth" , "Μέρος Γέννησης?") ,
            ("address" , "Διεύθυνση?") ,
            ("tel" , "Αριθμός τηλεφώνου?") ,
            ("email" , "Ηλεκτρονικό Ταχυδρομείο?") ,
            ("DAT" , "Δ.Α.Τ?") ,
            ("issued" , "Πότε εκδόθηκε?") ,
            ("place_issued" , "Που εκδόθηκε?") ,
            ("afm" , "Αριθμός ΑΦΜ?") ,
            ("doy" , "Δ.Ο.Υ?") ,
            ("dateOfCrime" , "Πότε-Ημερομηνία που έγινε το δίκημα?") ,
            ("hourOfCrime" , "Ακριβής ώρα αδικήματος?") ,
            ("placeOfCrime" , "Τοποθεσία αδικήματος?") ,
            ("surnamePerperator" , "Επώνυμο δράστη?") ,
            ("namePerperator" , "Όνομα δράστη?") ,
            ("fathernamePerperator" , "Πατρόνυμο δράστη?") ,
            ("mothernamePerperator" , "Μητρόνυμο δράστη?") ,
            ("dateOfBirthPerperator" , "Ημερ. γέννησης δράστη?") ,
            ("placeOfBirthPerperator" , "Τοποθεσία γέννησης δράστη?") ,
            ("addressPerperator" , "Διεύθυνση δράστη?") ,
            ("telPreperator" , "Τηλέφωνο δράστη?") ,
            ("emailPreperator" , "Email δράστη?") ,
            ("DATperperator" , "Δ.Α.Τ δράστη?") ,
            ("issuedPerperator" , "Πότε εκδόθηκε ΔΑΤ δράστη?") ,
            ("place_issuedPerperator" , "Που εκδόθηκε ΔΑΤ δράστη?") ,
            ("afmPreperator" , "ΑΦΜ δράστη?") ,
            ("doyPrep" , "ΔΟΥ δράστη?") ,
            ("dateOfSeparation" , "Πότε χωρίσατε?") ,
            ("numberOfChildren" , "Πόσα παιδι-ά  αποκτήσατε?") ,
            ("numberOfChildren" , "Ονόματα ηλικίες?") ,
            ("numberOfAdjudication", "Αριθμός Δικαστικής Απόφασης") ,
            ("dateOfAdjudication", "Ημερομηνία Δικαστικής Απόφασης?") ,
            ("nameOfAdjudication", "Ονοματολογία Δικαστικής Απόφασης") ,
            ("Adjudication", "Τι προέβλεπε και παραβιάστηκε στην απόφαση") ,
            ("whatHappened" , "Τι έγινε?") ,
            ("add_something" , "Θέλεις να προσθέσεις κάτι?") ,
            ("hourOfReportFinished" , "Τι ώρα τελείωσε η έκθεση μάρτυρα?") ,
            ("protocolnumber" , "Αριθμός πρωτοκόλλου?"),
            ("startTimeArrestReport","Ώρα Έναρξης Έκθεσης Σύλληψης?"),
            ("officer_arrest","Αστυνομικός που τον συνέλαβε?"),
            ("dateOfArrest","Ημερομηνία Σύλληψης?"),
            ("hourOfArrest","Ώρα σύλληψης?"),
            ("placeOfArrest","Τοποθεσία σύλληψης?"),
            ("endTimeOfReport","Ώρα Λήξης Έκθεσης Σύλληψης?"),
            ("date_num_apologia","Ημερομηνία αριθμητικά (Απολογία)?"),
            ("month_apologia","Μήνας (Απολογία)?"),
            ("year_apologia","Έτος (Απολογία)?"),
            ("day_apologia","Ημέρα (Απολογία)?"),
            ("start_hour_apologia","Ώρα Έναρξης (Απολογία)?"),
            ("question_rights_apologia","Επιθυμείτε να κάνετε χρήση των δικαιωμάτων?"),
            ("question_crime_apologia","Κατηγορήθηκες άλλη φορά και για ποια αιτία?"),
            ("question_crime_confess","Τι απολογείσαι?"),
            ("end_hour_apologia","Ώρα περάτωσης (Απολογία)?"),
            ("start_time_rights","Ώρα Έναρξης (Δικαιώματα)?"),
            ("end_time_rights","Ώρα περάτωσης (Δικαιώματα)?")
        ]

        for key, label in fields :
            self.inputs[key]=QTextEdit()
            if key not in ["place", "date_num", "month", "year", "day", "hour", "first_officer", "policeStation",
                           "sec_officer",
                           "surname", "name", "fathername", "mothername", "dateOfBirth", "placeOfBirth", "address",
                           "tel",
                           "email", "DAT", "issued", "place_issued", "afm", "doy", "dateOfCrime", "hourOfCrime",
                           "placeOfCrime",
                           "surnamePerperator", "namePerperator", "fathernamePerperator", "mothernamePerperator",
                           "dateOfBirthPerperator", "placeOfBirthPerperator", "addressPerperator", "telPreperator",
                           "emailPreperator", "DATperperator", "issuedPerperator", "place_issuedPerperator",
                           "afmPreperator",
                           "doyPrep"] :
                self.inputs[key].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            else:
                self.inputs[key].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            form_layout.addRow(QLabel(label), self.inputs[key])

        # Offences section with larger textarea
        offences_layout=QHBoxLayout()
        self.offence_input=QTextEdit()
        self.offence_input.setFixedHeight(100)  # Ομοιόμορφο ύψος
        add_button=QPushButton("Προσθήκη Αδικήματος")
        add_button.clicked.connect(self.add_offence)
        offences_layout.addWidget(self.offence_input)
        offences_layout.addWidget(add_button)
        form_layout.addRow("Αδικήματα:", offences_layout)

        self.offences_list=QListWidget( )
        self.offences_list.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list)

        # Generate button
        generate_button=QPushButton("Δημιουργία Εγγράφων")
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
                self.context[key]=widget.toPlainText()
            else:
                self.context[key]=widget.text()
        self.context['offences'] = [self.offences_list.item(i).text() for i in range(self.offences_list.count())]
        witness_report_adjudication()
        transmission_adjudication()
        silipsi()
        deltio_kat()
        apologia()
        rights()
        vas()



