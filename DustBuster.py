#This app is made by Sharad Verma using python language.
#Version of this app is 1.0(2024)

#This app clears the trash files present in %temp% & prefetch folders.

import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

def clear_temp():
    temp_path = os.getenv('TEMP')
    try:
        for filename in os.listdir(temp_path):
            file_path = os.path.join(temp_path, filename)
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
            except Exception:
                continue
        status_label.setText("Temporary files cleared successfully!")
        status_label.setStyleSheet("color: white; font-size: 16px;")
    except Exception:
        status_label.setText("Error clearing %TEMP%")
        status_label.setStyleSheet("color: white; font-size: 16px;")

def clear_prefetch():
    prefetch_path = r'C:\Windows\Prefetch'
    try:
        for filename in os.listdir(prefetch_path):
            file_path = os.path.join(prefetch_path, filename)
            try:
                os.remove(file_path)
            except Exception:
                continue
        status_label.setText("Prefetch files cleared successfully!")
        status_label.setStyleSheet("color: white; font-size: 16px;")
    except Exception:
        status_label.setText("Error clearing Prefetch")
        status_label.setStyleSheet("color: white; font-size: 16px;")

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle('Clear Temp & Prefetch')
window.setGeometry(400, 200, 400, 300)
window.setStyleSheet("background-color: #34495E; font-family: 'Comic Sans MS';")

# Set the application icon
window.setWindowIcon(QIcon('F:\Downloads\icon.ico'))

# Heading label asking what to clear
heading_label = QLabel("What would you like to clear?", window)
heading_label.setAlignment(Qt.AlignCenter)
heading_label.setStyleSheet("color: white; font-size: 20px; margin-bottom: 20px;")

# Create buttons with larger font size and increased gap
temp_button = QPushButton('%TEMP% Folder', window)
temp_button.setStyleSheet("""
    background-color: #2980B9; 
    color: white; 
    font-size: 18px; 
    border-radius: 15px; 
    padding: 15px;
""")
temp_button.clicked.connect(clear_temp)

prefetch_button = QPushButton('Prefetch Folder', window)
prefetch_button.setStyleSheet("""
    background-color: #2980B9; 
    color: white; 
    font-size: 18px; 
    border-radius: 15px; 
    padding: 15px;
""")
prefetch_button.clicked.connect(clear_prefetch)

# Create status label with larger font size
status_label = QLabel('', window)
status_label.setAlignment(Qt.AlignCenter)
status_label.setStyleSheet("color: white; font-size: 16px;")

# Create layout and add widgets with more gap between buttons
layout = QVBoxLayout()
layout.addWidget(heading_label)
layout.addWidget(temp_button)
layout.addWidget(prefetch_button)
layout.addWidget(status_label)

# Add more spacing between buttons
layout.setSpacing(20)

# Create a horizontal layout for footer to align left and right
footer_layout = QHBoxLayout()

# Left label for "Made by" with faded color and CMD-like font (Consolas)
made_by_label = QLabel("Made by: Sharad Verma", window)
made_by_label.setStyleSheet("""
    color: rgba(211, 211, 211, 0.5); 
    font-size: 12px; 
    font-family: 'Consolas', 'Courier New', monospace; 
    padding-left: 10px;
""")
footer_layout.addWidget(made_by_label, alignment=Qt.AlignLeft)

# Right label for "Version" with faded color and CMD-like font (Consolas)
version_label = QLabel("Version: 1.0", window)
version_label.setStyleSheet("""
    color: rgba(211, 211, 211, 0.5); 
    font-size: 12px; 
    font-family: 'Consolas', 'Courier New', monospace; 
    padding-right: 10px;
""")
footer_layout.addWidget(version_label, alignment=Qt.AlignRight)

# Add footer layout to main layout at the bottom
layout.addLayout(footer_layout)

# Set the main layout
window.setLayout(layout)

# Show the window
window.show()

# Run the application
app.exec_()
