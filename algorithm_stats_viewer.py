import sys
from main_window import MainWindow
from PySide import QtGui


def main():
    app = QtGui.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.raise_()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
