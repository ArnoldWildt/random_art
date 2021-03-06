from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name='Random art cython module',
    ext_modules=cythonize("./random_art/*.pyx"),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)
