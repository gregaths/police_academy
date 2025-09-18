from PyQt5.QtWidgets import ( QWidget, QVBoxLayout,  QTextBrowser)

class Relevent(QWidget):
    def __init__(self):
        super( ).__init__( )
        self.setWindowTitle( "Σχετικά" )
        self.setGeometry( 200 , 200 , 600 , 400 )

        layout = QVBoxLayout( )
        bio_text = QTextBrowser( )
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
            <h1 style="color:blue;">Plhroforiw</h1>
        </body>
        </html>
        """
