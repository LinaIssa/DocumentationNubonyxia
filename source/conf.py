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
import os
import pathlib
import sys
#sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Nubonyxia'
copyright = '2024, Bercy Hub'
author = 'Bercy Hub'

# The full version, including alpha/beta/rc tags
release = '0.1'
highlight_options  = {'default': {'lexers.python.PythonLexer'},
                     }
numfig = True  # to enable image ref 




# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
pygments_style = 'sphinx'

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
html_theme = 'furo' #pydata-sphinx-theme

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_title = ' '

html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitLab",
            
            # URL where the link will redirect
            "url": "https://forge.dgfip.finances.rie.gouv.fr/bercyhub/nubonyxia/DocumentationNubonyxia",
            
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-gitlab",

#            "announcement"    : "", to make an announcement

            
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }],
    "logo_only": True,
    
    "logo": {
        
        # Alt text for blind people
        "alt_text"    : "Nubonyxia Documentation - Home",
        "image_light" : "_static/logo_Nubonyxia.png",
        "image_dark"  : "_static/logo_Nubonyxia.png",
    },
    "show_nav_level"  : 2
}
# Workaround to rmove sidebar when using pydata-sphinx-theme
#html_sidebars = {
#    "firststeps": [],
#    "methode": [],
#    "minio": [],
#    "services": [],
#    "usecase": []
#}

html_logo = "images/logo_Nubonyxia.png"
html_css_files   = ["mycss.css"]
html_static_path = ['_static']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_design',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary', 
  #  'sphinxcontrib.osexample',
    'sphinx_tabs.tabs'
]

autosectionlabel_prefix_document = True


rst_prolog = """
.. role:: python(code)
  :language: python
  :class: highlight
.. _Boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
.. _S3Fs: https://s3fs.readthedocs.io/en/latest/
.. _pandas: https://pandas.pydata.org
.. _Nubonyxia: https://nubonyxia.incubateur.finances.rie.gouv.fr
.. _Harbor: https://harbor.lab.incubateur.finances.rie.gouv.fr
.. _MinIO: https://minio-console.lab.incubateur.finances.rie.gouv.fr/ 
.. _Vault: https://nubonyxia.incubateur.finances.rie.gouv.fr/account/vault
.. _SSP Cloud: https://datalab.sspcloud.fr
.. _Kubernetes: https://kubernetes.io/fr/docs/concepts/overview/what-is-kubernetes/
.. _forge: https://forge.dgfip.finances.rie.gouv.fr/ 
.. _RIE: https://www.renater.fr/projets-et-partenariats/projets-specifiques/le-reseau-interministeriel-de-letat-rie/ 


"""
