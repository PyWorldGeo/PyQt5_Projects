#pip install pyqt5-tools

# აპლიკაციისთვის საჭირო მოდულების შემოტანა
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()

    window.setGeometry(100, 100, 500, 500)
    window.setWindowTitle("Counter")

    layout = QVBoxLayout()

    label = QLabel("Enter Text Below:")
    label.setFont(QFont("Arial", 16))

    #ტექსტის შემყვანი ელემენტის შექმნა
    textbox = QTextEdit()
    textbox.setFont(QFont("Arial", 16))

    button = QPushButton("Run Counter!")
    button.clicked.connect(lambda: on_click(textbox.toPlainText()))
    #ღილაკის სიმაღლის რეგულირება
    button.setMinimumHeight(50)
    #ღილაკის წარწერის ზომა
    button.setFont(QFont("Arial", 16))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec_()


def on_click(msg):
    # მესიჯის ყუთის შექმნა
    message = QMessageBox()
    #მესიჯის ყუთში ინფოს გამოტანა
    message.setText(f"Total Number of Symbols Entered: {len(msg)}")
    #მესიჯის ყუთის გაშვება
    message.exec_()

main()

