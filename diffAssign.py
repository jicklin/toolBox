# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diffAssign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diffAssignForm(object):
    def setupUi(self, diffAssignForm):
        diffAssignForm.setObjectName("diffAssignForm")
        diffAssignForm.setWindowModality(QtCore.Qt.NonModal)
        diffAssignForm.resize(684, 448)
        self.fileShowInput = QtWidgets.QTextEdit(diffAssignForm)
        self.fileShowInput.setGeometry(QtCore.QRect(180, 60, 341, 41))
        self.fileShowInput.setObjectName("fileShowInput")
        self.fileSelectorBtn = QtWidgets.QPushButton(diffAssignForm)
        self.fileSelectorBtn.setGeometry(QtCore.QRect(540, 60, 111, 41))
        self.fileSelectorBtn.setObjectName("fileSelectorBtn")
        self.label = QtWidgets.QLabel(diffAssignForm)
        self.label.setGeometry(QtCore.QRect(60, 60, 72, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(diffAssignForm)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.label_2.setObjectName("label_2")
        self.outPathInput = QtWidgets.QTextEdit(diffAssignForm)
        self.outPathInput.setGeometry(QtCore.QRect(180, 140, 341, 41))
        self.outPathInput.setObjectName("outPathInput")
        self.fileOutPathBtn = QtWidgets.QPushButton(diffAssignForm)
        self.fileOutPathBtn.setGeometry(QtCore.QRect(540, 140, 111, 41))
        self.fileOutPathBtn.setObjectName("fileOutPathBtn")
        self.label_3 = QtWidgets.QLabel(diffAssignForm)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 72, 15))
        self.label_3.setObjectName("label_3")
        self.groupNumInput = QtWidgets.QTextEdit(diffAssignForm)
        self.groupNumInput.setGeometry(QtCore.QRect(180, 220, 104, 31))
        self.groupNumInput.setObjectName("groupNumInput")
        self.label_4 = QtWidgets.QLabel(diffAssignForm)
        self.label_4.setGeometry(QtCore.QRect(300, 230, 72, 15))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(diffAssignForm)
        self.pushButton.setGeometry(QtCore.QRect(170, 330, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(diffAssignForm)
        self.label_5.setGeometry(QtCore.QRect(60, 280, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.decimalPlaceInput = QtWidgets.QTextEdit(diffAssignForm)
        self.decimalPlaceInput.setGeometry(QtCore.QRect(180, 270, 104, 31))
        self.decimalPlaceInput.setObjectName("decimalPlaceInput")

        self.retranslateUi(diffAssignForm)
        QtCore.QMetaObject.connectSlotsByName(diffAssignForm)

    def retranslateUi(self, diffAssignForm):
        _translate = QtCore.QCoreApplication.translate
        diffAssignForm.setWindowTitle(_translate("diffAssignForm", "diffAssign"))
        self.fileSelectorBtn.setText(_translate("diffAssignForm", "选择文件"))
        self.label.setText(_translate("diffAssignForm", "选择文件"))
        self.label_2.setText(_translate("diffAssignForm", "选择导出文件夹"))
        self.fileOutPathBtn.setText(_translate("diffAssignForm", "选择导出路径"))
        self.label_3.setText(_translate("diffAssignForm", "分组规则"))
        self.label_4.setText(_translate("diffAssignForm", "位"))
        self.pushButton.setText(_translate("diffAssignForm", "开始处理"))
        self.label_5.setText(_translate("diffAssignForm", "小数位数"))
