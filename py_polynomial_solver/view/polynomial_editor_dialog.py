from PyQt5.QtWidgets import QDialog

class PolynomialEditorDialog(QDialog):
    def __init__(self, polynomial) -> None:
        super().__init__()

        self.polynomial = polynomial
        self.setWindowTitle("Edit Polynomial")
