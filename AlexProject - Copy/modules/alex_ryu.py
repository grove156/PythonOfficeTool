# -*- coding: utf-8 -*-

import sys, UI
from modules import logic as lo
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainDialog(QDialog, UI.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self, None)
        self.setupUi(self)

        self.search_pushButton.clicked.connect(self.search)
        self.file_pushButton.clicked.connect(self.get_file_path)

    def get_file_path(self):
        fname = QFileDialog.getOpenFileName(self)
        self.excel_lineEdit.setText(fname[0])

    def search(self):
        filename = self.excel_lineEdit.text()
        name = self.name_lineEdit.text()
        date = self.date_lineEdit.text()
        etc = self.etc_plainTextEdit.toPlainText()
        searching = lo.Search_customer(filename, name, date, etc)
        result = searching.print_result()
        self.result_plainTextEdit.insertPlainText("")
        self.result_plainTextEdit.insertPlainText(result)

app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()