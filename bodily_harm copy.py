# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFormLayout, QTextEdit, QListWidget, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from documents import (witness_report, iatrodik, silipsi,deltio_kat, apologia, rights, vas, transmission,
                       mutual, iatrodik_mutual, silipsi_mutual, deltio_kat_mutual, apologia_mutual,  context)


class BodilyHarmWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μήνυση με Σωματικές Βλάβες")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QHBoxLayout()

        # Left side: Image and programmer info
        left_layout = QVBoxLayout()
        pixmap = QPixmap("elas.jpg")
        if pixmap.isNull():
            self.image_label = QLabel("Εικόνα elas.jpg δεν βρέθηκε")
        else:
            self.image_label = QLabel()
            self.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        left_layout.addWidget(self.image_label)

        programmer_info = QLabel(
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
            "1. Μήνυση κατά αγνώστου",
            "2. Μήνυση με γνωστό δράστη?",
            "3. Μήνυση με γνωστό δράστη και σύλληψη?",
            "4. Αλληλομήνυση"
        ]
        for option in options:
            button = QPushButton(option)
            if option == "1. Μήνυση κατά αγνώστου":
                button.clicked.connect(self.open_case_1)
            elif option == "2. Μήνυση με γνωστό δράστη?":
                button.clicked.connect(self.open_case_2)
            elif option == "3. Μήνυση με γνωστό δράστη και σύλληψη?":
                button.clicked.connect(self.open_case_3a)
            elif option == "4. Αλληλομήνυση":
                button.clicked.connect(self.open_case_4)
            else:
                button.clicked.connect(lambda checked, opt=option: self.handle_option(opt))
            right_layout.addWidget(button)

        main_layout.addLayout(right_layout, 1)
        self.setLayout(main_layout)

    def handle_option(self, option):
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
        self.case_3a_window = Case3aWindow()
        self.case_3a_window.show()
        self.hide()

    def open_case_4(self):
        self.case_4_window = Case4Window()
        self.case_4_window.show()
        self.hide()


class Case1Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μήνυση με Γνωστό Δράστη και Σύλληψη")
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
            ("place" ,"Σε ποιο Αστυνομικό Τμήμα?") ,
            ("date_num" ,"Ημερομηνία αριθμητικά?") ,
            ("month" ,"Μήνας?") ,
            ("year" ,"Έτος?") ,
            ("day" ,"Ημέρα?") ,
            ("hour" ,"Ώρα?") ,
            ("first_officer" ,"1ος Ανακριτικός Υπάλληλος?") ,
            ("policeStation" ,"Αστυνομικό Τμήμα?") ,
            ("sec_officer" ,"2ος Ανακριτικός Υπάλληλος?") ,
            ("surname" ,"Επώνυμο?") ,
            ("name" ,"Όνομα?") ,
            ("fathername" ,"Όνομα πατέρα?") ,
            ("mothername" ,"Όνομα μητέρας?") ,
            ("dateOfBirth" ,"Ημερομηνία Γέννησης?") ,
            ("placeOfBirth" ,"Μέρος Γέννησης?") ,
            ("address" ,"Διεύθυνση?") ,
            ("tel" ,"Αριθμός τηλεφώνου?") ,
            ("email" ,"Ηλεκτρονικό Ταχυδρομείο?") ,
            ("DAT" ,"Δ.Α.Τ?") ,
            ("issued" ,"Πότε εκδόθηκε?") ,
            ("place_issued" ,"Που εκδόθηκε?") ,
            ("afm" ,"Αριθμός ΑΦΜ?") ,
            ("doy" ,"Δ.Ο.Υ?") ,
            ("dateOfCrime" ,"Πότε-Ημερομηνία που έγινε το δίκημα?") ,
            ("hourOfCrime" ,"Ακριβής ώρα αδικήματος?") ,
            ("placeOfCrime" ,"Τοποθεσία αδικήματος?") ,
            ("stateOfVictim" ,"Σε ποια κατάσταση βρισκόσουν?") ,
            ("surnamePerperator" ,"(Σημείωσε) άγνωστο δράστη"),
            ("whatHappened" ,"Τι έγινε?"),
            ("howHappened" ,"Πώς έγινε?"),
            ("whyHappened" ,"Γιατί έγινε?"),
            ("add_something" ,"Θέλεις να προσθέσεις κάτι?"),
            ("forensicExam" ,"Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution" ,"Επιθυμείς την ποινική δίωξη του δράστη?"),
            ("hourOfReportFinished" ,"Τι ώρα τελείωσε η έκθεση μάρτυρα?") ,
            ("protocolnumber" ,"Αριθμός πρωτοκόλλου?") ,
            ("placeOfHurt" ,"Πώς και πού προκλήθηκαν οι σωματικές βλάβες?") ,

        ]
        for key, label in fields:
            self.inputs[key] = QTextEdit()
            if key in ["place", "date_num", "month", "year", "day", "hour", "first_officer", "policeStation",
                        "sec_officer",
                        "surname", "name", "fathername", "mothername", "dateOfBirth", "placeOfBirth", "address", "tel",
                        "email", "DAT", "issued", "place_issued", "afm", "doy", "dateOfCrime", "hourOfCrime",
                        "placeOfCrime",
                        "surnamePerperator", "namePerperator", "fathernamePerperator", "mothernamePerperator",
                        "dateOfBirthPerperator", "placeOfBirthPerperator", "addressPerperator", "telPreperator",
                        "emailPreperator", "DATperperator", "issuedPerperator", "place_issuedPerperator",
                        "afmPreperator",
                        "doyPrep"]:
                self.inputs[key].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            else:
                self.inputs[key].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            form_layout.addRow(QLabel(label), self.inputs[key])

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
            else :
                self.context[key] = widget.text()
        self.context['offences'] = [self.offences_list.item(i).text() for i in
                                    range(self.offences_list.count())]
        witness_report()
        iatrodik()
        #vas ( )
        #transmission ( )


