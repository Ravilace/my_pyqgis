from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event):
        context = QMenu(self)
        context.addAction(QAction("test1", self))
        context.addAction(QAction("test2", self))
        context.addAction(QAction("test3", self))

        context.exec(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()