#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='pythonsite-dotenv',
    url="www.wiezebier.be",
    version='0.1dev',
    install_requires=['django-dotenv'],
    description="Extend environment when invoking python",
    author="Dries Desmet",
    author_email="dries@urga.be",
    zip_safe=False,
    py_modules=['sitecustomize'],
)