class Case3aWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μήνυση με Γνωστό Δράστη και Σύλληψη")
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
            ("stateOfVictim", "Σε ποια κατάσταση βρισκόσουν?"),
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
            ("whatHappened", "Τι έγινε?"),
            ("howHappened", "Πώς έγινε?"),
            ("whyHappened", "Γιατί έγινε?"),
            ("add_something", "Θέλεις να προσθέσεις κάτι?"),
            ("forensicExam", "Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution", "Επιθυμείς την ποινική δίωξη του δράστη?"),
            ("hourOfReportFinished", "Τι ώρα τελείωσε η έκθεση μάρτυρα?"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?"),
            ("placeOfHurt", "Πώς και πού προκλήθηκαν οι σωματικές βλάβες?"),
            ("startTimeArrestReport", "Ώρα Έναρξης Έκθεσης Σύλληψης?"),
            ("officer_arrest", "Αστυνομικός που τον συνέλαβε?"),
            ("dateOfArrest", "Ημερομηνία Σύλληψης?"),
            ("hourOfArrest", "Ώρα σύλληψης?"),
            ("placeOfArrest", "Τοποθεσία σύλληψης?"),
            ("endTimeOfReport", "Ώρα Λήξης Έκθεσης Σύλληψης?"),
            ("date_num_apologia", "Ημερομηνία αριθμητικά (Απολογία)?"),
            ("month_apologia", "Μήνας (Απολογία)?"),
            ("year_apologia", "Έτος (Απολογία)?"),
            ("day_apologia", "Ημέρα (Απολογία)?"),
            ("start_hour_apologia", "Ώρα Έναρξης (Απολογία)?"),
            ("question_rights_apologia", "Επιθυμείτε να κάνετε χρήση των δικαιωμάτων?"),
            ("question_crime_apologia", "Κατηγορήθηκες άλλη φορά και για ποια αιτία?"),
            ("question_crime_confess", "Τι απολογείσαι?"),
            ("end_hour_apologia", "Ώρα περάτωσης (Απολογία)?"),
            ("start_time_rights", "Ώρα Έναρξης (Δικαιώματα)?"),
            ("end_time_rights", "Ώρα περάτωσης (Δικαιώματα)?"),
        ]
        for key, label in fields:
            self.inputs[key] = QTextEdit()
            if key in ["place", "date_num", "month", "year", "day", "hour", "first_officer", "policeStation", "sec_officer",
                       "surname", "name", "fathername", "mothername", "dateOfBirth", "placeOfBirth", "address", "tel",
                       "email", "DAT", "issued", "place_issued", "afm", "doy", "dateOfCrime", "hourOfCrime", "placeOfCrime",
                       "surnamePerperator", "namePerperator", "fathernamePerperator", "mothernamePerperator",
                       "dateOfBirthPerperator", "placeOfBirthPerperator", "addressPerperator", "telPreperator",
                       "emailPreperator", "DATperperator", "issuedPerperator", "place_issuedPerperator", "afmPreperator",
                       "doyPrep"]:
                self.inputs[key].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            else:
                self.inputs[key].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            form_layout.addRow(QLabel(label), self.inputs[key])

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
        self.context['offences'] = [self.offences_list.item(i).text() for i in range(self.offences_list.count())]
        witness_report()
        iatrodik()
        silipsi()
        deltio_kat()
        apologia()
        rights()
        vas()
        transmission()


