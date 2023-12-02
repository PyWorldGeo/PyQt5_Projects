from PyQt5.QtWidgets import *
from random import choice

colors = ["red", "green", "purple", "yellow", "brown", "orange", "white", "blue"]

def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Color Changer App")
    window.setFixedSize(500, 200)

    layout = QVBoxLayout()


    button = QPushButton("Click!")
    button.setFixedHeight(100)

    layout.addWidget(button)
    window.setLayout(layout)

    button.clicked.connect(lambda: button.setStyleSheet(f"background-color: {choice(colors)};"))

    window.setStyleSheet("background-color: grey;")

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()