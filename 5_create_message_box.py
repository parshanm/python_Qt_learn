# imports:
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon


class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window:
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("My Window")
        # setting Icon
        self.setWindowIcon(QIcon("icon.jpg"))

        #adding a push button
        self.btn = QPushButton(self)
        self.btn.setText("Click me!")
        self.btn.setGeometry(100, 10, 100, 30)

        #connect button to a function
        self.btn.clicked.connect(self.message_box)

        # showing window:
        self.show()

    def message_box(self):
        msg = QMessageBox.question(
        self,
        'Title',
        'questation',
        # adding buttons (optional)
        QMessageBox.Ok,
        QMessageBox.No)

        # check the answer:
        if msg == QMessageBox.No:
            exit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())