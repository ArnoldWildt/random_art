# cython: cdivision=True, language_level=3

from libc.math cimport sin, cos, tan, atan, tanh, exp

cpdef double c_sin(double x): return sin(x)
cpdef double c_cos(double x): return cos(x)
cpdef double c_tan(double x): return tan(x)
cpdef double c_atan(double x): return atan(x)
cpdef double c_tanh(double x): return tanh(x)
cpdef double c_exp(double x): return exp(x)
cpdef double c_pi(): return 3.14159265359