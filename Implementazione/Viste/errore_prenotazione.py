# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errore_prenotazione.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_erroreprenotazione(object):
    def setupUi(self, erroreprenotazione,messaggio):
        erroreprenotazione.setObjectName("erroreprenotazione")
        erroreprenotazione.resize(400, 106)
        self.buttonBox = QtWidgets.QDialogButtonBox(erroreprenotazione)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.errore = QtWidgets.QLabel(erroreprenotazione)
        self.errore.setGeometry(QtCore.QRect(80, 30, 181, 51))
        self.errore.setObjectName("errore")

        self.retranslateUi(erroreprenotazione,messaggio)
        self.buttonBox.accepted.connect(erroreprenotazione.accept) # type: ignore
        self.buttonBox.rejected.connect(erroreprenotazione.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(erroreprenotazione)

    def retranslateUi(self, erroreprenotazione,messaggio):
        _translate = QtCore.QCoreApplication.translate
        erroreprenotazione.setWindowTitle(_translate("erroreprenotazione", "Dialog"))
        self.errore.setText(_translate("erroreprenotazione", messaggio))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    erroreprenotazione = QtWidgets.QDialog()
    ui = Ui_erroreprenotazione()
    ui.setupUi(erroreprenotazione)
    erroreprenotazione.show()
    sys.exit(app.exec_())
