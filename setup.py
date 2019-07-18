
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
    packages= find_packages('biocertainty'),
    package_dir={'biocertainty': 'biocertainty'},   
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=requirements,
    data_files=[('lib/python2.7/site-packages/biocertainty', ['data/training_set.csv', 'data/model.json', 'data/model.h5'])],
    package_data = {'lib/python2.7/site-packages/biocertainty': ['data/training_set.csv', 'data/model.json', 'data/model.h5']},
    include_package_data = True,
    setup_requires=[
        # dependency for `python setup.py test`
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'recommonmark'
    ]
)
