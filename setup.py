#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['--pep8', '--cov']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    cmdclass={'test': PyTest},
    name='PyKazoo',
    version='0.0a2',
    packages=['pykazoo'],
    install_requires=['requests>=2.7.0'],
    tests_require=['pytest>=2.6.4', 'pytest-cov>=2.1.0', 'pytest-pep8>=1.0.6'],
    url='https://github.com/tnewman/PyKazoo',
    license='MIT',
    author='Thomas Newman',
    author_email='tnewman@users.noreply.github.com',
    description='PyKazoo is a Python API client for 2600hz Kazoo',
)
