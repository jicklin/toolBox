# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingForm(object):
    def setupUi(self, LoadingForm):
        LoadingForm.setObjectName("LoadingForm")
        LoadingForm.resize(345, 220)
        self.imageLabel = QtWidgets.QLabel(LoadingForm)
        self.imageLabel.setGeometry(QtCore.QRect(140, 30, 72, 51))
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageLabel.setObjectName("imageLabel")
        self.textLabel = QtWidgets.QLabel(LoadingForm)
        self.textLabel.setGeometry(QtCore.QRect(10, 140, 321, 31))
        self.textLabel.setObjectName("textLabel")

        self.retranslateUi(LoadingForm)
        QtCore.QMetaObject.connectSlotsByName(LoadingForm)

    def retranslateUi(self, LoadingForm):
        _translate = QtCore.QCoreApplication.translate
        LoadingForm.setWindowTitle(_translate("LoadingForm", "拼命处理中"))
        self.imageLabel.setText(_translate("LoadingForm", "TextLabel"))
        self.textLabel.setText(_translate("LoadingForm", "处理中"))
