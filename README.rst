Aalto ASR preprocessing package
===============================

|License| |Tests|

|pre-commit| |Black|

.. |License| image:: https://img.shields.io/github/license/aalto-speech/aalto-asr-preprocessor
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Tests| image:: https://github.com/aalto-speech/aalto-asr-preprocessor/workflows/Tests/badge.svg
   :target: https://github.com/aalto-speech/aalto-asr-preprocessor/actions?workflow=Tests
   :alt: Tests
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

Features
--------

* Rule-based preprocessing recipes for ASR
* Recipes are validated with tests

Requirements
------------

* Python >= 3.8
* Click

Installation
------------

To install the Aalto ASR preprocessor,
clone the repository and run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/aalto-speech/aalto-asr-preprocessor.git
   $ cd aalto-asr-preprocessor
   $ pip install .

Usage
-----

For detailed instructions, see `Usage`_
or type ``aalto-prep --help`` in terminal.

Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.

License
-------

Distributed under the terms of the MIT_ license,
*Aalto ASR preprocessor* is free and open source software.

Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.

Credits
-------

This project uses `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.


.. _@cjolowicz: https://github.com/cjolowicz
.. _MIT: http://opensource.org/licenses/MIT
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/aalto-speech/aalto-asr-preprocessor/issues
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: docs/index.rst
