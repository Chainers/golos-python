# coding=utf-8
import os
import sys

from setuptools import find_packages
from setuptools import setup


assert sys.version_info[0] == 3 and sys.version_info[1] >= 5, "steep-golos requires Python 3.5 or newer"


def readme_file():
    return 'README.rst' if os.path.exists('README.rst') else 'README.md'


def license_file():
    return 'LICENSE' if os.path.exists('LICENSE') else 'LICENSE.txt'


setup(
    name='steep-golos',
    version='0.0.14',
    author='@steepshot',
    author_email='steepshot.org@gmail.com',
    description='Fork of official python STEEM library for Golos blockchain',
    license=open(license_file()).read(),
    keywords='golos steep-golos',
    url='https://github.com/Chainers/steep-golos',
    long_description=open(readme_file()).read(),
    packages=find_packages(exclude=['scripts']),
    setup_requires=['pytest-runner'],
    tests_require=['pytest',
                   'pep8',
                   'pytest-pylint',
                   'yapf',
                   'sphinx',
                   'recommonmark',
                   'sphinxcontrib-restbuilder',
                   'sphinxcontrib-programoutput',
                   'pytest-console-scripts'],

    install_requires=[
        'appdirs',
        'ecdsa',
        'pylibscrypt',
        'scrypt',
        'pycrypto',
        'requests',
        'urllib3',
        'certifi',
        'ujson',
        'w3lib',
        'maya',
        'toolz',
        'funcy',
        'langdetect',
        'diff-match-patch',
        'prettytable',
        'voluptuous',
        'python-dateutil',
        'websocket-client'
    ],
    entry_points={
        'console_scripts': [
            'golospy=golos.cli:legacy',
            'golospiston=golos.cli:legacy',
        ]
    })
