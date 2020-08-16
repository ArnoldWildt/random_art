from PIL import Image
from math_functions import *
import numpy as np
import math


def create_canvas(expr, size, is_str):
    # canvasWidth = 2 * size
    # canvas = Image.new("L", (canvasWidth, canvasWidth))
    canvas = np.zeros((size, size, 1), dtype='uint8')
    for px in range(size):
        for py in range(size):
            # Normalize to (-1 - 1)
            x = float(px - (size / 2)) / (size / 2)
            y = -float(py - (size / 2)) / (size / 2)

            if is_str:
                z = eval(expr)
            else:
                z = expr.eval(x, y)

            # Scale to (0 - 255).
            intensity = int(z * 127.5 + 127.5)
            canvas[px][py] = intensity

    return np.rot90(canvas, k=3)


def plot_image(red_expr, green_expr, blue_expr, size, is_str=False):
    red_canvas = create_canvas(red_expr, size, is_str)
    green_canvas = create_canvas(green_expr, size, is_str)
    blue_canvas = create_canvas(blue_expr, size, is_str)
    rgb_canvas = np.concatenate(
        (red_canvas, green_canvas, blue_canvas), axis=2)
    return Image.fromarray(rgb_canvas)
