#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import setuptools
from distutils.core import setup

setup(
    name='PyKazoo',
    version='0.0a1',
    packages=['pykazoo'],
    install_requires=['requests>=2.7.0'],
    url='https://github.com/tnewman/PyKazoo',
    license='MIT',
    author='Thomas Newman',
    author_email='tnewman@users.noreply.github.com',
    description='PyKazoo is a Python API client for 2600hz Kazoo',
)
