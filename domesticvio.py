from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFormLayout, QTextEdit, QListWidget, QHBoxLayout, QScrollArea)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from documents import (witness_report, silipsi, deltio_kat, apologia, rights, vas, transmission,
                       mutual,  silipsi_mutual, deltio_kat_mutual, apologia_mutual,  witness_report_adjudication,
                       transmission_adjudication, iatrodik, iatrodik_mutual,  context)
from documents2 import witness_domestic, witness_domestic_mutual, panic_button, panic_button_mutual
import os
import sys
from lawwindow import DomesticLaw


class DomesticVioWindow(QWidget):
    def __init__(self, parent_window=None):
        super().__init__()
        self.parent_window = parent_window
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
            "<center>Software Developer<br>Αθανάσιος Γρηγόριος<br>Υπαστυνόμος Α<br>"
            "Αστυνομικό Τμήμα Θεσσαλονίκης<br>Διεύθυνση Αστυνομίας Θεσσαλονίκης<br>Version 2.0<br>"
            "© 2025 All Rights Reserved</center>"
        )
        programmer_info.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(programmer_info)
        main_layout.addLayout(left_layout, 1)

        # Right side: Options for bodily harm
        right_layout = QVBoxLayout()
        options = [
            "1. Μήνυση χωρίς σύλληψη",
            "2. Μήνυση με γνωστό δράστη και σύλληψη",
            "3.  Αλληλομήνυση",
            "4. Νομοθεσία Περί Ενδοοικογενειακής Βίας",
            "5. ← Πίσω"

        ]
        for option in options:
            button = QPushButton(option)
            button.setFixedSize(280, 60)
            if option == "1. Μήνυση χωρίς σύλληψη":
                button.clicked.connect(self.open_case_1)
            elif option == "2. Μήνυση με γνωστό δράστη και σύλληψη":
                button.clicked.connect(self.open_case_2)
            elif option == "3.  Αλληλομήνυση":
                button.clicked.connect(self.open_case_3a)
            elif option == "4. Νομοθεσία Περί Ενδοοικογενειακής Βίας":
                button.clicked.connect( self.open_case_4 )
            elif option == "5. ← Πίσω":
                button.clicked.connect(self.open_case_5)
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
        self.case_2_window = Case2Window( )
        self.case_2_window.show( )
        self.hide( )

    def open_case_3a(self):
        self.case_3a_window = Case3Window( )
        self.case_3a_window.show( )
        self.hide( )

    def open_case_4(self):
        self.case_4_window = DomesticLaw()
        self.case_4_window.show()
        self.hide()

    def open_case_5(self):
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
        self.setWindowTitle("Μήνυση χωρίς σύλληψη")
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
            ("dateOfCrime", "Ημερομηνία εγκλήματος?"),
            ("hourOfCrime", "Ώρα εγκλήματος?"),
            ("placeOfCrime", "Τοποθεσία εγκλήματος?"),
            ("stateOfVictim", "σύζυγος/πρώην σύζυγος/<br>σύντροφος/πρώην σύντροφος"),
            ("whatHappened", "Τι έγινε?"),
            ("howHappened", "Πως έγινε?"),
            ("whyHappened", "Γιατι έγινε?"),
            ("add_something", "Πρόσθεσε κάτι"),
            ("forensicExam", "Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution", "Επιθυμείς την ποινική δίωξη?"),
            ("questionPast", "Έχουν υπάρξει ανάλογα περιστατικά στο παρελθόν;"),
            ("questionGun", "Είναι ο/η σύζυγός σας κάτοχος κάποιου όπλου;"),
            ("safehouse", "Επιθυμείτε να ενημερώσουμε κάποια δομή παροχής <br>"
                          "αρωγής σε θύματα ενδοοικογενειακής βίας και να σας <br>"
                          "μεταφέρουμε σε κάποιο ασφαλές κατάλυμα;"),
            ("transferHouse", "Επιθυμείτε να σας μεταφέρουμε στην οικία σας;"),
            ("transferForensic", "Επιθυμείτε να σας μεταφέρουμε <br>στην Ιατροδικαστική Υπηρεσία;"),
            ("QuestionAdd", "Έχετε κάτι άλλο να προσθέσετε;"),
            ("hourOfReportFinished", "Τι ώρα τελείωσε η μήνυση?"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?")


        ]

        for key, label in fields:
            self.inputs[ key ] = QTextEdit()
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
        form_layout.addRow("Αδικήματα:",offences_layout)

        self.offences_list=QListWidget()
        self.offences_list.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list)

        # Generate button
        generate_button=QPushButton("Δημιουργία Εγγράφων")
        generate_button.clicked.connect(self.generate_documents)
        main_layout.addWidget(generate_button)

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def add_offence(self):
        offence=self.offence_input.toPlainText().strip()
        if offence:
            self.offences_list.addItem(offence)
            self.offence_input.clear()  # Καθαρίζει μετά την προσθήκη

    def generate_documents(self):
        for key,widget in self.inputs.items():
            if isinstance(widget,QTextEdit):
                self.context[key]=widget.toPlainText()
            else:
                self.context[key]=widget.text()
        self.context['offences']=[self.offences_list.item(i).text() for i in
                                  range(self.offences_list.count())]
        witness_domestic()
        iatrodik()
        deltio_kat()
        vas()




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
            ("dateOfCrime", "Ημερομηνία εγκλήματος?"),
            ("hourOfCrime", "Ώρα εγκλήματος?"),
            ("placeOfCrime", "Τοποθεσία εγκλήματος?"),
            ("stateOfVictim", "σύζυγος/πρώην σύζυγος/<br>σύντροφος/πρώην σύντροφος"),
            ("whatHappened", "Τι έγινε?"),
            ("howHappened", "Πως έγινε?"),
            ("whyHappened", "Γιατι έγινε?"),
            ("add_something", "Πρόσθεσε κάτι"),
            ("forensicExam", "Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution", "Επιθυμείς την ποινική δίωξη?"),
            ("questionPast", "Έχουν υπάρξει ανάλογα περιστατικά στο παρελθόν;"),
            ("questionGun", "Είναι ο/η σύζυγός σας κάτοχος κάποιου όπλου;"),
            ("safehouse", "Επιθυμείτε να ενημερώσουμε κάποια δομή παροχής <br>"
                          "αρωγής σε θύματα ενδοοικογενειακής βίας και να σας <br>"
                          "μεταφέρουμε σε κάποιο ασφαλές κατάλυμα;"),
            ("transferHouse", "Επιθυμείτε να σας μεταφέρουμε στην οικία σας;"),
            ("transferForensic", "Επιθυμείτε να σας μεταφέρουμε <br>στην Ιατροδικαστική Υπηρεσία;"),
            ("QuestionAdd", "Έχετε κάτι άλλο να προσθέσετε;"),
            ("hourOfReportFinished", "Τι ώρα τελείωσε η μήνυση?"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?"),
            ("startTimeArrestReport", "Ώρα Έναρξης Έκθεσης Σύλληψης?"),
            ("officer_arrest", "Αστυνομικός που τον συνέλαβε?"),
            ("dateOfArrest", "Ημερομηνία Σύλληψης?"),
            ("hourOfArrest", "Ώρα σύλληψης?"),
            ("placeOfArrest", "Τοποθεσία σύλληψης?"),
            ("endTimeOfReport", "Ώρα Λήξης Έκθεσης Σύλληψης?"),
            ("start_time_rights", "Ώρα Έναρξης (Δικαιώματα)?"),
            ("end_time_rights", "Ώρα περάτωσης (Δικαιώματα)?"),
            ("date_num_apologia", "Ημερομηνία αριθμητικά (Απολογία)?"),
            ("month_apologia", "Μήνας (Απολογία)?"),
            ("year_apologia", "Έτος (Απολογία)?"),
            ("day_apologia", "Ημέρα (Απολογία)?"),
            ("start_hour_apologia", "Ώρα Έναρξης (Απολογία)?"),
            ("question_rights_apologia", "Επιθυμείτε να κάνετε χρήση των δικαιωμάτων?"),
            ("question_crime_apologia", "Κατηγορήθηκες άλλη φορά και για ποια αιτία?"),
            ("question_crime_confess", "Τι απολογείσαι?"),
            ("end_hour_apologia", "Ώρα περάτωσης (Απολογία)?")


        ]

        for key, label in fields:
            self.inputs[ key ] = QTextEdit()
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
        form_layout.addRow("Αδικήματα:",offences_layout)

        self.offences_list=QListWidget()
        self.offences_list.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list)

        # Generate button
        generate_button=QPushButton("Δημιουργία Εγγράφων")
        generate_button.clicked.connect(self.generate_documents)
        main_layout.addWidget(generate_button)

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def add_offence(self):
        offence=self.offence_input.toPlainText().strip()
        if offence:
            self.offences_list.addItem(offence)
            self.offence_input.clear()  # Καθαρίζει μετά την προσθήκη

    def generate_documents(self):
        for key,widget in self.inputs.items():
            if isinstance(widget,QTextEdit):
                self.context[key]=widget.toPlainText()
            else:
                self.context[key]=widget.text()
        self.context['offences']=[self.offences_list.item(i).text() for i in
                                  range(self.offences_list.count())]
        witness_domestic()
        iatrodik()
        silipsi()
        deltio_kat()
        apologia()
        rights()
        panic_button()
        vas()


