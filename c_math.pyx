# cython: cdivision=True, language_level=3

from libc.math cimport sin, cos

cpdef double c_sin(double x): return sin(x)
cpdef double c_cos(double x): return cos(x)
cpdef double c_pi(): return 3.14159265359