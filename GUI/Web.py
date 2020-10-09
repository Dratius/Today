# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/D'ratius/AppData/Local/Temp/WebDtdDrc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WebForm(object):
    def setupUi(self, WebForm):
        WebForm.setObjectName("WebForm")
        WebForm.setWindowModality(QtCore.Qt.ApplicationModal)
        WebForm.resize(584, 356)
        self.gridLayout = QtWidgets.QGridLayout(WebForm)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxResults = QtWidgets.QComboBox(WebForm)
        self.comboBoxResults.setCurrentText("")
        self.comboBoxResults.setObjectName("comboBoxResults")
        self.gridLayout.addWidget(self.comboBoxResults, 0, 0, 1, 1)
        self.lineEditSearch = QtWidgets.QLineEdit(WebForm)
        self.lineEditSearch.setClearButtonEnabled(True)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.gridLayout.addWidget(self.lineEditSearch, 0, 1, 1, 1)
        self.pushButtonSearch = QtWidgets.QPushButton(WebForm)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.gridLayout.addWidget(self.pushButtonSearch, 0, 2, 1, 1)
        self.DescriptionBrowser = QtWidgets.QTextBrowser(WebForm)
        self.DescriptionBrowser.setObjectName("DescriptionBrowser")
        self.gridLayout.addWidget(self.DescriptionBrowser, 1, 0, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(WebForm)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout.addWidget(self.pushButtonAdd, 2, 0, 1, 3)

        self.retranslateUi(WebForm)
        QtCore.QMetaObject.connectSlotsByName(WebForm)

    def retranslateUi(self, WebForm):
        _translate = QtCore.QCoreApplication.translate
        WebForm.setWindowTitle(_translate("WebForm", "Web Search"))
        self.lineEditSearch.setPlaceholderText(_translate("WebForm", "Search"))
        self.pushButtonSearch.setText(_translate("WebForm", "Search"))
        self.pushButtonAdd.setText(_translate("WebForm", "ADD"))
