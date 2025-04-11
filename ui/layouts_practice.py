# -*- coding: utf-8 -*-
# @Time    : 2025/4/11 10:20
# @Author  : Ravilace
# @File    : layouts_practice.py
# @Software: PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()
        layout.addWidget(Color('red'), 0, 3)
        layout.addWidget(Color('green'), 1, 1)
        layout.addWidget(Color('blue'), 3, 0)
        layout.addWidget(Color('orange'), 2, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
