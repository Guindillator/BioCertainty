#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(name='biocertainty',	
    version='0.1.0',	
    description='Python package that provides the certainty about biomedical statements.',	
    url='https://github.com/Guindillator/BioCertainty',	
    author='Mario Prieto',	
    author_email='mario.prieto@upm.es',	
    license='Wilkinson Laboratory',
    zip_safe=False
)
