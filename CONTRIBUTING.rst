==========================
Guide to Contributing Code
==========================

Contributions are always welcome and greatly appreciated!

You can contribute in many ways:

- Reporting bugs, suggesting features, providing feedback: Use the `issues page`_.
- Adding documentation: add a new notebook, fix a typo, improve the docstrings, mention us in a blog post...
- Adding features, fixing bugs, writing tests: I'll respond to your pull request quickly! Details below!

.. _`issues page`: https://github.com/mroberge/hydrofunctions/issues

Submitting a Pull Request
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
      - enables automatic commit testing with TravisCI.
      - all your subsequent commits get added to the pull request automatically.
- Don't apologize for mistakes or not being done yet!

Standards for the Ideal Pull Request
------------------------------------
*"We are all in the gutter, but some of us are looking at the stars."* -Oscar Wilde

- If you make a change, add your name to AUTHORS.rst
- Note your change in HISTORY.rst and initial it.
- Use docstrings, illustrate features in a notebook, add a section to docs/usage.rst
- Follow PEP8 standards in your code!
- Use `Google-style docstrings <https://google.github.io/styleguide/pyguide.html?showone=Comments#Comments>`_
  , described `here <http://www.sphinx-doc.org/en/stable/ext/example_google.html>`_.
- Add tests! Lots of tests! Make sure you test your code!
- Your code should work for Python 3.4, 3.5, & 3.6. This gets tested in `TravisCI <https://travis-ci.org/mroberge/hydrofunctions/pull_requests>`_


A Detailed Guide to Contributing New Code
-----------------------------------------

Ready to contribute? Here's how to set up `hydrofunctions` for local development.

#. Fork the `hydrofunctions repo <https://github.com/mroberge/hydrofunctions>`_ on GitHub by clicking the
   'Fork' button near the upper right corner.

#. Install Anaconda 3 if you don't already have it on your system. This includes the
   latest version of Python, and 
   a package manager, **conda**, which replaces pip and also manages virtual
   environments, replacing venv, and virtualenv.:

   Download Anaconda: https://www.continuum.io/downloads

#. Much of the rest involves the command line. In the following examples I'll
   be using Windows, but this will only affect simple commands like making a new
   directory, or changing directory. The important commands are the same on
   different platforms.  Also, if you are using Windows, use **cmd.exe** as your
   command line instead of PowerShell, which seems to interfere
   with one of our tools, conda.

#. Create a directory for your development work and change directories into
   it (I call mine py-dev)::

     > mkdir py-dev
     > cd py-dev

#. Create a new conda environment named `my36env`. Include everything we need:
   python 3.6, git, and the anaconda set of scientific packages::

    > conda create -n my36env python=3.6 anaconda git

#. List all of your available environments and activate my36env. The active
   environment will have a star next to it::

    > conda info -e		
    > activate my36env		

#. For kicks, check that you've got the right version of python running, and
   list all of the packages that you have available to you in this environment::

    > python --version
    > conda list

#. Conda doesn't install packages located on github or pypi, so we'll use pip to install the source
   files from the fork you created in your GitHub account. We use the -e flag to install packages 
   in development mode. This creates a src directory with 
   a subdirectory named in the `egg=` part of the url. Now you can edit the source
   files and have the edits freshly interpreted again when you `import
   hydrofunctions` during a python session. Additionally, git will create a `.git`
   directory inside of the hydrofunctions directory. ::	

    > pip install -e git+https://github.com/your_github_name/hydrofunctions.git@develop#egg=hydrofunctions	

#. Move into the hydrofunctions directory::

    > cd src/hydrofunctions

#. Run the automatic tests to make sure everything is hunky-dory::

    > python setup.py test

#. Start your own branch in git::

    > git checkout -b name-of-your-bugfix-or-feature

   Alternatively, use GitHub's Desktop tool, which does a great job of putting most of
   Git's best features into an easy-to-use GUI.

   Download `GitHub Desktop <https://desktop.github.com>`_.
   Add the repository we created in step 8:

        - click on the + pull-down > 'Add';
        - find the repository `py-dev/src/hydrofunctions`
        - confirm with 'Add Repository'.
        - Any changes you make in this directory will appear in this program.

#. Go ahead and make changes to the files now. I like to use Spyder, which you
   installed already with anaconda::

    > spyder

#. After you've made a small change, make sure you didn't break anything by
   running the tests again. I find it easiest to run the tests from the command
   line.

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



The Non-Conda Version
---------------------
**Caveat emptor:** I haven't tested the following steps recently!

1. Fork the `hydrofunctions` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/hydrofunctions.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv hydrofunctions
    $ cd hydrofunctions/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including
   testing other Python versions with tox::

       $ flake8 hydrofunctions tests
       $ python setup.py test
    
   or ``$ python -m unittest -v`` or  ``$ py.test`` or ``$ nose2``

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