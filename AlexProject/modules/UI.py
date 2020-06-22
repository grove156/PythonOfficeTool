# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_uiFiles/Alex.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 577)
        self.excel_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.excel_lineEdit.setGeometry(QtCore.QRect(20, 70, 381, 21))
        self.excel_lineEdit.setObjectName("excel_lineEdit")
        self.search_pushButton = QtWidgets.QPushButton(Dialog)
        self.search_pushButton.setGeometry(QtCore.QRect(20, 490, 471, 23))
        self.search_pushButton.setObjectName("search_pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 351, 21))
        self.label.setObjectName("label")
        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setGeometry(QtCore.QRect(20, 150, 191, 20))
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.date_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.date_lineEdit.setGeometry(QtCore.QRect(20, 220, 191, 20))
        self.date_lineEdit.setObjectName("date_lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(250, 130, 41, 21))
        self.label_5.setObjectName("label_5")
        self.etc_plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.etc_plainTextEdit.setGeometry(QtCore.QRect(20, 310, 191, 161))
        self.etc_plainTextEdit.setObjectName("etc_plainTextEdit")
        self.result_plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.result_plainTextEdit.setGeometry(QtCore.QRect(250, 150, 241, 321))
        self.result_plainTextEdit.setObjectName("result_plainTextEdit")
        self.file_pushButton = QtWidgets.QPushButton(Dialog)
        self.file_pushButton.setGeometry(QtCore.QRect(420, 70, 75, 23))
        self.file_pushButton.setObjectName("file_pushButton")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 530, 471, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search_pushButton.setText(_translate("Dialog", "검색"))
        self.label.setText(_translate("Dialog", "사용할 액셀파일을 찾아주세요."))
        self.label_2.setText(_translate("Dialog", "입금자명"))
        self.label_3.setText(_translate("Dialog", "만기일 (mm/dd/yyyy)"))
        self.label_4.setText(_translate("Dialog", "비고"))
        self.label_5.setText(_translate("Dialog", "결과"))
        self.file_pushButton.setText(_translate("Dialog", "파일찾기"))
        self.label_6.setText(_translate("Dialog", "*입금자명, 만기일, 잘못된 파일인경우 프로그램꺼짐. 실력이 후달려서 경고메세지는 없어요^^"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
