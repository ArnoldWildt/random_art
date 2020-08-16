def dip(x: float) -> float:
    """Function that looks like the dip in a line."""
    return 1 - 2 / (1 + x*x) ** 8


def tip(x: float) -> float:
    """Function that looks like the tip of a triangle."""
    return 1 - 2 * abs(x)


def parabola(x: float) -> float:
    """Function that looks like the parabola."""
    return x * x


def pow(x: float) -> float:
    """Function that returns x to the power of x."""
    return abs(x) ** x


def sqrt(x: float) -> float:
    """Function that returns squareroot of x."""
    return abs(x) ** 0.5


def modulo(x1: float, x2: float) -> float:
    """Function that returns modulo of x1 by x2 """
    if x2 == 0.0:
        return 0.0
    return x1 % x2


def quotient(x1: float, x2: float) -> float:
    """Function that returns quotient of x1 devided by x2"""
    if x2 == 0.0:
        return 0.0
    return x1 / x2


def avg(*args) -> float:
    """Gets the average of args.

    Returns:
        float: averaged value of args.
    """
    return sum(args) / len(args)


def level(x1: float, x2: float, x3: float, rnd_f: float) -> float:
    """Function that returns (x2 if x1 < rnd_f else x3)"""
    return x2 if x1 < rnd_f else x3


def mix(x1: float, x2: float, x3: float) -> float:
    """Function that returns a mix of the Inputs"""
    x3 = 0.5 * (x3 + 1.0)
    return x3 * x1 + (1 - x3) * x2
