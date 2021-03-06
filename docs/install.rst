
**WARNING**
===========

  **If you are updating from 4.0.1** please:

  Uninstall `isbntools` (``sudo pip uninstall isbntools``)
  and then **delete** all files ``isbntools*`` in your ``site-packages`` directory, including the folder
  ``isbntools``

  Then install `isbntools 4.2.3` (``sudo pip install isbntools``).

  **NOTE**: in Windows (or in OSX/Linux for an user install) you shouldn't use ``sudo pip ...``, just ``pip ...``


Install
=======

From the command line enter (in some cases you have to preced the
command with ``sudo``):


.. code-block:: bash

    $ pip install isbntools

or:

.. code-block:: bash

    $ easy_install isbntools

or:

.. code-block:: bash

    $ pip install isbntools-4.2.3.tar.gz

(first you have to download the file!)

You should check if the install was successful, by enter:

.. code-block:: bash

    $ isbntools




Portable Version (Windows and Linux)
------------------------------------

**If you are on a Windows system (NOW for Linux too)**,
you can download a portable_ version that **doesn't need python** and gives you
access to the scripts. However, doesn't support add-ins or customization!



    **Instructions**:

    1. unzip the file and put the file ``isbn.exe`` in a folder.
    2. go to that folder and open a command line.
    3. run ``isbn help`` to get further instructions.



.. _github: https://github.com/xlcnd/isbntools/issues

.. _range: https://www.isbn-international.org/range_file_generation

.. _here: http://isbndb.com/api/v2/docs

.. _wcat: https://github.com/xlcnd/isbntools/blob/master/isbntools/dev/wcat.py

.. _isbndb: https://github.com/xlcnd/isbntools/blob/master/isbntools/dev/isbndb.py

.. _see: https://github.com/xlcnd/isbntools/blob/master/isbntools/dev/merge.py

.. _help: https://github.com/xlcnd/isbntools/issues/8

.. _portable: http://bit.ly/1i8qatY

.. _twitter: https://twitter.com/isbntools
