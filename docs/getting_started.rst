.. _getting-started-chapter:

=================
 Getting started
=================

.. contents::
   :local:

This guide walks through getting a development environment set up
to allow you to contribute to plugincheck.


Getting the requirements
========================

1. Download and install git if you don't have it already:
   http://git-scm.com/

   .. Note::

      **Windows users:** When you install git, make sure to choose
      "Checkout as-is, commit Unix-style line endings". If you don't,
      then you'll end up with Windows-style line endings in your
      checkout and Fjord won't work in the virtual machine.

2. Download and install PostgreSQL if you don't have it already:
   https://www.postgresql.org/


Getting the Source
==================

If you have a GitHub account, you should fork the plugincheck repository and
then clone your fork::

    $ git clone https://github.com/<USERNAME>/plugincheck.git
    $ cd plugincheck

If you do not have a GitHub account, that's ok! Clone the official
plugincheck repository this way::

    $ git clone https://github.com/mozilla/plugincheck.git
    $ cd plugincheck

This creates a directory called ``plugincheck/``. We'll call that the
"plugincheck repository top-level directory".


Setting up an Environment
=========================

It is strongly recommended to run plugincheck in a virtual environment, which
is a tool to isolate Python environments from eachother and the system. It
makes local development much easier, especially when working on multiple
projects.

To create a virtual environment::

    $ virtualenv venv

which creates a virtualenv named "venv" in your current directory (which should
be the root of the git repo. Now activate the virtualenv::

    $ source venv/bin/activate

You'll need to run this command every time you work on plugincheck, in every
terminal window you use.


Installing dependencies
=======================

Python Packages
---------------

All the pure-Python requirements are provided in the requirements
directory. We use a tool called ``peep`` to install packages and make sure
versions are pinned. ::

    $ ./peep.sh install -r requirements.txt


If you have any issues installing via ``peep``, be sure you have the required
header files from the packages listed in the requirements section above.

For more information on ``peep``, refer to the
`README <https://github.com/erikrose/peep>`_ on the Github page for the project.


Configuration and Setup
=======================

settings_local.py
-----------------

There is a file called ``settings_local.py.dist`` in the ``plugincheck/``
directory. This contains a sample set of local settings. Copy the file, name
it ``settings_local.py``. and edit it, following the instructions within.
Don't forget to change ``<db_user>`` to your actual database user. Also,
add a password if the database account you are using requires one.

Additionally, you can copy and modify any settings from
``plugincheck/settings.py`` into ``plugincheck/settings_local.py`` and the
value will override the default.


Database
--------

You defined a database connection in ``plugincheck/settings_local.py``.

Now create the database::

    $ psql -U <db_user> template1
    template1=# CREATE DATABASE plugincheck;
    template1=# \q


Then we create the tables and run migrations::

    $ ./manage.py migrate


Finally, we create a superuser to log into plugincheck::

    $ ./manage.py createsuperuser


That's it!


Editing code and testing it
===========================

Plugincheck is a Django project. We use the Django runserver to run the
website to test it manually.

To launch the Django runserver::

    $ ./manage.py runserver 0.0.0.0:8000


Then on your host computer, use your browser and go to
``http://127.0.0.1:8000``. You should see the site.


Running the unit tests
----------------------

Running the test suite is easy::

    $ ./manage.py test


