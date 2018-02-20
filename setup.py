#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'pandas',
    'requests'
]

test_requirements = [
    # 'pytest'
    # 'nose2' doesn't add any extra functionality for me right now.
]

setup(
    name='hydrofunctions',
    version='0.1.5',
    description="A suite of convenience functions for exploring water data in IPython.",
    long_description=readme + '\n\n' + history,
    author="Martin Roberge",
    author_email='mroberge.whois@gmail.com',
    url='https://github.com/mroberge/hydrofunctions',
    packages=find_packages(),
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
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Utilities'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
