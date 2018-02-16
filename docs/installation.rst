.. highlight:: shell

============
Installation
============


Easy Install
============

To install HydroFunctions, run this command in your terminal:

.. code-block:: console

    $ pip install hydrofunctions

This is the preferred method to install HydroFunctions, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


Why Use Anaconda?
=================

Anaconda is a free, open-source Python distribution. It bundles important
scientific software like Jupyter notebooks and the Spyder IDE all into one
pre-configured, pre-compiled download, along with a huge number of scientific
libraries (packages). It also includes a tool, `conda`, which manages and
updates these packages. Conda also creates 'environments', which are isolated
installations of Python, just in case your ArcGIS software uses a different
version of Python than some other piece of software.

If you want to install Jupyter notebooks at the same time that you install
hydrofunctions, or if you want to use Python 2 and 3 at the same time, or if
you had problems when you tried the Easy Install instructions above... then use
these instructions here:

0. `Download and install Anaconda<https://www.continuum.io/downloads>`_.
Choose the version of Anaconda that is right for your operating system. I
advise using Python 3.4 or higher.

Once you have Anaconda installed, much of the following will be done from the
command line. For Windows users, use cmd.exe to do this instead of PowerShell,
which I've found has a strange interaction with conda.


Easy Anaconda Install
=====================

*For people who are using Anaconda because they just wanted an easy way to get
all of the software installed at once.*

1. From the command prompt, install hydrofunctions with Pip.

.. code-block:: console

    $ pip install hydrofunctions

That's it!


Safe Anaconda Install for People Having Problems
================================================

*For people who like to write their own code, or have Python already installed
for something else, or who had difficulties.*

1. From the command prompt, create a new environment with packages for 
Python 3.6 and jupyter notebooks::

        > conda create -n myenv python=3.6 jupyternb nb_conda

2. List all of the environments that you have available::

        > conda info -e

3. The active environment will have a star next to it. To activate a 
different environment, type::

         > activate name_of_environment

4. To test that you have the correct version of python::

         > python --version

5. install hydrofunctions using the pip tool::

         > pip install hydrofunctions

Getting Started Once Everything Is Installed
============================================

You now have several ways to run Python. If you installed Anaconda, then you
will have icons that will start the following programs. Otherwise, just open
a command prompt and type the following:

      - for a command line interface: `python`
      - for an enhanced command line: `ipython`
      - to use the Spyder IDE: `spyder`
      - or to use a Jupyter Notebook: 'jupyter notebook`

To use hydrofunctions in your python code, make sure that one of your first
lines says this::

         > import hydrofunctions as hf


Installations for People Wanting to Contribute Code to Hydrofunctions
=====================================================================

You are a brave and special person indeed. WE SALUTE YOU:

Follow the directions in the `Contributors Guide <http://hydrofunctions.readthedocs.io/en/master/contributing.html>`_
