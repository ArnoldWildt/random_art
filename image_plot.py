import sys
import numpy as np

from c_math import *
from math_functions import *
from PIL import Image


class ImageGenerator():
    def __init__(self, size):
        self.size = size
        self.cords = self.cord_list()

    def create_canvas(self, expr):
        self.canvas = np.zeros((self.size, self.size, 1), dtype='uint8')

        for pair in self.cords:
            self.eval_func(expr, *pair)

        return np.rot90(self.canvas, k=3)

    def cord_list(self):
        # Faster than a generator function. For this usecase.
        out = []
        for x in range(self.size):
            for y in range(self.size):
                out.append((x, y))
        return out

    def eval_func_(self, args):
        return eval_func(*args)

    def eval_func(self, expr, px, py):
        # Normalize to (-1 - 1)
        x = float(px - (self.size / 2)) / (self.size / 2)
        y = -float(py - (self.size / 2)) / (self.size / 2)

        z = eval(expr) if isinstance(expr, type(str())) else expr.eval(x, y)

        # Scale to (0 - 255).
        intensity = z * 127.5 + 127.5

        self.canvas[px][py] = int(intensity)

    def plot_image(self, red_expr, green_expr, blue_expr):
        red_canvas = self.create_canvas(red_expr)
        green_canvas = self.create_canvas(green_expr)
        blue_canvas = self.create_canvas(blue_expr)
        rgb_canvas = np.concatenate(
            (red_canvas, green_canvas, blue_canvas), axis=2)
        return Image.fromarray(rgb_canvas)
