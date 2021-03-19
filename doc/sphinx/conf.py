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
from os.path import sep as pathsep
from datetime import datetime as dt
from subprocess import run as __exe__
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Helper Functions --------------------------------------------------------
def __get_commit_sha__(branch=str('HEAD')):
    """Get the SHA1 sum of the current commit.

    Args:
        branch(str): Branch to run command against. (default str('HEAD'))
    Returns:
        str: SHA1 sum of the current commit."""
    # Define the command we want to use in order to get the current commit SHA hash.
    commit_cmd = list(['git',
                       'rev-parse',
                       str(branch)])
    # Execute command for grabbing current commit SHA, capturing output from STDOUT.
    commit_run = __exe__(commit_cmd,
                         capture_output=True)
    # Get just the captured STDOUT from executing the git command.
    commit_out = commit_cmd.stdout
    # Decode the output captured from STDOUT so that it's just a regular string.
    commit_sha = str(commit_out.decode())
    # Return STDOUT as a string.
    return str(commit_sha)

# -- Project information -----------------------------------------------------

project = 'qbitkit'
author = f'{project} Team'
copyright = f'{dt.now().year}, {author}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.apidoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.coverage",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ".rst"
master_doc = "index"

autoclass_content = "both"
autodoc_member_order = "bysource"
default_role = "py:obj"

html_theme = "sphinx_rtd_theme"
htmlhelp_basename = "{}doc".format(project)

napoleon_use_rtype = False

repo_root_path = f"..{pathsep}..{pathsep}"

apidoc_module_dir = f"..{pathsep}..{pathsep}{project}"
apidoc_output_dir = "_apidoc"
apidoc_excluded_paths = [f"..{pathsep}..{pathsep}"]
apidoc_separate_modules = True
apidoc_module_first = True
apidoc_extra_args = ["-f", "--implicit-namespaces", "-H", "API Reference"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build',
                    'Thumbs.db',
                    '.DS_Store',
                    '__MACOSX']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']