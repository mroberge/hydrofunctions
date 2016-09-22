.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/mroberge/hydrofunctions/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

HydroFunctions could always use more documentation, whether as part of the
official HydroFunctions docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/mroberge/hydrofunctions/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `hydrofunctions` for local development.


1. Run virtualenv, which will: create a new directory my_new_venv, copy your python executable into it, and install some basic tools.::

    $ virtualenv my_new_venv
    $ cd my_new_venv

2. Fork the `hydrofunctions` repo on GitHub website by clicking on the 'Fork' button.
3. Use Git to create a new directory hydrofunctions, and clone hydrofunctions into it.::

    $ git clone https://github.com/your_github_name_here/hydrofunctions.git
    $ cd hydrofunctions

4. Install hydrofunctions in development mode::

    $ python setup.py develop

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass all of the existing tests, plus the ones you wrote for your new code::

    $ python setup.py test

6. You can also use flake8 to check that your materials follow PEP8 guidelines, and tox to test other versions of python::

    $ flake8 hydrofunctions tests
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.::

    $ pip install flake8
    $ pip install tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 2.6, 2.7, 3.3, 3.4 and 3.5, and for PyPy. Check
   https://travis-ci.org/mroberge/hydrofunctions/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests, like the file `test_hydrofunctions.py`::


    $ python -m unittest tests.test_hydrofunctions
