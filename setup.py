#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    numpy,
    pandas
]

test_requirements = [
    nose2
]

setup(
    name='hydrofunctions',
    version='0.1.1',
    description="A suite of convenience functions for exploring water data in IPython.",
    long_description=readme + '\n\n' + history,
    author="Martin Roberge",
    author_email='mroberge.whois@gmail.com',
    url='https://github.com/mroberge/hydrofunctions',
    packages=[
        'hydrofunctions',
    ],
    package_dir={'hydrofunctions':
                 'hydrofunctions'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='hydrofunctions hydrology USGS stream gauge water NWIS',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Utilities'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
