#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def relative2absolute(input, old, new):
    """ Replaces every instance of rel_key in input with absolute_stem.
    Use this to change relative links to absolute links in pypi.
    """
    pattern = old
    p = re.compile(pattern)
    output = p.sub(new, input)
    return output


relative = r'_static'
stem = r'https://raw.githubusercontent.com/mroberge/hydrofunctions/master/_static'
readme = relative2absolute(readme, relative, stem)

requirements = [
    'matplotlib',
    'numpy',
    'pandas',
    'requests',
    'IPython'
]

test_requirements = [
    # Use coverage to run coverage tests locally.
    # Do not list codecov here. It is only listed in .travis.yml because
    # we only run codecov during Travis CI builds.
    'coverage'
]

setup(
    name='hydrofunctions',
    version='0.1.6',
    description="A suite of convenience functions for exploring water data in a Jupyter Notebook.",
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
    project_urls={
            'Documentation': 'https://hydrofunctions.readthedocs.io',
            'Source': 'https://github.com/mroberge/hydrofunctions',
            'Latest': 'https://github.com/mroberge/hydrofunctions/tree/develop',
            'Tracker': 'https://github.com/mroberge/hydrofunctions/issues'
            },
    classifiers=[
        'Development Status :: 3 - Alpha',
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
