from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext_modules = [
    Extension(
	name='data_producer._mask',
        sources=['data_producer.pyx'],
	extra_link_args=['-L/usr/lib/x86_64-linux-gnu/'],
    )
]

setup(ext_modules = cythonize(ext_modules))

