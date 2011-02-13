#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
import os.path as p

VERSION = open(p.join(p.dirname(p.abspath(__file__)), 'VERSION')).read().strip()

setup(
    name='exchequer',
    version=VERSION,
    description='Easy table formatting in Python and on the command-line.',
    author='Zachary Voase',
    author_email='z@zacharyvoase.com',
    url='http://github.com/zacharyvoase/exchequer',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    test_suite='exchequer._get_tests',
)
