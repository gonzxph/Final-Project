import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QFrame
from PyQt5.QtCore import Qt
from wesdw import widget

frame_width = 0
frame_height = 0
frame_x = 0
frame_y = 0

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout()  # Creating a grid layout

        self.frame2 = QFrame(self)
        self.frame = QFrame(self)

        self.frame2.setStyleSheet("background-color:#f2f2f2;")

        self.block = QLabel(self.frame)
        self.frame.setStyleSheet("background-color: orange;")
        self.block.setStyleSheet("background-color: green;")

        self.f = widget(self.frame)
        self.f.setStyleSheet("background-color:lightgrey;")

        grid_layout.addWidget(self.frame, 1, 0)
        grid_layout.addWidget(self.frame2, 0, 0)
        self.setLayout(grid_layout)

        self.setMinimumSize(1280, 720)
        self.setWindowTitle('Grid Layout Example')
        self.show()

    def resizeEvent(self, event):
        frame_width = int(self.height() * 0.8)
        self.frame.setFixedHeight(frame_width)
        self.f.setGeometry(0, 0, int(self.frame.width()), int(self.frame.height()))
