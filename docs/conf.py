# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.

import os, sys, time, subprocess, runpy, cgi
sys.path.append(os.path.abspath(".."))

# Try to get a version number.
# N.B. Similar code appears in setup.py.
# We don't use the dirty flag here because Read the Docs may dirty
# the repository while generating the documentation.
VERSIONFILE='../hy/version.py'
try:
    hy_version = (subprocess.check_output
        (["git", "describe", "--tags"])
        .decode('ASCII').strip()
        .replace('-', '+', 1).replace('-', '.'))
except (subprocess.CalledProcessError, OSError):
    if os.path.exists(VERSIONFILE):
        hy_version = runpy.run_path(VERSIONFILE)['__version__']
    else:
        hy_version = "unknown"

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'hy'
copyright = u'2013-%s, Paul Tagliamonte' % time.strftime('%Y')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ".".join(hy_version.split(".")[:-1])
# The full version, including alpha/beta/rc tags.
release = hy_version
hy_descriptive_version = cgi.escape(hy_version)
if "+" in hy_version:
    hy_descriptive_version += " <strong style='color: red;'>(unstable)</strong>"

exclude_patterns = ['_build', 'coreteam.rst']

pygments_style = 'sphinx'

import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_use_smartypants = False
html_show_sphinx = False

html_context = dict(
    hy_descriptive_version = hy_descriptive_version)
