#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
SITENAME = 'Code Bebop'
SITEURL = ''
SUMMARY_MAX_LENGTH = 0

# Time and Date
TIMEZONE = 'Asia/Ho_Chi_Minh'
DEFAULT_DATE_FORMAT = '%d %b %Y'

# Metadata
AUTHOR = 'kinoubenkyou'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<title>.*)'

# Feed
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 4

# Translation
DEFAULT_LANG = 'en'

# Theme
THEME = 'kelican'
SOCIAL = ()
