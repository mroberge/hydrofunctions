==========================
Guide to Contributing Code
==========================

Contributions are always welcome and greatly appreciated!

You can contribute in many ways:

- Reporting bugs, suggesting features, providing feedback: Use the `issues page`_.
- Adding documentation: add a new notebook, fix a typo, improve the docstrings, mention us in a blog post...
- Adding features, fixing bugs, writing tests: I'll respond to your pull request quickly! Details below!

.. _`issues page`: https://github.com/mroberge/hydrofunctions/issues

Submitting a pull request
-------------------------

- Start by forking mroberge/hydrofunctions into your own GitHub account.
- Working from your own account, move to the Develop branch to see the current state of the project.
- When you are ready to make changes, create a new branch off of Develop with a short, boring, yet
  descriptive name, like "bug-nwis-parsing" or "feature-metric-units".
- Keep your commits small and focused: deal with just one issue at a time.
- Use helpful comments on each commit. Refer to an issue number if possible.
- Try to sync your local commits with GitHub at least once a day. People are curious!
- **Submit your Pull Request early**, while you are just starting to get started! This will:
      - open up a forum in GitHub where people can add comments
      - set up a checklist of things to get done
      - enables automatic unit testing.
      - all your subsequent commits get added to the pull request automatically.
- Don't apologize for mistakes or not being done yet!

Standards for the ideal pull request
------------------------------------
*"We are all in the gutter, but some of us are looking at the stars."* -Oscar Wilde

- If you make a change, add your name to AUTHORS.rst
- Note your change in HISTORY.rst and initial it.
- Use docstrings, illustrate features in a notebook, add a section to docs/usage.rst
- I use 'Black' for code formatting. Follow PEP8 standards!
- Use `Google-style docstrings <https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments>`_
  , described `here <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_.
- Add tests! Lots of tests! Make sure you test your code!
- Your code should work for Python 3.6, 3.7, 3.8, 3.9, & 3.10. This gets tested by the `CI <https://github.com/mroberge/hydrofunctions/actions/workflows/test.yaml>`_


A detailed guide to contributing new code
-----------------------------------------

.. highlight:: doscon

Ready to contribute? Here's how to set up `hydrofunctions` for local development.

#. Fork the `hydrofunctions repo <https://github.com/mroberge/hydrofunctions>`_ on GitHub by clicking the
   'Fork' button near the upper right corner.

#. Open the GitHub page for your fork, and clone it to your local computer where you
   will be doing your coding. To clone your fork, I like to use GitHub's Desktop tool, 
   which does a great job of putting most of Git's best features into an easy-to-use GUI.

   Download `GitHub Desktop <https://desktop.github.com>`_.

   There are two ways to clone your files to your local computer:

   - Starting from the GitHub page for your fork: Select the 'Code' button and select 'Open with GitHub Desktop'
   - or, if you have GitHub Desktop open: File > clone repository...

   These options will set up a local folder on your computer where you can use git while editing
   your version of hydrofunctions.

#. Install Anaconda 3 if you don't already have it on your system. This includes the
   latest version of Python, and a package manager, **conda**, which is an alternative to pip that
   also manages virtual environments, replacing venv, and virtualenv.:

   Download Anaconda: https://www.continuum.io/downloads

#. Much of the rest involves the command line. In the following examples I'll
   be using Windows, but this will only affect simple commands like making a new
   directory, or changing directory. The important commands are the same on
   different platforms.  Also, if you are using Windows, use **cmd.exe** as your
   command line instead of PowerShell, which seems to interfere
   with one of our tools, conda.

#. Create a new conda environment named `my39env`. Include everything we need:
   python 3.9, git, and the anaconda set of scientific packages::

    > conda create -n my36env python=3.9 anaconda git

#. List all of your available environments and activate my36env. The active
   environment will have a star next to it::

    > conda info -e
    > activate my39env

#. For kicks, check that you've got the right version of python running, and
   list all of the packages that you have available to you in this environment::

    > python --version
    > conda list

#. Now we are going to install hydrofunctions using the file from **your** forked version, 
   instead of the standard version from PyPI. To do this, first move into the directory
   where you had GitHub Desktop put your clone::

   > cd GitHub/hydrofunctions

#. We'll use pip to install your files in 'develop' mode using the '-e' flag. 
   Now you can edit the source files and have the edits freshly interpreted again when you
   `import hydrofunctions` during a python session. The [dev] part tells pip to install all
   of the extra requirements that you'll need as a developer::
   
   > pip install -e .[dev]

#. Run the automatic tests to make sure everything is hunky-dory::

    > pytest

#. Before you start improving hydrofunctions with all your fantastic changes, create a new branch.
   Give it a simple name that explains what your change adds::

    > git checkout -b name-of-your-bugfix-or-feature

   Alternatively, use GitHub's Desktop tool:

      - Branch > New branch...

#. Go ahead and make changes to the files now. I like to use VS Code or Spyder, which you
   installed already with anaconda::

    > spyder

#. After you've made a small change, make sure you didn't break anything by
   running the tests again. I find it easiest to run the tests from the command
   line inside the hydrofunctions directory::

    > pytest

#. Before you make too many changes, 'commit' what you've done. Ideally, each
   group of changes that you put into a commit will be logically related to each
   other, and the group of changes will be really small. Make sure that you
   explain your changes in the commit message. Use GitHub Desktop. If you use the
   command line, then type::

     > git add .
     > git commit -m "Your detailed description of your changes."

#. When you are done commiting changes, push your branch and all of the
   commits in it to GitHub. This can be done with the 'Sync' button in the
   upper right corner of Desktop, or use the command line::

    > git push origin name-of-your-bugfix-or-feature

#. Finally, submit a pull request to me through the GitHub website. Your branch
   doesn't need to be done to submit- this just warns people that you exist and
   prevents duplication.



The non-conda version
---------------------
**Caveat emptor:** I haven't tested the following steps recently!

.. highlight:: console

1. Fork the `hydrofunctions` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/hydrofunctions.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv hydrofunctions
    $ cd hydrofunctions/
    $ pip install -e .[dev]

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including
   testing other Python versions with tox::

       $ flake8 hydrofunctions tests
       $ pytest

   or ``$ python -m unittest -v``

   then::

    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.::

    $ pip install flake8
    $ pip install tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.


Tips
----
- The Spyder IDE will highlight bad code formatting if you turn this feature
  on: Tools > Preferences > Code Introspection/Analysis > Real-time code style
  analysis
- Test out your .rst files using the `Online reStructuredText editor <http://rst.ninjs.org>`_
- To run a subset of tests, like the file `test_hydrofunctions.py`::

    $ python -m unittest tests.test_hydrofunctions