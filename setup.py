import pytest
import setuptools
from distutils.core import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errorno = pytest.main('--cov=pykazoo --pep8')
        raise SystemExit(errorno)

setup(
    name='PyKazoo',
    version='0.0.a0',
    packages=setuptools.find_packages(),
    package_data={'': ['LICENSE.md', 'README.md', '.coveragerc']},
    install_requires=open('requirements.txt').readlines(),
    url='https://github.com/tnewman/PyKazoo',
    license='MIT',
    author='Thomas Newman',
    description='PyKazoo is a Python API client for 2600hz Kazoo',
    cmdclass={'test': PyTest},
)
