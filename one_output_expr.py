import expr_functions as ex
from math_functions import *
import math


class CosPi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"math.cos(math.pi * {self.expr})"

    def eval(self, x, y):
        return math.cos(math.pi * self.expr.eval(x, y))


class SinPi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"math.sin(math.pi * {self.expr})"

    def eval(self, x, y):
        return math.sin(math.pi * self.expr.eval(x, y))


class Cos2Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"math.cos(2 * math.pi * {self.expr})"

    def eval(self, x, y):
        return math.cos(2 * math.pi * self.expr.eval(x, y))


class Sin2Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"math.sin(2 * math.pi * {self.expr})"

    def eval(self, x, y):
        return math.sin(2 * math.pi * self.expr.eval(x, y))


class Sin:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"math.sin({self.expr})"

    def eval(self, x, y):
        return math.sin(self.expr.eval(x, y))


class Cos:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"math.cos({self.expr})"

    def eval(self, x, y):
        return math.cos(self.expr.eval(x, y))


class Dip:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"dip({self.expr})"

    def eval(self, x, y):
        return dip(self.expr.eval(x, y))


class Tip:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"tip({self.expr})"

    def eval(self, x, y):
        return tip(self.expr.eval(x, y))


class Parabola:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"parabola({self.expr})"

    def eval(self, x, y):
        return parabola(self.expr.eval(x, y))


class Pow:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"pow({self.expr})"

    def eval(self, x, y):
        return pow(self.expr.eval(x, y))


class Sqrt:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"sqrt({self.expr})"

    def eval(self, x, y):
        return sqrt(self.expr.eval(x, y))


class Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"{self.expr} * math.pi"

    def eval(self, x, y):
        return self.expr.eval(x, y) * math.pi

# Other Ideas #

# class Jitter growing "x*sin(x)""
# class hearth "x^2+(y-3root(x^2))^2 = 1"
# class high peak mid "sin(x)/x"
# tan(x)/sin(x) loops
# atan(x) midpoint
# tanh(x)
# 'pi*(x**2 + y**2)',  # circle
# 'sin(x)',  # gradient horizontal
# 'cos(x)',  # gradient horizontal center-hollow
# 'cos(x)+sin(x)',
# 'abs(x)',
# '2*x**2*y**2',  # corner circles
# 'x**5*y**2+3*x*3+2*x**2+x**4',  # thick gradient
# 'exp(pi*sin(x))',  # lighter gradient than sin(x)
# 'sin(pi*x)*cos(x)*pi*(y**2 + y**2)',  # reflecting half circles
# 'sin(2*x**2*y**2)',
