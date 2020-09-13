# -*- coding: utf-8 -*-
#

# import os, sys
# sys.path.insert(0, os.path.abspath(os.path.join('.', 'ext')))

import sphinx_rtd_theme

extensions = ['sphinx.ext.todo',
              'sphinx_rtd_theme',
              'sphinx.ext.mathjax']

project = 'CARS Cloud Data'
copyright = 'Public Domain'
release = '0.1'
html_title  = 'CARS Cloud Data'
html_short_title = 'millenia.cars.aps.anl.gov/cloud'


pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8'

master_doc = 'index'

exclude_trees = ['_build']

add_function_parentheses = True
add_module_names = False

html_static_path = ['_static']
html_favicon = '_static/uchicago_logo.ico'

language = None
html_theme_options = {
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False, # True,
    # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False
}