class Case3Window(QWidget):
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
            ("dateOfCrime", "Ημερομηνία εγκλήματος?"),
            ("hourOfCrime", "Ώρα εγκλήματος?"),
            ("placeOfCrime", "Τοποθεσία εγκλήματος?"),
            ("stateOfVictim", "σύζυγος/πρώην σύζυγος/<br>σύντροφος/πρώην σύντροφος"),
            ("whatHappened", "Τι έγινε?"),
            ("howHappened", "Πως έγινε?"),
            ("whyHappened", "Γιατι έγινε?"),
            ("add_something", "Πρόσθεσε κάτι"),
            ("forensicExam", "Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution", "Επιθυμείς την ποινική δίωξη?"),
            ("questionPast", "Έχουν υπάρξει ανάλογα περιστατικά στο παρελθόν;"),
            ("questionGun", "Είναι ο/η σύζυγός σας κάτοχος κάποιου όπλου;"),
            ("safehouse", "Επιθυμείτε να ενημερώσουμε κάποια δομή παροχής <br>"
                          "αρωγής σε θύματα ενδοοικογενειακής βίας και να σας <br>"
                          "μεταφέρουμε σε κάποιο ασφαλές κατάλυμα;"),
            ("transferHouse", "Επιθυμείτε να σας μεταφέρουμε στην οικία σας;"),
            ("transferForensic", "Επιθυμείτε να σας μεταφέρουμε <br>στην Ιατροδικαστική Υπηρεσία;"),
            ("QuestionAdd", "Έχετε κάτι άλλο να προσθέσετε;"),
            ("hourOfReportFinished", "Τι ώρα τελείωσε η μήνυση?"),
            ("protocolnumber", "Αριθμός πρωτοκόλλου?"),
            ("startTimeArrestReport", "Ώρα Έναρξης Έκθεσης Σύλληψης?"),
            ("officer_arrest", "Αστυνομικός που τον συνέλαβε?"),
            ("dateOfArrest", "Ημερομηνία Σύλληψης?"),
            ("hourOfArrest", "Ώρα σύλληψης?"),
            ("placeOfArrest", "Τοποθεσία σύλληψης?"),
            ("endTimeOfReport", "Ώρα Λήξης Έκθεσης Σύλληψης?"),
            ("start_time_rights", "Ώρα Έναρξης (Δικαιώματα)?"),
            ("end_time_rights", "Ώρα περάτωσης (Δικαιώματα)?"),
            ("date_num_apologia", "Ημερομηνία αριθμητικά (Απολογία)?"),
            ("month_apologia", "Μήνας (Απολογία)?"),
            ("year_apologia", "Έτος (Απολογία)?"),
            ("day_apologia", "Ημέρα (Απολογία)?"),
            ("start_hour_apologia", "Ώρα Έναρξης (Απολογία)?"),
            ("question_rights_apologia", "Επιθυμείτε να κάνετε χρήση των δικαιωμάτων?"),
            ("question_crime_apologia", "Κατηγορήθηκες άλλη φορά και για ποια αιτία?"),
            ("question_crime_confess", "Τι απολογείσαι?"),
            ("end_hour_apologia", "Ώρα περάτωσης (Απολογία)?"),
            ############################
            ("hour1", "Ώρα σύνταξης έκθεσης? (αλληλομήνυση)"),
            ("dateOfCrime1", "Ημερομηνία εγκλήματος?"),
            ("hourOfCrime1", "Ώρα εγκλήματος?"),
            ("placeOfCrime1", "Τοποθεσία εγκλήματος?"),
            ("stateOfVictim1", "σύζυγος/πρώην σύζυγος/<br>σύντροφος/πρώην σύντροφος"),
            ("whatHappened1", "Τι έγινε?"),
            ("howHappened1", "Πως έγινε?"),
            ("whyHappened1", "Γιατι έγινε?"),
            ("add_something1", "Πρόσθεσε κάτι"),
            ("forensicExam1", "Επιθυμείς ιατροδικαστική εξέταση?"),
            ("prosecution1", "Επιθυμείς την ποινική δίωξη?"),
            ("questionPast1", "Έχουν υπάρξει ανάλογα περιστατικά στο παρελθόν;"),
            ("questionGun1", "Είναι ο/η σύζυγός σας κάτοχος κάποιου όπλου;"),
            ("safehouse1", "Επιθυμείτε να ενημερώσουμε κάποια δομή παροχής <br>"
                          "αρωγής σε θύματα ενδοοικογενειακής βίας και να σας <br>"
                          "μεταφέρουμε σε κάποιο ασφαλές κατάλυμα;"),
            ("transferHouse1", "Επιθυμείτε να σας μεταφέρουμε στην οικία σας;"),
            ("transferForensic1", "Επιθυμείτε να σας μεταφέρουμε <br>στην Ιατροδικαστική Υπηρεσία;"),
            ("QuestionAdd1", "Έχετε κάτι άλλο να προσθέσετε;"),
            ("hourOfReportFinished1", "Τι ώρα τελείωσε η μήνυση?")


        ]

        for key, label in fields:
            self.inputs[ key ] = QTextEdit()
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
        form_layout.addRow("Αδικήματα:",offences_layout)

        self.offences_list=QListWidget()
        self.offences_list.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list)

        offences_layout1 = QHBoxLayout()
        self.offence_input1 = QTextEdit()
        self.offence_input1.setFixedHeight(100)  # Ομοιόμορφο ύψος
        add_button1 = QPushButton("Προσθήκη Αδικήματος")
        add_button1.clicked.connect(self.add_offence1)
        offences_layout1.addWidget(self.offence_input1)
        offences_layout1.addWidget(add_button1)
        form_layout.addRow("Αδικήματα:", offences_layout1)

        self.offences_list1 = QListWidget()
        self.offences_list1.setFixedHeight(150)  # Εμφάνιση αδικημάτων
        form_layout.addRow(self.offences_list1)

        # Generate button
        generate_button=QPushButton("Δημιουργία Εγγράφων")
        generate_button.clicked.connect(self.generate_documents)
        main_layout.addWidget(generate_button)

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    def add_offence(self):
        offence=self.offence_input.toPlainText().strip()
        if offence:
            self.offences_list.addItem(offence)
            self.offence_input.clear()  # Καθαρίζει μετά την προσθήκη

    def add_offence1(self):
        offence = self.offence_input1.toPlainText().strip()
        if offence:
            self.offences_list1.addItem(offence)
            self.offence_input1.clear()

    def generate_documents(self):
        for key,widget in self.inputs.items():
            if isinstance(widget,QTextEdit):
                self.context[key]=widget.toPlainText()
            else:
                self.context[key]=widget.text()
        self.context['offences']=[self.offences_list.item(i).text() for i in
                                  range(self.offences_list.count())]
        witness_domestic()
        iatrodik()
        silipsi()
        deltio_kat()
        apologia()
        rights()
        panic_button()
        witness_domestic_mutual()
        iatrodik_mutual()
        silipsi_mutual()
        deltio_kat_mutual()
        apologia_mutual()
        panic_button_mutual()



class Case4Window(QWidget):
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

