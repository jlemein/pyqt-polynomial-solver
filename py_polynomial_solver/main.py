import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import * #QMainWindow, QLabel, QVBoxLayout, QLineEdit, QWidget
from PyQt5.QtCore import QSize    
import pyqtgraph as pg
from py_polynomial_solver.view.math_text_label import MathTextLabel
import numpy as np
from py_polynomial_solver.model.polynomial import Polynomial
from py_polynomial_solver.view.polynomial_editor_dialog import PolynomialEditorDialog

class PolynomialSolverApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))    
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com")
        
        self.polynomials = [Polynomial([10, 20, 30, 40])]

        self.editPolynomialButton = QPushButton("Edit")
        self.editPolynomialButton.clicked.connect(self.edit_button_clicked)
        
        self.graphWidget = pg.PlotWidget()

        # centralWidget = QWidget(self)          
        # self.setCentralWidget(centralWidget)   

        title = QLabel("Hello World from PyQt", self) 
        title.setAlignment(QtCore.Qt.AlignCenter)

        #mathText=r'$X_k = \sum_{n=0}^{N-1} x_n . e^{\frac{-i2\pi kn}{N}}$'
        mathText=r'$x^2 - 10x + 10$'
        self.updateCharts()
        
        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(self.graphWidget)
        layout.addWidget(self.editPolynomialButton)
        layout.addWidget(MathTextLabel(mathText, self), alignment=QtCore.Qt.AlignHCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def updateCharts(self):
        x = np.arange(-10, 10, 1)
        y = np.power(self.polynomials[0].coefficients(), np.arange(0,4))

        self.graphWidget.plot(x, y)
    
    def edit_button_clicked(self):
        print([1,2,3,4,5])
        dlg = PolynomialEditorDialog(self.polynomials)
        dlg.exec()

        self.polynomials = dlg.polynomials
        self.updateCharts()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = PolynomialSolverApp()
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()