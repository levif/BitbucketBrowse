|License|

******************
Bitbucket browsing
******************

This project aims to list Bitbucket repositories.

This script prints all the repository urls that can be fetched from
Bitbucket Cloud as a member of those repositories.

You have to create an App password on Bitbucket portal first to let
the script execute on your behalf.

Installation
============

Virtual environment::

  python -m virtualenv ./venv
  source venv/bin/activate
  pip install -r requirements.txt

Launching
=========

You'll need the `username` and `password` (App password recommended at it can be easily revoked)

Commands::

  python bitbucket-browse.py
  Enter your Bitbucket cloud username:
  Enter your app password (set in Bitbucket web interface):
  git@bitbucket.org:username/my_repo_1.git
  git@bitbucket.org:username/my_repo_2.git


Authors
=======

BitbucketBrowse was created by `Cédric Le Dillau`.

License
=======

GNU General Public License v3.0 or later.

See `LICENSE <LICENSE>`_ to see the full text.

.. |License| image:: https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg
   :target: LICENSE
   :alt: Repository License
