#pip install pyqt5
#pip install pillow


#სურათის გახსნა
# from PIL import Image, ImageFilter
# with Image.open('cat.png') as original:
#     original.show()
#     #სურათის თვისებები
#     print(original.size)
#     print(original.format)
#     print(original.mode)
#
#     #სურათის გაშავთეთრება
#     pic_gray = original.convert("L")
#     pic_gray.show()
#     pic_blured = original.filter(ImageFilter.BLUR)
#     pic_up = original.transpose(Image.ROTATE_90)
#     pic_gray.save('gray.png')





# აპლიკაციისთვის საჭირო მოდულების შემოტანა
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter

class Photoshop():
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()

        self.window.setGeometry(100, 100, 500, 500)
        self.window.setWindowTitle("Photoshop")

        self.layout = QVBoxLayout()

        self.label_image = QLabel()
        self.image = QPixmap(400, 400)
        self.label_image.setPixmap(self.image)
        self.label_image.setAlignment(Qt.AlignCenter)
        self.label_image.hide()

        self.layout.addWidget(self.label_image)


        self.label = QLabel("Enter Image Name Below:")
        self.label.setFont(QFont("Arial", 16))
        # ტექსტის შემყვანი ელემენტის შექმნა
        self.textbox = QTextEdit()

        self.textbox.setFont(QFont("Arial", 16))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textbox)

        self.button_load = QPushButton("Load Image")
        self.button_load.clicked.connect(lambda: self.on_load(self.textbox.toPlainText()))

        self.button_blur = QPushButton("Blur")
        self.button_blur.clicked.connect(lambda: self.on_blur())

        self.button_rotate = QPushButton("Rotate")
        self.button_rotate.clicked.connect(lambda: self.on_rotate())

        self.button_b_w = QPushButton("Black&White")
        self.button_b_w.clicked.connect(lambda: self.on_b_w())

        self.buttons = [self.button_load, self.button_rotate, self.button_b_w, self.button_blur]
        for button in self.buttons:
            # ღილაკის სიმაღლის რეგულირება
            button.setMinimumHeight(50)
            # ღილაკის წარწერის ზომა
            button.setFont(QFont("Arial", 16))

            self.layout.addWidget(button)

        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()

    def on_load(self, msg):
        with Image.open(msg) as original:
            #make copy
            self.new_name = "copy_"+msg
            original.save(self.new_name)

        self.image = QPixmap(self.new_name)
        self.textbox.setText("")
        self.label_image.setPixmap(self.image)
        self.label_image.show()



    def on_b_w(self):
        with Image.open(self.new_name) as copy:
            pic_gray = copy.convert("L")
            pic_gray.save(self.new_name)
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)

    def on_blur(self):
        with Image.open(self.new_name) as copy:
            pic_blur = copy.filter(ImageFilter.BLUR)
            pic_blur.save(self.new_name)
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)

    def on_rotate(self):
        with Image.open(self.new_name) as copy:
            pic_rotate = copy.transpose(Image.ROTATE_90)
            pic_rotate.save(self.new_name)
            self.image = QPixmap(self.new_name)
            self.label_image.setPixmap(self.image)



photoshop1 = Photoshop()

