from py_polynomial_solver.model.equation import Equation

class Polynomial(Equation):
    """Polynomial data structure"""
    def __init__(self, coefficients = [0]) -> None:
        super().__init__()

        self._coefficients = coefficients

    def toString(self) -> str:
        coefficients_str = []
        for idx, val in self._coefficients[::-1]:
            if idx == 0:
                coefficients_str.append(val)
            else:
                coefficients_str.append("{}^{}".format(val, idx))
        
        return coefficients_str.join("+")

    def coefficients(self):
        return self._coefficients

    def get_coefficient(self, coeff):
        return self._coefficients[coeff] if len(self._coefficients) > coeff else 0

    def set_coefficient(self, coeff, value):
        self._coefficients[coeff] = value