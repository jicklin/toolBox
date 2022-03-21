import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication

from Loading import Ui_LoadingForm


class LoadingPop(QWidget, Ui_LoadingForm):
    def __init__(self):
        super(LoadingPop, self).__init__()
        self.setupUi(self)
        jpg = QtGui.QPixmap("images/loading.gif")
        self.imageLabel.setPixmap(jpg)

    def set_message(self, message):
        self.textLabel.setText(message)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadingPop()
    win.show()
    sys.exit(app.exec_())
