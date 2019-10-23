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


Configuration
---------------------------

Create a docs directory in your project.

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

+------------------+------------------------------------------+
| Name             | Link                                     |
+==================+==========================================+
| reStructuredText | http://docutils.sourceforge.net/rst.html |
+------------------+------------------------------------------+
| Sphinx Doc       | https://www.sphinx-doc.org               |
+------------------+------------------------------------------+
| Read the docs    | https://docs.readthedocs.io              |
+------------------+------------------------------------------+
