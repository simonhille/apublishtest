# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -- #
# ------------------------- #
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "test"
copyright = "Simon Hans Hille"
author = "Simon Hans Hille"
release = "2025"

# -- General configuration -- #
# --------------------------- #
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Note that it is somehow important that napoleon comes first
# see github.com/tox-dev/sphinx-autodoc-typehints
extensions = [
    "myst_nb",
    "sphinx.ext.napoleon",  # Latex docstring style
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",  # extracts taglines from docstrings
    "sphinx.ext.extlinks",  # shortcuts to create hyperlinks
]

# -- sphinx.ext.autodoc -- #
autodoc_member_order = "bysource"

# -- sphinx.ext.intersphinx -- #
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),  # Link to Python standard library
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "tenpy": ("https://tenpy.readthedocs.io/en/latest/", None),
    "pfapack": ("https://pfapack.readthedocs.io/en/latest", None),
}


# -- sphinx.ext.extlinks -- #
# For later


# -- Something else -- #
# --------------------- #
templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -- #
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,  # Keeps the sidebar expanded
    "style_external_links": True,  # Adds external link icons
}

def autodoc_process_docstring(app, what, name, obj, options, lines):
    # doc_links = {
    #     "TeNpy": (
    #         "TeNpy",
    #         "https://tenpy.readthedocs.io/en/latest/index.html",
    #     ),
    # }
    # Add more here as needed
    for i in range(len(lines)):
        # lines[i] = lines[i].replace("np.", "numpy.") # For longer links
        lines[i] = lines[i].replace("np.", "~numpy.")  # For shorter links
        # lines[i] = lines[i].replace("List[", "~typing.List[")
        # A mapping from full class path to (display name, link)
        # for full_path, (short_name, url) in doc_links.items():
        #     lines[i] = lines[i].replace(full_path, f"`{short_name} <{url}>`_")

# -- Extension configuration ------------------------------------------
def setup(app):
    app.connect("autodoc-process-docstring", autodoc_process_docstring)
