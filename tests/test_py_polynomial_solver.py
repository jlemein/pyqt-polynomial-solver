import unittest
from py_polynomial_solver.controller.polynomial_parser import PolynomialParser

class TestPolynomialParser(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(PolynomialParser().parseFromString("5"), [5])
        self.assertEqual(PolynomialParser().parseFromString("125"), [125])
        self.assertEqual(PolynomialParser().parseFromString("125.45"), [125.45])
        self.assertEqual(PolynomialParser().parseFromString("0"), [0])
        self.assertEqual(PolynomialParser().parseFromString(""), [0])

    def test_linear(self):
        self.assertEqual(PolynomialParser().parseFromString("5x + 10"), [10, 5])
        self.assertEqual(PolynomialParser().parseFromString("5x"), [0, 5])

    def test_quadratic(self):
        #self.assertEqual(PolynomialParser().parseFromString("5x^2 + 10"), [10, 0, 5])
        #self.assertEqual(PolynomialParser().parseFromString("10"), [10])
        #self.assertEqual(PolynomialParser().parseFromString("10x"), [0, 10])
        self.assertEqual(PolynomialParser().parseFromString("10x^2 + 3x - 120"), [10, 3, -120])
        #self.assertEqual(PolynomialParser().parseFromString("-10x^2 - 3x + 120"), [-10, -3, 120])

if __name__ == '__main__':
    unittest.main()