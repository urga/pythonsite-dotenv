#!/usr/bin/env python

from setuptools import setup
import version

setup(
    name='pythonsite-dotenv',
    url="https://github.com/urga/pythonsite-dotenv",
    version=version.getVersion(),
    install_requires=['django-dotenv', ],
    description="Extend environment when invoking python",
    author="Dries Desmet",
    author_email="dries@urga.be",
    packages=['sitecustomize', ],
)