🎨 PyQt5 Mini Projects Collection

A collection of simple yet powerful GUI applications built with PyQt5 — demonstrating interactive user interfaces, event handling, and real-world functionality such as image editing, authentication, and dynamic visuals.

📁 Projects Overview
Project	Description	Core Features
🧮 Calculator
	A styled GUI calculator with dynamic expression evaluation	Basic arithmetic, clear screen, live input display
🎨 Color Changer
	A one-click app that changes button colors randomly	Dynamic colors, simple UI
🖼️ Photo Editor
	A lightweight image editor using PIL (Pillow)	Load, blur, rotate, black & white filter
🔢 Practice Counter
	A text counter showing the number of entered characters	Message box output, PyQt5 signals
🔐 Login Counter App
	A mini app with login system and text counter	Login validation, text processing, UI from Qt Designer
🧮 Calculator

A fully functional PyQt5-based calculator with a modern UI and colorful styling.

🧠 Features

Perform addition, subtraction, multiplication, and division

Clear screen with one button

Custom design using QSS (Qt Style Sheets)

Built from .ui file designed in Qt Designer

🗂️ Files
calculator/
├── calculator.py
└── calculator.ui

▶️ Run
python calculator.py

🎨 Color Changer

A minimal PyQt5 app that changes button color randomly on each click.

⚙️ Features

One-click button color change

Random color generation from predefined list

Clean interface

🗂️ Files
color_changer/
└── color_changer.py

▶️ Run
python color_changer.py

🖼️ Photo Editor

A simple image editing app using Pillow (PIL) for transformations, built with PyQt5 widgets.

🧠 Features

Load images dynamically

Apply filters: Blur, Rotate, Black & White

Real-time preview with QPixmap

Interactive layout with large image preview

🗂️ Files
photo_editor/
└── photo_editor.py

🧩 Requirements
pip install PyQt5 pillow

▶️ Run
python photo_editor.py

🔢 Practice Counter

A simple text counting app that counts characters entered in a text box.

⚙️ Features

Text input via QTextEdit

Displays symbol count in a message box

Clean layout and button actions

🗂️ Files
practice_counter/
└── practice.py

▶️ Run
python practice.py

🔐 Login Counter App

A login-protected text counter that enables tools only after successful authentication.

🧠 Features

Login form with username & password validation

Character counter for input text

Clear text functionality

Built using .ui file designed in Qt Designer

🗂️ Files
pyqt5_app/
├── app.py
└── app2.ui

▶️ Run
python app.py

🧰 Requirements

Install required dependencies before running any project:

pip install PyQt5 pillow


To edit .ui files, install PyQt5 Tools:

pip install pyqt5-tools


Then open Qt Designer via:

<your-env-path>\Lib\site-packages\qt5_applications\Qt\bin\designer.exe
