#!/usr/bin/env python2

"""
Copyright (c) 2006-2013 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import sys

PYVERSION = sys.version.split()[0]

if PYVERSION >= "3" or PYVERSION < "2.6":
    exit("[CRITICAL] incompatible Python version detected ('%s'). For successfully running sqlmap you'll have to use version 2.6 or 2.7 (visit 'http://www.python.org/download/')" % PYVERSION)