import random
import expr_functions as ex
from math_functions import *


class Product:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"({self.expr_1} * {self.expr_2})"

    def eval(self, x, y):
        return self.expr_1.eval(x, y) * self.expr_2.eval(x, y)


class Quotient:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"quotient({self.expr_1}, {self.expr_2})"

    def eval(self, x, y):
        return quotient(self.expr_1.eval(x, y), self.expr_2.eval(x, y))


class Modulo:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"modulo({self.expr_1}, {self.expr_2})"

    def eval(self, x, y):
        return modulo(self.expr_1.eval(x, y), self.expr_2.eval(x, y))


class Sum:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"({self.expr_1} + {self.expr_2})"

    def eval(self, x, y):
        return self.expr_1.eval(x, y) + self.expr_2.eval(x, y)


class Avg:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"avg({self.expr_1}, {self.expr_2})"

    def eval(self, x, y):
        return avg(self.expr_1.eval(x, y), self.expr_2.eval(x, y))


#################
# Three Outputs #
#################


class Level:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)
        self.expr_3 = ex.build_expr(prob * prob)
        self.rnd_f = random.random()

    def __repr__(self):
        return f"level({self.expr_1}, {self.expr_2}, {self.expr_3}, {self.rnd_f})"

    def eval(self, x, y):
        return level(self.expr_1.eval(x, y), self.expr_2.eval(x, y),
                     self.expr_3.eval(x, y), self.rnd_f)


class Mix:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)
        self.expr_3 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"mix({self.expr_1}, {self.expr_2}, {self.expr_3})"

    def eval(self, x, y):
        return mix(self.expr_1.eval(x, y), self.expr_2.eval(x, y), self.expr_3.eval(x, y))
