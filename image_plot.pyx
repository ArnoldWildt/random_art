# cython: cdivision=True, language_level=3

import math
import sys
import numpy as np
cimport numpy as np

from math_functions import *
from PIL import Image

ctypedef fused str_obj:
    str
    object

cdef class ImageGenerator():
    cdef int size
    cdef np.ndarray cords
    cdef np.ndarray canvas
    def __init__(self, int size):
        self.size = size
        self.cords = self.cord_list()

    cpdef np.ndarray create_canvas(self, str_obj expr):
        self.canvas = np.zeros((self.size, self.size, 1), dtype='uint8')
        cdef np.ndarray pair
        cdef int x, y
        for pair in self.cords:
            x, y = pair
            self.eval_func(expr, x, y)

        return np.rot90(self.canvas, k=3)

    cpdef np.ndarray cord_list(self):
        # Faster than a generator function. For this usecase.
        cdef np.ndarray out = np.zeros([self.size * self.size, 2], dtype='uint8')
        cdef int x, y
        cdef int counter = 0
        for x in range(self.size):
            for y in range(self.size):
                out[counter][0] = x
                out[counter][1] = y
                counter += 1
        return out

    cpdef eval_func(self, str_obj expr, int px, int py):
        # Normalize to (-1 - 1)
        cdef float x = float(px - (self.size / 2)) / (self.size / 2)
        cdef float y = -float(py - (self.size / 2)) / (self.size / 2)

        cdef float z = eval(expr) if isinstance(expr, type(str())) else expr.eval(x, y)

        # Scale to (0 - 255).
        cdef float intensity = z * 127.5 + 127.5

        self.canvas[px][py] = int(intensity)

    cpdef plot_image(self, str_obj red_expr, str_obj green_expr, str_obj blue_expr):
        cdef np.ndarray red_canvas = self.create_canvas(red_expr)
        cdef np.ndarray green_canvas = self.create_canvas(green_expr)
        cdef np.ndarray blue_canvas = self.create_canvas(blue_expr)
        cdef np.ndarray rgb_canvas = np.concatenate(
            (red_canvas, green_canvas, blue_canvas), axis=2)
        return Image.fromarray(rgb_canvas)