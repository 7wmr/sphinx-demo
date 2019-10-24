SPHINX DEMO
==========================

Installation
--------------------------

Install the Sphinx tool.

.. code:: bash

   $ pip install sphinx

Install the read the docs theme.

.. code:: bash

   $ pip install sphinx-rtd-theme

Install the HTTP domain extension.

.. code:: bash

   $ pip install sphinxcontrib-httpdomain

Install the confluence builder extension.

.. code:: bash

   $ pip install sphinxcontrib-confluencebuilder

   
Configuration
---------------------------

Create a docs directory in your project then set as current directory.

.. code:: bash

   $ mkdir docs/ && cd docs/

Run the sphinx setup command and answer the prompts.

.. code:: bash

   $ sphinx-quickstart

Update the following line in the file ``docs/source/conf.py`` to use the Read The Docs theme.

.. code:: python

   html_theme = 'sphinx_rtd_theme' # 'alabaster'


References
---------------------------

+------------------------------+-----------------------------------------------------+
| Name                         | Link                                                |
+==============================+=====================================================+
| reStructuredText             | http://docutils.sourceforge.net/rst.html            |
+------------------------------+-----------------------------------------------------+
| Sphinx Doc                   | https://www.sphinx-doc.org                          |
+------------------------------+-----------------------------------------------------+
| Read the docs                | https://docs.readthedocs.io                         |
|                              | https://readthedocs.com/pricing/                    |
+------------------------------+-----------------------------------------------------+
| Confluence builder extension | https://github.com/sphinx-contrib/confluencebuilder |
+------------------------------+-----------------------------------------------------+
