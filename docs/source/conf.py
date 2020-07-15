# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'CNE Runbooks'
copyright = '2020, Contino'
author = 'Richard Neave'

# The full version, including alpha/beta/rc tags
release = 'v1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.confluencebuilder',
    'sphinx.ext.autodoc',
    'sphinx-jsonschema',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' # 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/icon.png'

logo_only = True

# -- Extensions -------------------------------------------------

# Custom styling
def setup(app):
  app.add_stylesheet('style.css')
  app.add_javascript("custom.js")
  app.add_javascript("https://cdn.jsdelivr.net/npm/clipboard@1/dist/clipboard.min.js")

# Todos extension
todo_include_todos = False

# Confluence extension
confluence_publish = True
confluence_master_homepage = False
confluence_purge = False
confluence_max_doc_depth = 5
confluence_page_hierarchy = True
confluence_space_name = 'CNE'
confluence_parent_page = 'SRE'
confluence_publish_postfix = ' [azdo]'

confluence_server_url = 'https://7wmr.atlassian.net/wiki/'
confluence_server_user = os.environ['CONFLUENCE_SERVER_USER']
confluence_server_pass = os.environ['CONFLUENCE_SERVER_PASS']

# # https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/configuration.html#confluence-server-auth
# from requests_oauthlib import OAuth1

# client_key = ''
# client_secret = ''
# resource_owner_key = ''
# resource_owner_secret = ''

# confluence_server_auth = OAuth1(client_key,
#     client_secret=client_secret,
#     resource_owner_key=resource_owner_key,
#     resource_owner_secret=resource_owner_secret)
