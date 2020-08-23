import math
import sys
import numpy as np

from math_functions import *
from PIL import Image


class ImageGenerator():
    def create_canvas(self, expr, size):
        self.canvas = np.zeros((size, size, 1), dtype='uint8')

        for pair in self.xy_gen(size):
            self.eval_func(expr, size, *pair)

        return np.rot90(self.canvas, k=3)

    def xy_gen(self, size):
        for x in range(size):
            for y in range(size):
                yield (x, y)

    def eval_func(self, expr, size, px, py):
        # Normalize to (-1 - 1)
        x = float(px - (size / 2)) / (size / 2)
        y = -float(py - (size / 2)) / (size / 2)

        z = eval(expr) if isinstance(expr, type(str())) else expr.eval(x, y)

        # Scale to (0 - 255).
        intensity = z * 127.5 + 127.5

        self.canvas[px][py] = int(intensity)

    def plot_image(self, red_expr, green_expr, blue_expr, size):
        red_canvas = self.create_canvas(red_expr, size)
        green_canvas = self.create_canvas(green_expr, size)
        blue_canvas = self.create_canvas(blue_expr, size)
        rgb_canvas = np.concatenate(
            (red_canvas, green_canvas, blue_canvas), axis=2)
        return Image.fromarray(rgb_canvas)
