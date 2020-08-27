import random_art.expr_functions as ex
from random_art.c_math import *
from random_art.math_functions import *


class CosPi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_cos(c_pi() * {self.expr})"

    def eval(self, x, y):
        return c_cos(c_pi() * self.expr.eval(x, y))


class SinPi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_sin(c_pi() * {self.expr})"

    def eval(self, x, y):
        return c_sin(c_pi() * self.expr.eval(x, y))


class Cos2Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_cos(2 * c_pi() * {self.expr})"

    def eval(self, x, y):
        return c_cos(2 * c_pi() * self.expr.eval(x, y))


class Sin2Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_sin(2 * c_pi() * {self.expr})"

    def eval(self, x, y):
        return c_sin(2 * c_pi() * self.expr.eval(x, y))


class Sin:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_sin({self.expr})"

    def eval(self, x, y):
        return c_sin(self.expr.eval(x, y))


class Cos:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_cos({self.expr})"

    def eval(self, x, y):
        return c_cos(self.expr.eval(x, y))


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
        return f"{self.expr} * c_pi()"

    def eval(self, x, y):
        return self.expr.eval(x, y) * c_pi()


class Jitter:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"{self.expr} * c_sin({self.expr})"

    def eval(self, x, y):
        return self.expr.eval(x, y) * c_sin(self.expr.eval(x, y))


class Peak:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"quotient(c_sin({self.expr}), {self.expr})"

    def eval(self, x, y):
        return quotient(c_sin(self.expr.eval(x, y)), self.expr.eval(x, y))


class Loops:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"quotient(c_tan({self.expr}),c_sin({self.expr}))"

    def eval(self, x, y):
        return quotient(c_tan(self.expr.eval(x, y)),
                        c_sin(self.expr.eval(x, y)))


class MidPoint:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_atan({self.expr})"

    def eval(self, x, y):
        return c_atan(self.expr.eval(x, y))


class Curve:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_tanh({self.expr})"

    def eval(self, x, y):
        return c_tanh(self.expr.eval(x, y))


class Absolut:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"abs({self.expr})"

    def eval(self, x, y):
        return abs(self.expr.eval(x, y))


class Waves:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"abs({self.expr})"

    def eval(self, x, y):
        return c_exp(c_pi()*c_sin(self.expr.eval(x, y)))
