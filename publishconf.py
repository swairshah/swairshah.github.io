#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://swairshah.github.io'
#RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

THEME = 'TuftePelican'
PLUGIN_PATHS = ['/Users/swairshah/work/writing/pelican-plugins']
PLUGINS = ['render_math', 'code_include','md_inline_extension'] #'simple_footnotes']
DELETE_OUTPUT_DIRECTORY = True
SUMMARY_MAX_LENGTH=0

MD_INLINE = {
    #'[+]': 'sidenote-number',
    #'[-]': 'sidenote',
    '[+]': 'dt-note',
    '=+=': 'framed'
    #'|-|': ('color:blue;', 'sidenote'),
}

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
