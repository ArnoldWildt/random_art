# cython: cdivision=True, language_level=3

cpdef float dip(float x):
    """Function that looks like the dip in a line."""
    return 1 - 2 / (1 + x*x) ** 8


cpdef float tip(x: float):
    """Function that looks like the tip of a triangle."""
    return 1 - 2 * abs(x)


cpdef float parabola(float x):
    """Function that looks like the parabola."""
    return x * x


cpdef float pow(float x):
    """Function that returns x to the power of x."""
    return abs(x) ** x


cpdef float sqrt(float x):
    """Function that returns squareroot of x."""
    return abs(x) ** 0.5


cpdef float modulo(float x1, float x2):
    """Function that returns modulo of x1 by x2 """
    if x2 == 0.0:
        return 0.0
    return x1 % x2


cpdef float quotient(float x1, float x2):
    """Function that returns quotient of x1 devided by x2"""
    if abs(x1) > abs(x2):
        x1, x2 = x2, x1
    if x2 == 0.0:
        return 0.0
    return x1 / x2


def avg(*args):
    """Function that returns the average of all args given."""
    return sum(args) / len(args)


cpdef float level(float x1, float x2, float x3, float rnd_f):
    """Function that returns (x2 if x1 < rnd_f else x3)"""
    return x2 if x1 < rnd_f else x3


cpdef float mix(float x1, float x2, float x3):
    """Function that returns a mix of the Inputs"""
    x3 = 0.5 * (x3 + 1.0)
    return x3 * x1 + (1 - x3) * x2

cpdef float normelize(float x):
    """Function that normelzies a float to -1 to 1."""
    if -1 < x < 1:
        return x
    return 1 if x > 1 else -1