import os
import re
import sys

sys.path.insert(0, os.path.abspath('..'))
import sphinx
from sphinxcontrib.pylit import meta

# Include todo list
todo_include_todos = True
pylit_include_pylits = True
#pylit_emit_warnings = True

# -- Project information -----------------------------------------------------

project = 'sphinxcontrib-pylit'
copyright = '2020, Roie R. Black'
author = 'Roie R. Black'
version = meta.version

# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.todo',
        'sphinx.ext.autosummary',
        'sphinx.ext.extlinks',
        'sphinx.ext.intersphinx',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
        'sphinx.ext.coverage',
        'sphinx_ext.wordcount',
        'sphinx_ext.programoutput',
        'sphinxcontrib.bibtex',
        'sphinxcontrib.tikz',
]

tikz_proc_suite = 'ImageMagick'

master_doc = 'contents'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_examples']

project = 'PyLiT'
copyright = '2020, Roie R. Black and the Sphinx team'
version = meta.version
release = version
show_authors = True

rst_prolog = """
..  include::   /header.inc
"""

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx13'
html_theme_path = ['_themes']
html_static_path = ['_static']
html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}
html_additional_pages = {'index': 'index.html'}
html_logo = '_static/pylit.svg'

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [('contents', 'pylit.tex', 'PyLiT Documentation',
                    'Roie R. Black', 'manual', 1)]
latex_logo = '_static/pylit.png'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'fontenc': r'\usepackage[LGR,X2,T1]{fontenc}',
    'fontpkg': r'''
\usepackage[sc]{mathpazo}
\usepackage[scaled]{helvet}
\usepackage{courier}
\usepackage{oz}
\substitutefont{LGR}{\rmdefault}{cmr}
\substitutefont{LGR}{\sfdefault}{cmss}
\substitutefont{LGR}{\ttdefault}{cmtt}
\substitutefont{X2}{\rmdefault}{cmr}
\substitutefont{X2}{\sfdefault}{cmss}
\substitutefont{X2}{\ttdefault}{cmtt}
''',
    'passoptionstopackages': '\\PassOptionsToPackage{svgnames}{xcolor}',
    'preamble': '\\DeclareUnicodeCharacter{229E}{\\ensuremath{\\boxplus}}',
    'fvset': '\\fvset{fontsize=auto}',
    # fix missing index entry due to RTD doing only once pdflatex after makeindex
    'printindex': r'''
\IfFileExists{\jobname.ind}
             {\footnotesize\raggedright\printindex}
             {\begin{sphinxtheindex}\end{sphinxtheindex}}
''',
}
latex_show_urls = 'footnote'

# -- Extension interface -------------------------------------------------------

from sphinx import addnodes  # noqa

event_sig_re = re.compile(r'([a-zA-Z-]+)\s*\((.*)\)')


def parse_event(env, sig, signode):
    m = event_sig_re.match(sig)
    if not m:
        signode += addnodes.desc_name(sig, sig)
        return sig
    name, args = m.groups()
    signode += addnodes.desc_name(name, name)
    plist = addnodes.desc_parameterlist()
    for arg in args.split(','):
        arg = arg.strip()
        plist += addnodes.desc_parameter(arg, arg)
    signode += plist
    return name


def setup(app):
    from sphinx.ext.autodoc import cut_lines
    from sphinx.util.docfields import GroupedField
    app.connect('autodoc-process-docstring', cut_lines(4, what=['module']))
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
    app.add_object_type('setuptools-confval', 'setuptools-confval',
                        objname='setuptools configuration value',
                        indextemplate='pair: %s; setuptools configuration value')
    fdesc = GroupedField('parameter', label='Parameters',
                         names=['param'], can_collapse=True)
    app.add_object_type('event', 'event', 'pair: %s; event', parse_event,
                        doc_field_types=[fdesc])

    # workaround for RTD
    from sphinx.util import logging
    logger = logging.getLogger(__name__)
    app.info = lambda *args, **kwargs: logger.info(*args, **kwargs)
    app.warn = lambda *args, **kwargs: logger.warning(*args, **kwargs)
    app.debug = lambda *args, **kwargs: logger.debug(*args, **kwargs)
