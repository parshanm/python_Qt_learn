# imports:
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
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

        # adding a button:
        self.btn = QPushButton(self)
        self.btn.setText("Click me!")
        self.btn.setGeometry(100, 10, 100, 30)

        # connecting button to function:
        self.btn.clicked.connect(self.on_click)

        # showing window:
        self.show()

    def on_click(self):
        print("Hello,I'm a button!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())
