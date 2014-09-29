#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='shardgather',
    version='1.0.0',
    description='A tool for executing SQL queries against sharded databases',
    long_description=readme + '\n\n' + history,
    author='Kevin Jing Qiu',
    author_email='kevin@idempotent.ca',
    url='https://github.com/kevinjqiu/shardgather',
    packages=[
        'shardgather',
    ],
    package_dir={'shardgather': 'shardgather'},
    include_package_data=True,
    install_requires=map(str.strip, open('requirements.txt').readlines()),
    license="BSD",
    zip_safe=False,
    keywords='shardgather',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
