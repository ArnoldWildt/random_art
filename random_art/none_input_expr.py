import random


class VarX:
    def __str__(self):
        return "x"

    def eval(self, x, y):
        return x


class VarY:
    def __str__(self):
        return "y"

    def eval(self, x, y):
        return y


class Zero:
    def __str__(self):
        return "0"

    def eval(self, x, y):
        return 0


class One:
    def __str__(self):
        return "1"

    def eval(self, x, y):
        return 1


class MinusOne:
    def __str__(self):
        return "-1"

    def eval(self, x, y):
        return -1


class RdnConst:
    def __init__(self):
        self.const = random.random()

    def __str__(self):
        return str(self.const)

    def eval(self, x, y):
        return self.const
