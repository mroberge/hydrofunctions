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


1. Fork the `hydrofunctions repo <https://github.com/mroberge/hydrofunctions>`
on GitHub website by clicking on the 'Fork' button near the upper right corner.

2. Install Anaconda if you don't already have it on your system. This includes
a package manager, conda, which replaces pip and also manages virtual
environments, replacing venv, and virtualenv.:

    `Download Anaconda <https://www.continuum.io/downloads>`

3. Much of the rest involves the command line. In the following examples I'll
be using Windows, but this will only affect simple commands like making a new
directory, or changing directory. The important commands are the same on
different platforms.  Also, if you are using Windows, use **cmd.exe** as your
command line instead of PowerShell, which seems to interfere
with one of our tools, conda.)

4. Create a directory for your development work and change directories into
it (I call mine py-dev)::

    `> mkdir py-dev
    `> cd py-dev

5. If you've just installed Anaconda and haven't done anything else with it,
then you can skip ahead to step #7.

6. Create a new conda environment named `my35env`. Include everything we need:
python 3.5, git, and the anaconda set of scientific packages.

    `> conda create -n my35env python=3.5 anaconda git

7. List all of your available environments, and activate my35env.:

    `> conda info -e`  The active environment will have a star next to it.
    `> activate my35env

8. For kicks, check that you've got the right version of python running::

    `> python --version

9. Conda doesn't install from github or pypi, so we'll use pip instead. Use pip
to install hydrofunctions in development mode from github, and to start git
tracking. This command creates a src directory, and puts the source files into
a directory named in the `egg=` part of the url. Then you can edit the source
files and have the edits freshly interpreted again when you `import
hydrofunctions` during a python session. Additionally, git will create a .git
directory inside of the hydrofunctions directory.:

    `> pip install -e git+https://github.com/your_github_name/hydrofunctions.git@master#egg=hydrofunctions

10. Move into the hydrofunctions directory.:

    `> cd src/hydrofunctions

11. Run the automatic tests to make sure everything is hunky-dory::

    `> python setup.py test

12. Start your own branch in git::

    `> git checkout -b name-of-your-bugfix-or-feature

Alternatively, use github's Desktop tool, which does a great job of putting
most of Git's best features into an easy-to-use GUI.

    Download `GitHub Desktop <https://desktop.github.com/>`
    Add the repository we created in step 9:
        -click on the + pull-down > 'Add';
        -find the repository `py-dev/src/hydrofunctions`;
        -confirm with 'Add Repository'.
        -Any changes you make in this directory will appear in this program.

12. Go ahead and make changes to the files now. I like to use Spyder, which you
installed already with anaconda::

    `> spyder

13. After you've made a small change, make sure you didn't break anything by
running the tests again. I find it easiest to run the tests from the command
line. If you tied up the command line when you ran spyder, you can access it
here: Tools > Open Command Prompt.

14. Before you make too many changes, 'commit' what you've done. Ideally, each
group of changes that you put into a commit will be logically related to each
other, and the group of changes will be really small. Make sure that you
explain your changes in the commit message. Use github Desktop. If you use the
command line, then type::

    `> git add .
    `> git commit -m "Your detailed description of your changes."

15. When you are done commiting changes, push your branch and all of the
commits in it to GitHub. This can be done with the 'Sync' button in the
upper right corner. Or, use the command line::

    `> git push origin name-of-your-bugfix-or-feature

16. Finally, submit a pull request to me through the GitHub website.



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
