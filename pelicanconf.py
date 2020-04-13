#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Swair'
SITENAME = 'Notes'
SITEURL = ''
#THEME = 'TuftePelican'
THEME = 'simple'
PLUGIN_PATHS = ['/Users/swairshah/work/writing/pelican-plugins']
PLUGINS = ['render_math', 'code_include','md_inline_extension'] #'simple_footnotes']
MD_INLINE = {
    #'[+]': 'sidenote-number',
    #'[-]': 'sidenote',
    '[+]': 'dt-note',
    '=+=': 'framed'
    #'|-|': ('color:blue;', 'sidenote'),
}

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
