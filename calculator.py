from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic


class MyGui(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculator.ui", self)
        self.screen.setText("")
        self.show()

        #რიცხვების კლავიშები
        self.pushButton_0.clicked.connect(lambda: self.update_screen("0"))
        self.pushButton_1.clicked.connect(lambda: self.update_screen("1"))
        self.pushButton_2.clicked.connect(lambda: self.update_screen("2"))
        self.pushButton_3.clicked.connect(lambda: self.update_screen("3"))
        self.pushButton_4.clicked.connect(lambda: self.update_screen("4"))
        self.pushButton_5.clicked.connect(lambda: self.update_screen("5"))
        self.pushButton_6.clicked.connect(lambda: self.update_screen("6"))
        self.pushButton_7.clicked.connect(lambda: self.update_screen("7"))
        self.pushButton_8.clicked.connect(lambda: self.update_screen("8"))
        self.pushButton_9.clicked.connect(lambda: self.update_screen("9"))
        #სხვა კლავიშები
        self.pushButton_point.clicked.connect(lambda: self.update_screen("."))
        self.pushButton_plus.clicked.connect(lambda: self.update_screen("+"))
        self.pushButton_minus.clicked.connect(lambda: self.update_screen("-"))
        self.pushButton_multiply.clicked.connect(lambda: self.update_screen("*"))
        self.pushButton_divide.clicked.connect(lambda: self.update_screen("/"))
        #გასუფთავების კლავიში
        self.pushButton_clear.clicked.connect(lambda: self.screen.setText(""))
        #ტოლობის კლავიში
        self.pushButton_equels.clicked.connect(lambda: self.calculate(self.screen.text()))




    def update_screen(self, info):
        new_text = self.screen.text() + info
        self.screen.setText(new_text)

    def calculate(self, problem):
        try:
            answer = str(eval(problem))
        except:
            answer = "Mistake!"
        self.screen.setText(answer)



def main():
    app = QApplication([])
    window = MyGui()
    window.setWindowTitle("Calculator")

    app.setStyleSheet("""
    #logo {
        font-size: 30px;
        color: #93deed;
    }
    #screen {
        font-size: 30px;
        color: #93deed;
    }
    #Dialog {
        background-color: rgb(80, 80, 80);
    }
    #pushButton_equels {
        font-size: 20px;
        background-color: rgb(255, 180, 120);
        border-radius: 10px;
    }
    #pushButton_plus {
        font-size: 20px;
        background-color: rgb(255, 180, 120);
        border-radius: 10px;
    }
    #pushButton_minus {
        font-size: 20px;
        background-color: rgb(255, 180, 120);
        border-radius: 10px;
    }
    #pushButton_multiply {
        font-size: 20px;
        background-color: rgb(255, 180, 120);
        border-radius: 10px;
    }
    #pushButton_divide {
        font-size: 20px;
        background-color: rgb(255, 180, 120);
        border-radius: 10px;
    }
    #pushButton_point {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_0 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_1 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_2 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_3 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_4 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_5 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_6 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_7 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_8 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_9 {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    #pushButton_clear {
        font-size: 30px;
        background-color: rgb(255, 255, 255);
        border-radius: 10px;
    }
    
    
    """)

    app.exec_()

if __name__ == "__main__":
    main()