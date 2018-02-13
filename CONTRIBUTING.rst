.. highlight:: shell

============
Contributing
============

Contributions are always welcome and greatly appreciated!

You can contribute in many ways:

- Reporting bugs, suggesting features, providing feedback: Use the `issues page`_.
- Adding documentation: add a new notebook, fix a typo, docstrings, mention us in a blog post...
- Adding features, fixing bugs, writing tests: I'll respond to your pull request quickly! Details below!

.. _`issues page`: https://github.com/mroberge/hydrofunctions/issues

Submitting a Pull Request
-------------------------

- Start by forking from the Develop branch. Give your fork a descriptive name: "parsing_bugfix"
- Keep your commits small and focused: try to edit just one file at a time and deal
  with one issue at a time.
- Use helpful comments on each commit.
- If you make a change, add your name to AUTHORS.rst
- If you add a feature, update the docs! Use docstrings and update the README.rst
- Add tests! Lots of tests! Make sure you test your code!
- Your code should work for Python 3.4, 3.5, & 3.6. Check
  https://travis-ci.org/mroberge/hydrofunctions/pull_requests
  and make sure that the tests pass for all supported Python versions.

A Detailed Guide to Submitting a Pull Request
---------------------------------------------

Ready to contribute? Here's how to set up `hydrofunctions` for local development.

#. Fork the `hydrofunctions repo <https://github.com/mroberge/hydrofunctions>`_ on GitHub by clicking the
   'Fork' button near the upper right corner.

#. Install Anaconda if you don't already have it on your system. This includes
   a package manager, conda, which replaces pip and also manages virtual
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

#. If you've just installed Anaconda and haven't done anything else with it,		
   then you can skip ahead to step #7.		

#. Create a new conda environment named `my35env`. Include everything we need:		
   python 3.5, git, and the anaconda set of scientific packages::		

    > conda create -n my35env python=3.5 anaconda git		

#. List all of your available environments, and activate my35env::	

    > conda info -e # The active environment will have a star next to it.		
    > activate my35env		

#. For kicks, check that you've got the right version of python running::

    > python --version

#. Conda doesn't install from github or pypi, so we'll use pip instead. Use pip
   to install hydrofunctions in development mode from github, and to start git
   tracking. This command creates a src directory, and puts the source files into
   a directory named in the `egg=` part of the url. Then you can edit the source
   files and have the edits freshly interpreted again when you `import
   hydrofunctions` during a python session. Additionally, git will create a `.git`
   directory inside of the hydrofunctions directory. ::	

    > pip install -e git+https://github.com/your_github_name/hydrofunctions.git@master#egg=hydrofunctions	

#. Move into the hydrofunctions directory::

    > cd src/hydrofunctions

#. Run the automatic tests to make sure everything is hunky-dory::

    > python setup.py test

#. Start your own branch in git::

    > git checkout -b name-of-your-bugfix-or-feature

   Alternatively, use github's Desktop tool, which does a great job of putting most of
   Git's best features into an easy-to-use GUI.

   Download `GitHub Desktop <https://desktop.github.com>`_.
   Add the repository we created in step 9:

        - click on the + pull-down > 'Add';
        - find the repository `py-dev/src/hydrofunctions`
        - confirm with 'Add Repository'.
        - Any changes you make in this directory will appear in this program.

#. Go ahead and make changes to the files now. I like to use Spyder, which you
   installed already with anaconda::

    > spyder

#. After you've made a small change, make sure you didn't break anything by
   running the tests again. I find it easiest to run the tests from the command
   line. If you tied up the command line when you ran spyder, you can access it

#. Before you make too many changes, 'commit' what you've done. Ideally, each
   group of changes that you put into a commit will be logically related to each		
   other, and the group of changes will be really small. Make sure that you		
   explain your changes in the commit message. Use github Desktop. If you use the		
   command line, then type::

     > git add .
     > git commit -m "Your detailed description of your changes."

#. When you are done commiting changes, push your branch and all of the
   commits in it to GitHub. This can be done with the 'Sync' button in the		
   upper right corner. Or, use the command line::

    > git push origin name-of-your-bugfix-or-feature

#. Finally, submit a pull request to me through the GitHub website.





The Short Version
-----------------

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

 		  
 -To run a subset of tests, like the file `test_hydrofunctions.py`::


    $ python -m unittest tests.test_hydrofunctions