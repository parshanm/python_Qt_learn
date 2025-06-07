# import:
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# create a app
app = QApplication([])

# create a window
window = QWidget()

# set a title:
window.setWindowTitle("My first app")

# show this window
window.show()

# keep window on screen
sys.exit(app.exec())
