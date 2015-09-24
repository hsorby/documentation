#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'OpenCMISS Project'
SITENAME = u'OpenCMISS Website'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

# Use the custom theme
THEME = "./themes/ocmiss"

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
EXTRA_TEMPLATES_PATHS = ['../app/']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

DIRECT_TEMPLATES = ["index","categories"]

PAGINATED_DIRECT_TEMPLATES = ['News']

TEMPLATE_PAGES = {}

READERS = {'html':None }

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_URL = '{category}/{slug}.html'

AUTHOR_SAVE_AS = ''

ARCHIVE_SAVE_AS = ''

CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/index.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = 'slug.html'