class Case2Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Μήνυση με Γνωστό Δράστη και Σύλληψη")
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
            ("place","Σε ποιο Αστυνομικό Τμήμα?") ,
            ("date_num" ,"Ημερομηνία αριθμητικά?") ,
            ("month" ,"Μήνας?") ,
            ("year" ,"Έτος?") ,
            ("day" ,"Ημέρα?") ,
            ("hour" ,"Ώρα?") ,
            ("first_officer" ,"1ος Ανακριτικός Υπάλληλος?") ,
            ("policeStation" ,"Αστυνομικό Τμήμα?") ,
            ("sec_officer" ,"2ος Ανακριτικός Υπάλληλος?") ,
            ("surname" ,"Επώνυμο?") ,
            ("name" ,"Όνομα?") ,
            ("fathername" ,"Όνομα πατέρα?") ,
            ("mothername" ,"Όνομα μητέρας?") ,
            ("dateOfBirth" ,"Ημερομηνία Γέννησης?") ,
            ("placeOfBirth" ,"Μέρος Γέννησης?") ,
            ("address" ,"Διεύθυνση?") ,
            ("tel" ,"Αριθμός τηλεφώνου?") ,
            ("email" ,"Ηλεκτρονικό Ταχυδρομείο?") ,
            ("DAT" ,"Δ.Α.Τ?") ,
            ("issued" ,"Πότε εκδόθηκε?") ,
            ("place_issued" ,"Που εκδόθηκε?") ,
            ("afm" ,"Αριθμός ΑΦΜ?") ,
            ("doy" ,"Δ.Ο.Υ?") ,
            ("dateOfCrime" ,"Πότε-Ημερομηνία που έγινε το δίκημα?") ,
            ("hourOfCrime" ,"Ακριβής ώρα αδικήματος?") ,
            ("placeOfCrime" ,"Τοποθεσία αδικήματος?") ,
            ("stateOfVictim" ,"Σε ποια κατάσταση βρισκόσουν?") ,
            ("surnamePerperator" ,"Επώνυμο δράστη?") ,
            ("namePerperator" ,"Όνομα δράστη?") ,
            ("fathernamePerperator" ,"Πατρόνυμο δράστη?") ,
            ("mothernamePerperator" ,"Μητρόνυμο δράστη?") ,
            ("dateOfBirthPerperator" ,"Ημερ. γέννησης δράστη?") ,
            ("placeOfBirthPerperator" ,"Τοποθεσία γέννησης δράστη?") ,
            ("addressPerperator" ,"Διεύθυνση δράστη?") ,
            ("telPreperator" ,"Τηλέφωνο δράστη?") ,
            ("emailPreperator" ,"Email δράστη?") ,
            ("DATperperator" ,"Δ.Α.Τ δράστη?") ,
            ("issuedPerperator" ,"Πότε εκδόθηκε ΔΑΤ δράστη?") ,
            ("place_issuedPerperator" ,"Που εκδόθηκε ΔΑΤ δράστη?") ,
            ("afmPreperator" ,"ΑΦΜ δράστη?") ,
            ("doyPrep","ΔΟΥ δράστη?") ,
            ("whatHappened" ,"Τι έγινε?") ,
            ("howHappened" ,"Πώς έγινε?") ,
            ("whyHappened" ,"Γιατί έγινε?") ,
            ("add_something" ,"Θέλεις να προσθέσεις κάτι?") ,
            ("forensicExam" ,"Επιθυμείς ιατροδικαστική εξέταση?") ,
            ("prosecution" ,"Επιθυμείς την ποινική δίωξη του δράστη?") ,
            ("hourOfReportFinished" ,"Τι ώρα τελείωσε η έκθεση μάρτυρα?") ,
            ("protocolnumber" ,"Αριθμός πρωτοκόλλου?") ,
            ("placeOfHurt" ,"Πώς και πού προκλήθηκαν οι σωματικές βλάβες?") ,

        ]
        for key,label in fields:
            self.inputs[key] = QTextEdit()
            if key in ["place","date_num","month","year","day","hour","first_officer","policeStation",
                       "sec_officer",
                       "surname","name","fathername","mothername","dateOfBirth","placeOfBirth","address","tel",
                       "email","DAT","issued","place_issued","afm","doy","dateOfCrime","hourOfCrime",
                       "placeOfCrime",
                       "surnamePerperator","namePerperator","fathernamePerperator","mothernamePerperator",
                       "dateOfBirthPerperator","placeOfBirthPerperator","addressPerperator","telPreperator",
                       "emailPreperator","DATperperator","issuedPerperator","place_issuedPerperator",
                       "afmPreperator",
                       "doyPrep"]:
                self.inputs[key].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            else:
                self.inputs[key].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            form_layout.addRow(QLabel(label), self.inputs[key])

        # Offences section with larger textarea
        offences_layout = QHBoxLayout()
        self.offence_input = QTextEdit()
        self.offence_input.setFixedHeight(100)  # Ομοιόμορφο ύψος
        add_button = QPushButton("Προσθήκη Αδικήματος")
        add_button.clicked.connect(self.add_offence)
        offences_layout.addWidget(self.offence_input)
        offences_layout.addWidget(add_button)

        form_layout.addRow ( "Αδικήματα:" ,offences_layout )

        self.offences_list = QListWidget ( )
        self.offences_list.setFixedHeight ( 150 )  # Εμφάνιση αδικημάτων
        form_layout.addRow ( self.offences_list )

        # Generate button
        generate_button = QPushButton ( "Δημιουργία Εγγράφων" )
        generate_button.clicked.connect ( self.generate_documents )
        main_layout.addWidget ( generate_button )

        main_layout.addWidget ( scroll )
        self.setLayout ( main_layout )


    def add_offence(self):
        offence = self.offence_input.toPlainText( ).strip( )
        if offence:
            self.offences_list.addItem(offence)
            self.offence_input.clear( )  # Καθαρίζει μετά την προσθήκη

    def generate_documents(self):
        for key,widget in self.inputs.items( ):
            if isinstance(widget,QTextEdit):
                self.context[key] = widget.toPlainText( )
            else:
                self.context[key] = widget.text( )
        self.context['offences'] = [self.offences_list.item(i).text( ) for i in
                                    range(self.offences_list.count( ))]
        witness_report()
        iatrodik()
        deltio_kat()


