import sys

from PyQt5 import QtWidgets, QtGui

from MainWindow import Ui_MainWindow


class StartProgram:
    randomDropWindow = None


    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        app.setApplicationName("DNDestiny Loot Generator 0.0.1")
        appIcon = QtGui.QIcon()
        appIcon.addPixmap(QtGui.QPixmap("bin/images/Token_Engram_Exotic.png"), QtGui.QIcon.Normal,
                          QtGui.QIcon.Off)
        app.setWindowIcon(appIcon)
        app.setApplicationVersion("0.0.1")
        stylesheet = "bin/ButtonsStyle.css"
        with open(stylesheet, "r") as fh:
            app.setStyleSheet(fh.read())
        MainWindow = QtWidgets.QMainWindow()
        MainUI = Ui_MainWindow()
        MainUI.setupUi(MainWindow)
        MainWindow.show()

        sys.exit(app.exec_())


StartProgram()
