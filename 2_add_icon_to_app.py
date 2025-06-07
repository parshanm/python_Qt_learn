# imports:
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #window:
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('My Window')
        # setting Icon
        self.setWindowIcon(QIcon('icon.jpg'))

        # showing window:
        self.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())

