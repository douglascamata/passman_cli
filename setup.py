#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()
doclink = """
Documentation
-------------

The full documentation is at http://passman-cli.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='passman_cli',
    version='0.0.1',
    description='A command line interface to get data from your Passman instance',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Douglas Camata',
    author_email='d.camata@gmail.com',
    url='https://github.com/douglascamata/passman_cli',
    packages=find_packages(exclude=['docs', 'tests', 'samples']),
    entry_points={
        'console_scripts': [
            'passman = passman_cli.entrypoint:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        "requests",
        "pycryptodome",
        "sjcl"
    ],
    dependency_links=[
        "https://github.com/arnuschky/sjcl/tarball/master#egg=sjcl"
    ],
    license='MIT',
    zip_safe=False,
    keywords='passman_cli, passman, security',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
