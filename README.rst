===============================
HydroFunctions
===============================


.. image:: https://img.shields.io/pypi/v/hydrofunctions.svg
        :target: https://pypi.python.org/pypi/hydrofunctions

.. image:: https://img.shields.io/travis/mroberge/hydrofunctions.svg
        :target: https://travis-ci.org/mroberge/hydrofunctions

.. image:: https://readthedocs.org/projects/hydrofunctions/badge/?version=latest
        :target: https://hydrofunctions.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
        :target: https://github.com/mroberge/hydrofunctions/blob/master/LICENSE
        :alt: MIT license

A suite of convenience functions for exploring water data in IPython.




Features
--------

* Retrieves stream gauge data from the USGS NWIS service
* Extracts into a Pandas dataframe or dict
* Read the `online manual <http://hydrofunctions.readthedocs.io/en/master>`_

* Still under development! More features to come!

Basic Usage
-----------




Installation
------------

Hydrofunctions depends upon Pandas and numerous other scientific packages
for Python. The easiest way to get started is by using
`Anaconda <https://www.continuum.io/open-source-core-modern-software>`_,
which puts everything you need into
`one easy download <https://www.continuum.io/downloads>`_. Choose
the version of Anaconda that is right for your operating system, and I would
advise using Python 3.5.

Once you have Anaconda installed, much of the following will be done from the
command line. For Windows users, use cmd.exe to do this instead of PowerShell,
which I've found has a strange interaction with conda.

1. list your available environments::

         > conda info -e

2. The active environment will have a star next to it. 
   To activate a different environment, type::

         > activate name_of_environment

3. Test that you have the correct version of python::

         > python --version

4. install git::

         > conda install git

5. install hydrofunctions using the pip tool::

         > pip install git+https://github.com/your_github_name/hydrofunctions.git@master#egg=hydrofunctions

6. You can now run python in one of several 
   environments:

      - from the command line: `python`
      - from an enhanced command line: `ipython`
      - in the Spyder IDE: `spyder`
      - or using Jupyter: 'jupyter notebook`

7) Use hydrofunctions in your python code this way::

         > import hydrofunctions as hf

Credits
---------

Visit `Hydropy <https://github.com/stijnvanhoey/hydropy>`_, which builds upon Pandas for enhanced data selection and plotting of hydrology data.

`WellApplication <https://github.com/inkenbrandt/WellApplication>`_ provides functions for working with dataloggers and USGS well data.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
