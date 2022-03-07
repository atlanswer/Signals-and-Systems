# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '信号与系统'
author = 'X. Zhao'
copyright = 'CC BY-NC-SA 4.0'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# If set to a major.minor version string like '1.1', Sphinx will
# compare it with its version and refuse to build if it is too old.
# Default is no requirement.
needs_sphinx = '4.3'

# If true, Sphinx will warn about all references where the target
# cannot be found. Default is False. You can activate this mode
# temporarily using the `-n` command-line switch.
nitpicky = True

language = 'zh_CN'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'numpydoc',
    'sphinx.ext.githubpages',
]

# MyST parser configuration
myst_enable_extensions = ['dollarmath']

# numpydoc config
numpydoc_use_plots = True
numpydoc_validation_checks = {'all'}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']
