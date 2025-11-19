# imports:
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel,QPushButton, QMessageBox
from PyQt5.QtGui import QIcon


class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # window:
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("login Window")
        # setting Icon
        self.setWindowIcon(QIcon("icon.jpg"))

        self.title = QLabel(self, text='login page')
        self.title.setGeometry(180,10,50,20)

        #adding a line edit (input)
        self.sub_title1 = QLabel(self, text='name')
        self.sub_title1.setGeometry(180,35,50,20)
        self.line1 = QLineEdit(self)
        #place it:
        self.line1.move(140, 55)

        #adding a line edit (input)
        self.sub_title2 = QLabel(self, text='last name')
        self.sub_title2.setGeometry(180,75,50,20)
        self.line2 = QLineEdit(self)
        #place it:
        self.line2.move(140, 95)

        #add a btn:
        self.btn = QPushButton(parent=self, text='submit')
        self.btn.clicked.connect(self.submit)
        self.btn.move(165, 125)

        # showing window:
        self.show()

    def submit(self):
        name = self.line1.text()
        last = self.line2.text()
        QMessageBox.information(self,'hi', f'hello {name} {last}')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())
