# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confermaiscrizione.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfermaIscrizione(object):
    def setupUi(self, ConfermaIscrizione):
        ConfermaIscrizione.setObjectName("ConfermaIscrizione")
        ConfermaIscrizione.resize(400, 93)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfermaIscrizione)
        self.buttonBox.setGeometry(QtCore.QRect(20, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ConfermaIscrizione)
        self.label.setGeometry(QtCore.QRect(30, 20, 341, 20))
        self.label.setObjectName("label")

        self.retranslateUi(ConfermaIscrizione)
        self.buttonBox.accepted.connect(ConfermaIscrizione.accept) # type: ignore
        self.buttonBox.rejected.connect(ConfermaIscrizione.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ConfermaIscrizione)

    def retranslateUi(self, ConfermaIscrizione):
        _translate = QtCore.QCoreApplication.translate
        ConfermaIscrizione.setWindowTitle(_translate("ConfermaIscrizione", "Dialog"))
        self.label.setText(_translate("ConfermaIscrizione", "Iscrizione effettuata con successo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfermaIscrizione = QtWidgets.QDialog()
    ui = Ui_ConfermaIscrizione()
    ui.setupUi(ConfermaIscrizione)
    ConfermaIscrizione.show()
    sys.exit(app.exec_())