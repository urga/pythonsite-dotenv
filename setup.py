#!/usr/bin/env python

from setuptools import setup


setup(
    name='pythonsite-dotenv',
    url="https://github.com/urga/pythonsite-dotenv",
    version='0.1dev',
    install_requires=['django-dotenv', ],
    description="Extend environment when invoking python",
    author="Dries Desmet",
    author_email="dries@urga.be",
    zip_safe=False,
    packages=['sitecustomize', ],
)