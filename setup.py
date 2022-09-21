#!/usr/bin/env python

from setuptools import setup, Extension
from Cython.Build import cythonize

"""
Setup script for the Parsley distribution.
"""

extensions = [
    Extension("ometa.runtime", ["ometa/runtime.py"])
]

extension_options = {
    "compiler_directives": {"profile": True}, "annotate": True
}

setup(
    name="Parsley",
    version="1.3",
    url="http://launchpad.net/parsley",
    description="Parsing and pattern matching made easy.",
    author="Allen Short",
    author_email="washort42@gmail.com",
    license="MIT License",
    long_description=open("README").read(),
    packages=["ometa", "terml", "ometa._generated", "terml._generated",
              "ometa.test", "terml.test"],
    py_modules=["parsley"],
    ext_modules=cythonize(extensions, **extension_options),
)
