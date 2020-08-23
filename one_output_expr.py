import expr_functions as ex
from c_math import *
from math_functions import *


class CosPi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_cos(c_pi() * {self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return c_cos(c_pi() * self._expr)


class SinPi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_sin(c_pi() * {self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return c_sin(c_pi() * self._expr)


class Cos2Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_cos(2 * c_pi() * {self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return c_cos(2 * c_pi() * self._expr)


class Sin2Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_sin(2 * c_pi() * {self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return c_sin(2 * c_pi() * self._expr)


class Sin:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_sin({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return c_sin(self._expr)


class Cos:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"c_cos({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return c_cos(self._expr)


class Dip:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"dip({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return dip(self._expr)


class Tip:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"tip({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return tip(self._expr)


class Parabola:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"parabola({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return parabola(self._expr)


class Pow:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"pow({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return pow(self._expr)


class Sqrt:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"sqrt({self.expr})"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return sqrt(self._expr)


class Pi:
    def __init__(self, prob):
        self.expr = ex.build_expr(prob * prob)

    def __repr__(self):
        return f"{self.expr} * c_pi()"

    def eval(self, x, y):
        self._expr = normelize(self.expr.eval(x, y))
        return self._expr * c_pi()

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
