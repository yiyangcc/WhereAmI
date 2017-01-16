# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WhereAmI_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WhereAmIDialogBase(object):
    def setupUi(self, WhereAmIDialogBase):
        WhereAmIDialogBase.setObjectName(_fromUtf8("WhereAmIDialogBase"))
        WhereAmIDialogBase.resize(400, 96)
        self.label = QtGui.QLabel(WhereAmIDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(WhereAmIDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 381, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(WhereAmIDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(290, 60, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(WhereAmIDialogBase)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), WhereAmIDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(WhereAmIDialogBase)

    def retranslateUi(self, WhereAmIDialogBase):
        WhereAmIDialogBase.setWindowTitle(_translate("WhereAmIDialogBase", "Where Am I?", None))
        self.label.setText(_translate("WhereAmIDialogBase", "Coordinates of map click:", None))
        self.pushButton.setText(_translate("WhereAmIDialogBase", "Close", None))

