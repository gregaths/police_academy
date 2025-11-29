from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTextBrowser)


class cv2g(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Βιογραφικό")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()
        bio_text = QTextBrowser()
        bio_html = """
       <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Grigoris Athanasiadis</title>
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic|Open+Sans:300,400,500,700|
    Waiting+for+the+Sunrise|Shadows+Into+Light' rel='stylesheet' type='text/css'>
     <link rel="stylesheet" href="styles.css" />
</head>
<body>
    <div class="wrapper clearfix">
  <div class="left">

    <div class="name-hero">

      <div class="me-img"></div>

      <div class="name-text">

        <h1>Γρηγόρης <em>Αθανασιάδης</em></h1>
        <p>Υπαστυνόμος Α</p>
        <p>Αστυνομικό Τμήμα Θέρμης</p>
        <p>g.athanasiadis@astynomia.gr</p>

      </div>

    </div>

  </div>
  <div class="right">

    <div class="inner">
      <section>
        <h1>Εργασιακή εμπειρία</h1>
        <p>Από το 2018 αρχικά με απόσπαση και πλέον με μετάθεση εργάζομαι στο Αστυνομικό Τμήμα
          Θέρμης. Στο  συγκεκριμένο  Αστυνομικό Τμήμα  κυρίως  τα πρώτα  πέντε χρόνια  εργάστηκα ως Αξιωματικός  Υπηρεσίας.</p>
        <p> Επίσης έχω εργαστεί στο Τμήμα Δίωξης και Εξιχνίασης Εγκλημάτων Δράμας, στην Διεύθυνση Προστασίας Επισήμων προσώπων,
          στο Αστυνομικό Τμήμα Προσοτσάνης Δράμας, στο Αστυνομικό Τμήμα Καρουσάδων Κέρκυρας, στη Διευθυνση Άμεσης Δράσης Αττικής,στο Αστυνομικό Τμήμα Νέου Ψυχικού,
          στο Αστυνομικό Τμήμα Πάρου, στο Αστυνομικό Τμήμα Χαλανδρίου, στην Υποδιεύθυνση Αστυνομίας Αερολιμένα Κέρκυρας,
          στο Αστυνομικό Τμήμα Παλαιού Ψυχικού, στο Αστυνομικό Τμήμα Χολαργού.</p>
      </section>
      <section>
        <h1>Ακαδημαική Εκπαίδευση</h1>
        <p>1996-1998| <em>Σχολή Αστυφυλάκων Αστυνομίας | Τ.Δ.Α Ξάνθης</em></p>
        <p>2011-2015 |<em>Πτυχίο | Πληροφορική | Τμήμα Πληροφορικής Ε.Α.Π</em></p>
        <p><em>Πτυχιακή Εργασία: Πρόβλεψη αγώνων ποδοσφαίρου με χρήση αλγορίθμων Μηχανικής Μάθησης</em></p>
        <p>2016-2018| <em>Μεταπτυχιακό | Υπολογιστική Νοημοσύνη και Ψηφιακά Μέσα | Τμήμα Πληροφορικής Α.Π.Θ</em></p>
         <p><em>Διπλωματική Εργασία: Τεχνικές ανάλσης ηλεκτροεγκεφαλογραφήματος για Διεπαφή εγκεφάλου με
         υπολογιστή με στόχο την ανίχνευση του ερεθίσματος που αντιστοιχεί στην έναρξη λειτουργίας των φώτων
         φρένων του προπορευόμενου οχήματος</em></p>

      </section>

      <section>
        <h1>Επιπρόσθετες επιμορφώσεις</h1>
        <ol>
             <li>Google Cybersecurity Specialization - COURSERA</li>
          <li>Introduction to Cybersecurity -CISCO</li>
            <li>Machine Lerning by Andrew NG - COURSERA</li>
          <li>AI engineer core track: LLM engineering, RAG, QLoRA Agents -
            Ed Donner -UDEMY</li>
             <li >100 Days of Code: The Complete Python Pro Bootcamp -
             -  Dr. Angela Yu -UDEMY</li>
             <li >Machine Learning A-Z: AI, Python & R + ChatGPT- Kirill Eremenko -UDEMY</li>
            <li>Deep Learning A-Z 2025: Neural Networks, AI & ChatGPT Prize - Kirill Eremenko -UDEMY</li>
             <li>Complete Guide to TensorFlow for Deep Learning with Python
              -Jose Portilla-UDEMY</li>
            <li>Learn Neural Networks using Matlab Programming - Hossein Technology -UDEMY</li>
            <li>Digital Signal Processing with MATLAB- Hossein Technology -UDEMY</li>
             <li>Master Computer Vision™ OpenCV4 in Python with Deep Learning
              Master Computer Vision™ OpenCV4 like a pro while learning Dlib, Deep Learning Computer Vision <br>
              (Keras, TensorFlow & Caffe) + 21 Projects! -UDEMY</li>
            <li>Cluster Analysis and Unsupervised Machine Learning in Python - The lazy programmer -UDEMY</li>
            <li>Face Detection -Master Open CV with Digital Image Processing- UDEMY</li>
            <li>Become a WordPress Developer: Unlocking Power With Code - Brad Schiff -UDEMY</li>
            <li>Learn and understand C++ - Ermin Kreponic- UDEMY</li>
            <LI>The complete web developer course 3.0 -Rob Percival -UDEMY</LI>
               <li>Darkweb - CEPOL</li>
          <li>Cybercrime - CEPOL</li>
            <li>Εκπαίδευση σημείων επαφής για το κυβερνοέγκλημα - Persons of contact (POC) on Cybercrime (series of 4 webinars)-Διεύθυνση Δίωξης Ηλεκτρονικού Εγκλήματος</li>
            <li>Impact of the use of AI technology in the field of internal
security: threats, opportunities, and outlooks for European LE - CEPOL</li>
             </ol>

      </section>

      <section>
        <h1>Technical Skills</h1>
        <ul class="skill-set">
          <li>Web Development</li>
          <li>Python</li>
          <li>Java</li>
          <li>Machine Learning</li>
          <li>Deep Learning</li>
          <li>Artificial Intelligence Agents</li>
          <li>HTML5</li>
          <li>CSS3</li>
          <li>JQUERY</li>
          <li>UI Design</li>
          <li>Responsive Web Design</li>
          <li>C++</li>
          <li>Javascript</li>
          <li>Matlab</li>
        </ul>
      </section>

      <section>
        <h1>Personal Interests</h1>
        <ul class="skill-set">
          <li>Good music</li>
          <li>Playing Basketball</li>
          <li>Reading</li>
        </ul>
      </section>
      <section>
        <div class="handmade">
          <p>handmade by <em> Grigoris Athanasiadis</em></p>
        </div>
      </section>
    </div>

  </div>

</div>

</body>
</html>
       
       
        """
        bio_text.setHtml(bio_html)
        layout.addWidget(bio_text)
        self.setLayout(layout)