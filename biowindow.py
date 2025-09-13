
from PyQt5.QtWidgets import ( QWidget, QVBoxLayout,  QTextBrowser)


class BioWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Βιογραφικό - Αθανασιάδης Γρηγόριος")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()
        bio_text = QTextBrowser()
        bio_html = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #2c3e50; }
                p { line-height: 1.6; }
            </style>
        </head>
        <body>
            <h1 style="color:blue;">Βιογραφικό - Αθανασιάδης Γρηγόριος</h1>
            <p align="center">Ο Αθανασιάδης Γρηγόριος είναι Υπαστυνόμος Α στο Αστυνομικό Τμήμα Θέρμης Θεσσαλονίκης,
             με πολυετή εμπειρία.</p>
            <p><strong>Ακαδημαική Εκπαίδευση:</strong> 
            <ol>
                  <li style="color:blue;"> Πτυχίο Πληροφορικής, Ε.Α.Π.</li>
                  <li style="color:blue;">Μεταπτυχιακός Τίτλος Σπουδών <br>Υπολογιστική Νοημοσύνη και<br>
                   Ψηφιακά Μέσα-Α.Π.Θ</li>
                </ol>
             <p><strong>Μετεκπαίδευση:</strong> 
             <ol>
             <li style="color:blue;">Google Cybersecurity Specialization <br>Coursera</li>
             <li style="color:blue;">100 Days of Code: The Complete Python Pro Bootcamp - 
            <br> Dr. Angela Yu -UDEMY</li>
             <li style="color:blue;">Machine Learning A-Z: AI, Python & R + ChatGPT<br> Kirill Eremenko -UDEMY</li>
             <li style="color:blue;">Complete Guide to TensorFlow for Deep Learning with Python
              <br>Jose Portilla-UDEMY</li>
              <li style="color:blue;">Master Computer Vision™ OpenCV4 in Python with Deep Learning
              Master Computer Vision™ OpenCV4 like a pro while learning Dlib, Deep Learning Computer Vision <br>
              (Keras, TensorFlow & Caffe) + 21 Projects! -UDEMY</li>
              <li style="color:blue;">Face Detection -Master Open CV with Digital Image Processing<br> UDEMY
              
</li>
             </ol>
            
           </p>
            <p><strong>Εργασιακή Εμπειρία:</strong> 29 χρόνια στην αστυνομία </p>
            <p><strong>Επικοινωνία:</strong> g.athanasidis@astynomia.gr</p>
        </body>
        </html>
        """
        bio_text.setHtml(bio_html)
        layout.addWidget(bio_text)
        self.setLayout(layout)