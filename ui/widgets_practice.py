import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QSpinBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        widget = QSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(f"{i=}")

    def value_changed_str(self, s):
        print(f"{s=}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
