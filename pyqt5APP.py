from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

#pip install pyqt5-tools
#G:\YouTube\Videos\venv\Lib\site-packages\qt5_applications\Qt\bin



class MyGui(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("app2.ui", self)
        self.show()

        self.enterPushButton.clicked.connect(self.login)
        self.countPushButton.clicked.connect(lambda: self.onclick(self.textEdit.toPlainText()))
        self.clearPushButton.clicked.connect(self.clear)



    def login(self):
        if self.userLineEdit.text() == "Nika2023" and self.passwordLineEdit.text() == "Pass23":
            self.textEdit.setEnabled(True)
            self.countPushButton.setEnabled(True)
            self.clearPushButton.setEnabled(True)

        else:
            message = QMessageBox()
            message.setText(f"Incorrect Username or Password!")
            message.exec_()

    def onclick(self, msg):
        self.finalresult.setText(str(len(msg)))

    def clear(self):
        self.textEdit.setText("")



def main():
    app = QApplication([])
    window = MyGui()
    window.setWindowTitle("Counter")
    app.exec_()


if __name__ == "__main__":
    main()