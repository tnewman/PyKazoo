#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import setuptools
from distutils.core import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        pytest.main(['--pep8', '--cov'])

setup(
    cmdclass={'test': PyTest},
    name='PyKazoo',
    version='0.0a2',
    packages=['pykazoo'],
    install_requires=['requests'],
    tests_require=['pytest', 'pytest-cov', 'pytest-pep8'],
    url='https://github.com/tnewman/PyKazoo',
    license='MIT',
    author='Thomas Newman',
    author_email='tnewman@users.noreply.github.com',
    description='PyKazoo is a Python API client for 2600hz Kazoo',
)
