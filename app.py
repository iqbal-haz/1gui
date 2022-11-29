from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget, QPushButton
import os
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)
        self.options = ('ASR', 'OCR', 'ZSC')

        self.dropdown = QComboBox()
        self.dropdown.addItems(self.options)
        layout.addWidget(self.dropdown)

        self.button = QPushButton('Launch')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.launch)

    def launch(self):
        option = self.dropdown.currentText()
        if option == "ASR":
            os.system("./asr.sh")
        elif option == "OCR":
            os.system("./ocr.sh")
        elif option == "ZSC":
            os.system("./zsc.sh")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    app.exec()