class Case4Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Αλληλομήνυση")
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
            ("place","Σε ποιο Αστυνομικό Τμήμα?") ,
            ("date_num" ,"Ημερομηνία αριθμητικά?") ,
            ("month" ,"Μήνας?") ,
            ("year" ,"Έτος?") ,
            ("day" ,"Ημέρα?") ,
            ("hour" ,"Ώρα?") ,
            ("first_officer" ,"1ος Ανακριτικός Υπάλληλος?") ,
            ("policeStation" ,"Αστυνομικό Τμήμα?") ,
            ("sec_officer" ,"2ος Ανακριτικός Υπάλληλος?") ,
            ("surname" ,"Επώνυμο?") ,
            ("name" ,"Όνομα?") ,
            ("fathername" ,"Όνομα πατέρα?") ,
            ("mothername" ,"Όνομα μητέρας?") ,
            ("dateOfBirth" ,"Ημερομηνία Γέννησης?") ,
            ("placeOfBirth" ,"Μέρος Γέννησης?") ,
            ("address" ,"Διεύθυνση?") ,
            ("tel" ,"Αριθμός τηλεφώνου?") ,
            ("email" ,"Ηλεκτρονικό Ταχυδρομείο?") ,
            ("DAT" ,"Δ.Α.Τ?") ,
            ("issued" ,"Πότε εκδόθηκε?") ,
            ("place_issued" ,"Που εκδόθηκε?") ,
            ("afm" ,"Αριθμός ΑΦΜ?") ,
            ("doy" ,"Δ.Ο.Υ?") ,
            ("dateOfCrime" ,"Πότε-Ημερομηνία που έγινε το δίκημα?") ,
            ("hourOfCrime" ,"Ακριβής ώρα αδικήματος?") ,
            ("placeOfCrime" ,"Τοποθεσία αδικήματος?") ,
            ("stateOfVictim" ,"Σε ποια κατάσταση βρισκόσουν?") ,
            ("surnamePerperator" ,"Επώνυμο δράστη?") ,
            ("namePerperator" ,"Όνομα δράστη?") ,
            ("fathernamePerperator" ,"Πατρόνυμο δράστη?") ,
            ("mothernamePerperator" ,"Μητρόνυμο δράστη?") ,
            ("dateOfBirthPerperator" ,"Ημερ. γέννησης δράστη?") ,
            ("placeOfBirthPerperator" ,"Τοποθεσία γέννησης δράστη?") ,
            ("addressPerperator" ,"Διεύθυνση δράστη?") ,
            ("telPreperator" ,"Τηλέφωνο δράστη?") ,
            ("emailPreperator" ,"Email δράστη?") ,
            ("DATperperator" ,"Δ.Α.Τ δράστη?") ,
            ("issuedPerperator" ,"Πότε εκδόθηκε ΔΑΤ δράστη?") ,
            ("place_issuedPerperator" ,"Που εκδόθηκε ΔΑΤ δράστη?") ,
            ("afmPreperator" ,"ΑΦΜ δράστη?") ,
            ("doyPrep","ΔΟΥ δράστη?") ,
            ("whatHappened" ,"Τι έγινε?") ,
            ("howHappened" ,"Πώς έγινε?") ,
            ("whyHappened" ,"Γιατί έγινε?") ,
            ("add_something" ,"Θέλεις να προσθέσεις κάτι?") ,
            ("forensicExam" ,"Επιθυμείς ιατροδικαστική εξέταση?") ,
            ("prosecution" ,"Επιθυμείς την ποινική δίωξη του δράστη?") ,
            ("hourOfReportFinished" ,"Τι ώρα τελείωσε η έκθεση μάρτυρα?") ,
            ("protocolnumber" ,"Αριθμός πρωτοκόλλου?") ,
            ("placeOfHurt" ,"Πώς και πού προκλήθηκαν οι σωματικές βλάβες?"),
            ("startTimeArrestReport" , "Ώρα Έναρξης Έκθεσης Σύλληψης?") ,
            ("officer_arrest" , "Αστυνομικός που τον συνέλαβε?") ,
            ("dateOfArrest" , "Ημερομηνία Σύλληψης?") ,
            ("hourOfArrest" , "Ώρα σύλληψης?") ,
            ("placeOfArrest" , "Τοποθεσία σύλληψης?") ,
            ("endTimeOfReport" , "Ώρα Λήξης Έκθεσης Σύλληψης?") ,
            ("date_num_apologia" , "Ημερομηνία αριθμητικά (Απολογία)?") ,
            ("month_apologia" , "Μήνας (Απολογία)?") ,
            ("year_apologia" , "Έτος (Απολογία)?") ,
            ("day_apologia" , "Ημέρα (Απολογία)?") ,
            ("start_hour_apologia" , "Ώρα Έναρξης (Απολογία)?") ,
            ("question_rights_apologia" , "Επιθυμείτε να κάνετε χρήση των δικαιωμάτων?") ,
            ("question_crime_apologia" , "Κατηγορήθηκες άλλη φορά και για ποια αιτία?") ,
            ("question_crime_confess" , "Τι απολογείσαι?") ,
            ("end_hour_apologia" , "Ώρα περάτωσης (Απολογία)?") ,
            ("start_time_rights" , "Ώρα Έναρξης (Δικαιώματα)?") ,
            ("end_time_rights" , "Ώρα περάτωσης (Δικαιώματα)?") ,
            ################
            ('place1','Σε ποιο μέρος;(mutual) '),
            ('date_num1','Ημερομηνία αριθμητικά; '),
            ('month1','Μήνας; '),
            ('day1','Ημέρα;'),
            ('hour1','Ώρα; '),
            ('dateOfCrime1','Ημερομηνία εγκλήματος;'),
            ('hourOfCrime1','Ώρα εγκλήματος;'),
            ('placeOfCrime1','Τοποθεσία εγκλήματος; '),
            ('stateOfVictim1','Κατάσταση θύματος; '),
            ('whatHappened1','Τι έγινε; '),
            ('howHappened1','Πώς έγινε; '),
            ('whyHappened1','Γιατί έγινε;'),
            ('hourOfReportFinished1','Ώρα ολοκλήρωσης έκθεσης; '),
            ('offences1','Αδικήματα ξατά άρθρο π.χ 308 (Σωματικές Βλάβες)'),
            ('placeOfHurt1','Που χτύπησες?'),
            ('startTimeArrestReport1','Ώρα Έναρξης Έκθεσης Σύλληψης?'),
            ('officer_arrest1','Αστυνομικός που τον συνέλαβε? '),
            ('dateOfArrest1',"Ημερομηνία Σύλληψης"),
            ('hourOfArrest1','Ώρα σύλληψης?'),
            ('placeOfArrest1','Τοποθεσία σύλληψης?'),
            ('endTimeOfReport1','Ώρα Λήξης Έκθεσης Σύλληψης?'),
            ('start_time_rights1','Ώρα Έναρξης (Δικαιώματα κατηγορουμένου);'),
            ('end_time_rights1','Ώρα περάτωσης (Δικαιώματα κατηγορουμένου);'),
            ("date_num_apologia1","Ημερομηνία αριθμητικά; "),
            ('month_apologia1 ',"Μήνας (Απολογία); "),
            ('year_apologia1 ',"Έτος (Απολογία); "),
            ('start_hour_apologia1 ',"Ώρα Έναρξης (Απολογία); "),
            ('question_rights_apologia1',
             'Επιθυμείται να κάνετε χρήση των δικαιωμάτων που σας γνωστοποιήθηκαν ;'),
            ('question_crime_apologia1','Κατηγορήθηκες  άλλη φορά και για ποια αιτία ; '),
            ('question_crime_confess1','Κατηγορείσαι ήδη για τις πράξεις που σου γνωστοποιήθηκαν ανωτέρω. '
                                       'Τι απολογείσαι; '),
            ('end_hour_apologia','Ώρα περάτωσης (Απολογία);')

        ]
        for key, label in fields:
            self.inputs[key] = QTextEdit()
            if key in ["place", "date_num", "month", "year", "day", "hour", "first_officer", "policeStation",
                       "sec_officer",
                       "surname", "name", "fathername", "mothername", "dateOfBirth", "placeOfBirth", "address", "tel",
                       "email", "DAT", "issued", "place_issued", "afm", "doy", "dateOfCrime", "hourOfCrime",
                       "placeOfCrime",
                       "surnamePerperator", "namePerperator", "fathernamePerperator", "mothernamePerperator",
                       "dateOfBirthPerperator", "placeOfBirthPerperator", "addressPerperator", "telPreperator",
                       "emailPreperator", "DATperperator", "issuedPerperator", "place_issuedPerperator",
                       "afmPreperator",
                       "doyPrep", "place1", "date_num1", "month1", "yea1r", "day1", "hour1", 'dateOfCrime1',
                       'hourOfCrime1', "placeOfCrime1", 'dateOfArrest1', 'hourOfArrest1', 'placeOfArrest1',
                       'endTimeOfReport1', 'start_time_rights1', 'end_time_rights1', "date_num_apologia1",
                       'month_apologia1', 'year_apologia1', 'start_hour_apologia1', 'question_rights_apologia1',
                       'question_crime_apologia1', 'end_hour_apologia1']:
                self.inputs[key].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            else:
                self.inputs[key].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            form_layout.addRow(QLabel(label), self.inputs[key])

        # Offences section with larger textarea
        offences_layout = QHBoxLayout()
        self.offence_input = QTextEdit()
        self.offence_input.setFixedHeight(100)  # Ομοιόμορφο ύψος
        add_button = QPushButton("Προσθήκη Αδικήματος")
        add_button.clicked.connect(self.add_offence)
        offences_layout.addWidget(self.offence_input)
        offences_layout.addWidget(add_button)
        form_layout.addRow("Αδικήματα:", offences_layout )

        self.offences_list = QListWidget()
        self.offences_list.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list)

        offences_layout1 = QHBoxLayout()
        self.offence_input1 = QTextEdit()
        self.offence_input1.setFixedHeight(100)  # Ομοιόμορφο ύψος
        add_button1 = QPushButton("Προσθήκη Αδικήματος")
        add_button1.clicked.connect(self.add_offence1)
        offences_layout1.addWidget(self.offence_input1)
        offences_layout1.addWidget(add_button1)
        form_layout.addRow("Αδικήματα:",offences_layout1)

        self.offences_list1 = QListWidget()
        self.offences_list1.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list1)

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

    def add_offence1(self):
        offence = self.offence_input1.toPlainText().strip()
        if offence:
            self.offences_list1.addItem(offence)
            self.offence_input1.clear()

    def generate_documents(self):
        for key ,widget in self.inputs.items ( ):
            if isinstance ( widget ,QTextEdit ):
                self.context[key] = widget.toPlainText ( )
            else:
                self.context[key] = widget.text ( )
        self.context['offences'] = [self.offences_list.item ( i ).text ( ) for i in
                                    range ( self.offences_list.count ( ) )]
        mutual()
        iatrodik_mutual()
        silipsi_mutual()
        deltio_kat_mutual()
        apologia_mutual()

