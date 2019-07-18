
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
#     packages=['biocertainty'],
    package_dir={'biocertainty':
                 'biocertainty'},   
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7'
    ],
    test_suite='tests',
    install_requires=requirements,
    include_package_data = True,
    data_files=[('', ['data/training_set.csv'])],
    package_data = {'': ['data/training_set.csv']},
    setup_requires=[
        # dependency for `python setup.py test`
        'pytest-runner',
        # dependencies for `python setup.py build_sphinx`
        'sphinx',
        'recommonmark'
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ]
)
