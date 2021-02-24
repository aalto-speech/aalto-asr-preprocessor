The Aalto ASR preprocessor
==========================

.. toctree::
   :hidden:
   :maxdepth: 1

   License <license>
   Reference <reference>

Aalto ASR preprocessor is a tool for rule-based preprocessing of texts used in ASR.
It uses recipes made of regular expressions to process the input.
The preprocessor also takes in a list of accepted characters,
and raises an error if the output contains characters outside that list.

The output of the recipes is validated with tests,
check the `tests` folder in the repository for examples.

The tool has a simple command line client, see more in :ref:`usage`.
You can also write your own script to access :py:func:`aalto_asr_preprocessor.preprocessor.apply`.

Currently, the preprocessor has recipes for one language: Finnish.

Installation
------------

To install the Aalto ASR preprocessor,
clone the repository and run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/aalto-speech/aalto-asr-preprocessor.git
   $ cd aalto-asr-preprocessor
   $ pip install .


.. _usage:

Usage
-----

Aalto ASR preprocessor can be used through the command line:

.. code-block:: console

   $ aalto-prep [OPTIONS] INPUT OUTPUT RECIPEFILE

.. option:: INPUT

   A file containing the text to preprocess.
   Alternatively, you can use `-` to pipe input from stdin.

.. option:: OUTPUT

   A file to write the output to.
   Alternatively, you can use `-` to get output printed in stdout/terminal.

.. option:: RECIPEFILE

   A python file that defines the list of accepted characters,
   and regular expressions used to preprocess the input.

.. option:: --add-linefeed

   Add linefeed to the end of each input row.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
