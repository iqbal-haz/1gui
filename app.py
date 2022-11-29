from PyQt5.QtCore import QRunnable, QThreadPool
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget, QPushButton
import os
import sys
import time

class Service(QRunnable):
    def __init__(self, script: str):
        super().__init__()
        self.script = script

    def run(self):
        os.system(f"./{self.script}")
        time.sleep(1)


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
        self.seed()

        self.button = QPushButton('Launch')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.launch)

    def launch(self):
        option = self.dropdown.currentText()
        pool = QThreadPool.globalInstance()
        service = {
            "OCR": self.services['OCR'],
            "ASR": self.services['ASR'],
            "ZSC": self.services['ZSC']
        }[option]
        pool.start(service)

    def seed(self):
        ocr = Service('ocr.sh')
        asr = Service('asr.sh')
        zsc = Service('zsc.sh')
        self.services = {
            "OCR": ocr,
            "ASR": asr,
            "ZSC": zsc
        }

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())