import expr_functions as ex
from math_functions import *
import random


class Product:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"({self.expr_1} * {self.expr_2})"

    def eval(self, x, y):
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        return self._expr_1 * self._expr_2


class Quotient:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"quotient({self.expr_1}, {self.expr_2})"

    def eval(self, x, y):
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        return quotient(self._expr_1, self._expr_2)


class Modulo:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"modulo({self.expr_1}, {self.expr_2})"

    def eval(self, x, y):
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        return modulo(self._expr_1, self._expr_2)


class Sum:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"({self.expr_1} + {self.expr_2})"

    def eval(self, x, y):
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        return self._expr_1 + self._expr_2


class Avg:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"avg({self.expr_1}, {self.expr_2})"

    def eval(self, x, y):
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        return avg(self._expr_1, self._expr_2)


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
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        self._expr_3 = normelize(self.expr_3.eval(x, y))
        return level(self._expr_1, self._expr_2,
                     self._expr_3, self.rnd_f)


class Mix:
    def __init__(self, prob):
        self.expr_1 = ex.build_expr(prob * prob)
        self.expr_2 = ex.build_expr(prob * prob)
        self.expr_3 = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"mix({self.expr_1}, {self.expr_2}, {self.expr_3})"

    def eval(self, x, y):
        self._expr_1 = normelize(self.expr_1.eval(x, y))
        self._expr_2 = normelize(self.expr_2.eval(x, y))
        self._expr_3 = normelize(self.expr_3.eval(x, y))
        return mix(self._expr_1, self._expr_2,
                   self._expr_3)
