#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

readme = open('README.md').read()

setup(
    name='heinrichy',
    version='0.23.0',
    description='Personal assistant made especially for GNU/Linux'
                ' because we deserve our own version of siri too!',
    long_description=readme,
    author='michpcx',
    author_email='michpcx@protonmail.ch',
    url='https://github.com/MichPCX/Heinrichy',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'heinrichy = heinrichy.__main__:main'
        ],
    },
    install_requires=['bs4', 'httplib2',
    ],
    license="Copyright",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
