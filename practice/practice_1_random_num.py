# imports:
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from random import randint


class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window:
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("random number")
        # setting Icon
        self.setWindowIcon(QIcon("icon.jpg"))

        # adding a label: (without any text)
        self.lbl = QLabel(self)
        self.lbl.setGeometry(115, 50, 100, 40)

        
        # adding a button:
        self.btn = QPushButton(self)
        self.btn.setText("Pick a number")
        self.btn.setGeometry(100,10, 100,30)

        # connect button to function:
        self.btn.clicked.connect(self.pick_number)

        # showing window:
        self.show()

    def pick_number(self):
        # generate a random number:
        num = randint(20, 100)
        # show the number:
        self.lbl.setText(f'{num}')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())
