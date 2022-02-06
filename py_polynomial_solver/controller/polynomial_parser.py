import re

class PolynomialParser():
    def __init__(self):
        pass

    def parseFromString(self, equation):
        # splits the equation in terms of the variable used.
        # parts = re.split('([a-zA-Z]+\^?\d)', equation)
        parts = re.split('\+', equation)
        parts = [element.strip("+ '") for element in parts]

        print(parts)
        coefficients = [0] * 5

        for p in parts:
            x = re.search('[a-zA-Z]+(\^\d+)?$', p)
            if x != None:
                # element ends with polynomial of form x^<??>
                split = re.split("([a-zA-Z]+\^?)", p)

                if len(split) == 1:
                    print("coeff is 0")
                    coeff = 0
                else:
                    print("Length of split is {}".format(len(split)))
                    print("Split[2] is {}".format(split[2]))
                    coeff = int(split[2]) if len(split[2]) >= 1 else 1
                    print("{} leads to coeff is {}".format(p, coeff))

                if coeff <= 5:
                    coefficients[coeff] += float(split[0])
                else:
                    raise Exception("Polynomial could not be parsed. Coefficient higher than max number of coefficients")
            else:
                coefficients[0] += float(p) if len(p) > 0 else 0

        if (all(v ==0 for v in coefficients)):
            return [0]
        else:
            # find index of largest nonzero coefficient for polynomial
            idx = len(coefficients) - next(i for i, val in enumerate(reversed(coefficients), 1) if val != 0)
            return coefficients[:idx+1]