'''

class Case4Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Αλληλομήνυση")
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
            ("stateOfVictim", "Σε ποια κατάσταση βρισκόσουν, τι έκανες εκείνη τη στιγμή?"),
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
            ("whatHappened", "Τι έγινε?"),
            ("howHappened", "Πώς έγινε?"),
            ("whyHappened", "Γιατί έγινε?"),
            ("add_something", "Θέλεις να προσθέσεις κάτι?"),
            ("forensicExam", "Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution", "Επιθυμείς την ποινική δίωξη του δράστη?"),
            ("hourOfReportFinished", "Τι ώρα τελείωσε η έκθεση μάρτυρα?"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?"),
            ("placeOfHurt", "Πώς και πού προκλήθηκαν οι σωματικές βλάβες?"),
            ("startTimeArrestReport", "Ώρα Έναρξης Έκθεσης Σύλληψης?"),
            ("officer_arrest", "Αστυνομικός που τον συνέλαβε?"),
            ("dateOfArrest", "Ημερομηνία Σύλληψης?"),
            ("hourOfArrest", "Ώρα σύλληψης?"),
            ("placeOfArrest", "Τοποθεσία σύλληψης?"),
            ("endTimeOfReport", "Ώρα Λήξης Έκθεσης Σύλληψης?"),
            ("date_num_apologia", "Ημερομηνία αριθμητικά (Απολογία)?"),
            ("month_apologia", "Μήνας (Απολογία)?"),
            ("year_apologia", "Έτος (Απολογία)?"),
            ("day_apologia", "Ημέρα (Απολογία)?"),
            ("start_hour_apologia", "Ώρα Έναρξης (Απολογία)?"),
            ("question_rights_apologia", "Επιθυμείτε να κάνετε χρήση των δικαιωμάτων?"),
            ("question_crime_apologia", "Κατηγορήθηκες άλλη φορά και για ποια αιτία?"),
            ("question_crime_confess", "Τι απολογείσαι?"),
            ("end_hour_apologia", "Ώρα περάτωσης (Απολογία)?"),
            ("start_time_rights", "Ώρα Έναρξης (Δικαιώματα)?"),
            ("end_time_rights", "Ώρα περάτωσης (Δικαιώματα)?"),
            # New fields for the second complaint
            ("place1", "Σε ποιο Αστυνομικό Τμήμα (δεύτερο)?"),
            ("date_num1", "Ημερομηνία αριθμητικά (δεύτερο)?"),
            ("month1", "Μήνας (δεύτερο)?"),
            ("year1", "Έτος (δεύτερο)?"),
            ("day1", "Ημέρα (δεύτερο)?"),
            ("hour1", "Ώρα (δεύτερο)?"),
            ("dateOfCrime1", "Πότε-Ημερομηνία που έγινε το δίκημα (δεύτερο)?"),
            ("hourOfCrime1", "Ακριβής ώρα αδικήματος (δεύτερο)?"),
            ("placeOfCrime1", "Τοποθεσία αδικήματος (δεύτερο)?"),
            ("dateOfArrest1", "Ημερομηνία Σύλληψης (δεύτερο)?"),
            ("hourOfArrest1", "Ώρα σύλληψης (δεύτερο)?"),
            ("placeOfArrest1", "Τοποθεσία σύλληψης (δεύτερο)?"),
            ("endTimeOfReport1", "Ώρα Λήξης Έκθεσης Σύλληψης (δεύτερο)?"),
            ("start_time_rights1", "Ώρα Έναρξης (Δικαιώματα - δεύτερο)?"),
            ("end_time_rights1", "Ώρα περάτωσης (Δικαιώματα - δεύτερο)?"),
            ("date_num_apologia1", "Ημερομηνία αριθμητικά (Απολογία - δεύτερο)?"),
            ("month_apologia1", "Μήνας (Απολογία - δεύτερο)?"),
            ("year_apologia1", "Έτος (Απολογία - δεύτερο)?"),
            ("start_hour_apologia1", "Ώρα Έναρξης (Απολογία - δεύτερο)?"),
            ("question_rights_apologia1", "Επιθυμείτε να κάνετε χρήση των δικαιωμάτων (δεύτερο)?"),
            ("question_crime_apologia1", "Κατηγορήθηκες άλλη φορά και για ποια αιτία (δεύτερο)?"),
            ("end_hour_apologia1", "Ώρα περάτωσης (Απολογία - δεύτερο)?"),
            ("add_new_offence", "Προσθήκη Καινούργιου Αδικήματος?"),
        ]
        for key, label in fields:
            self.inputs[key] = QTextEdit()
            if key in ["place", "date_num", "month", "year", "day", "hour", "first_officer", "policeStation", "sec_officer",
                       "surname", "name", "fathername", "mothername", "dateOfBirth", "placeOfBirth", "address", "tel",
                       "email", "DAT", "issued", "place_issued", "afm", "doy", "dateOfCrime", "hourOfCrime", "placeOfCrime",
                       "surnamePerperator", "namePerperator", "fathernamePerperator", "mothernamePerperator",
                       "dateOfBirthPerperator", "placeOfBirthPerperator", "addressPerperator", "telPreperator",
                       "emailPreperator", "DATperperator", "issuedPerperator", "place_issuedPerperator", "afmPreperator",
                       "doyPrep", "place1", "date_num1", "month1", "year1", "day1", "hour1", "dateOfCrime1", "hourOfCrime1",
                       "placeOfCrime1", "dateOfArrest1", "hourOfArrest1", "placeOfArrest1", "endTimeOfReport1", "start_time_rights1",
                       "end_time_rights1", "date_num_apologia1", "month_apologia1", "year_apologia1", "start_hour_apologia1",
                       "question_rights_apologia1", "question_crime_apologia1", "end_hour_apologia1", "add_new_offence"]:
                self.inputs[key].setFixedHeight(30)  # Μικρότερο ύψος για τα προαναφερθέντα ερωτήματα
            else:
                self.inputs[key].setFixedHeight(100)  # Μεγαλύτερο ύψος για τα υπόλοιπα
            form_layout.addRow(QLabel(label), self.inputs[key])

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
        self.context['offences'] = [self.offences_list.item(i).text() for i in range(self.offences_list.count())]

        # Generate first set of documents
        witness_report()
        iatrodik()
        silipsi()
        deltio_kat()
        apologia()
        rights()
        vas()
        transmission()

        # Swap fields for the second complaint
        swap_fields = [
            ("surname", "surnamePerperator"),
            ("name", "namePerperator"),
            ("fathername", "fathernamePerperator"),
            ("mothername", "mothernamePerperator"),
            ("dateOfBirth", "dateOfBirthPerperator"),
            ("placeOfBirth", "placeOfBirthPerperator"),
            ("address", "addressPerperator"),
            ("tel", "telPreperator"),
            ("email", "emailPreperator"),
            ("DAT", "DATperperator"),
            ("issued", "issuedPerperator"),
            ("place_issued", "place_issuedPerperator"),
            ("afm", "afmPreperator"),
            ("doy", "doyPrep"),
        ]
        for field1, field2 in swap_fields:
            self.context[field1], self.context[field2] = self.context[field2], self.context[field1]

        # Update with new fields for the second complaint
        self.context['place'] = self.context.get('place1', self.context['place'])
        self.context['date_num'] = self.context.get('date_num1', self.context['date_num'])
        self.context['month'] = self.context.get('month1', self.context['month'])
        self.context['year'] = self.context.get('year1', self.context['year'])
        self.context['day'] = self.context.get('day1', self.context['day'])
        self.context['hour'] = self.context.get('hour1', self.context['hour'])
        self.context['dateOfCrime'] = self.context.get('dateOfCrime1', self.context['dateOfCrime'])
        self.context['hourOfCrime'] = self.context.get('hourOfCrime1', self.context['hourOfCrime'])
        self.context['placeOfCrime'] = self.context.get('placeOfCrime1', self.context['placeOfCrime'])
        self.context['dateOfArrest'] = self.context.get('dateOfArrest1', self.context['dateOfArrest'])
        self.context['hourOfArrest'] = self.context.get('hourOfArrest1', self.context['hourOfArrest'])
        self.context['placeOfArrest'] = self.context.get('placeOfArrest1', self.context['placeOfArrest'])
        self.context['endTimeOfReport'] = self.context.get('endTimeOfReport1', self.context['endTimeOfReport'])
        self.context['start_time_rights'] = self.context.get('start_time_rights1', self.context['start_time_rights'])
        self.context['end_time_rights'] = self.context.get('end_time_rights1', self.context['end_time_rights'])
        self.context['date_num_apologia'] = self.context.get('date_num_apologia1', self.context['date_num_apologia'])
        self.context['month_apologia'] = self.context.get('month_apologia1', self.context['month_apologia'])
        self.context['year_apologia'] = self.context.get('year_apologia1', self.context['year_apologia'])
        self.context['start_hour_apologia'] = self.context.get('start_hour_apologia1', self.context['start_hour_apologia'])
        self.context['question_rights_apologia'] = self.context.get('question_rights_apologia1', self.context['question_rights_apologia'])
        self.context['question_crime_apologia'] = self.context.get('question_crime_apologia1', self.context['question_crime_apologia'])
        self.context['end_hour_apologia'] = self.context.get('end_hour_apologia1', self.context['end_hour_apologia'])

        # Generate second set of documents
        witness_report()
        iatrodik()
        silipsi()
        deltio_kat()
        apologia()
        rights()
        vas()
        transmission()
'''