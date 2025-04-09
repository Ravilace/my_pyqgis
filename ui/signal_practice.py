from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, a0):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, a0):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, a0):
        self.label.setText("mouseDoubleClickEvent")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()