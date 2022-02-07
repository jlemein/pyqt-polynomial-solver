import PyQt5.QtWidgets
import PyQt5.QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtGui, QtCore, uic

class PolynomialEditorDialog(QDialog):
    def __init__(self, polynomials) -> None:
        super().__init__()

        self.polynomials = polynomials

        # Load and retrieve UI elements
        uic.loadUi('resources/polynomialeditor_dialog.ui', self)

        self.table = self.findChild(QtWidgets.QTableWidget, 'tableWidget')
        self.addButton = self.findChild(QtWidgets.QPushButton, 'addButton')
        self.deleteButton = self.findChild(QtWidgets.QPushButton, 'deleteButton')

        # handle the table data
        column_labels = ["Label"]
        for x in range(4, -1, -1):
            column_labels.append("x^{}".format(x))
        self.table.setColumnCount(len(column_labels))
        self.table.setHorizontalHeaderLabels(column_labels)

        for n, poly in self.polynomials:
            self.table.insertRow(n)
            for idx, val in enumerate(poly, start=0):
                value_item = QtWidgets.QTableWidgetItem(str(val))
                coefficient_item = QtWidgets.QTableWidgetItem(str(idx))
                self.table.setItem(n, idx, value_item)
                self.table.setItem(n, idx, coefficient_item)

        self.table.horizontalHeader().setResizeMode(QtWidgets.QHeaderView.Stretch)
        self.show()

