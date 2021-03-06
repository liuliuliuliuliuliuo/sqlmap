#!/usr/bin/env python2

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.common import getOrds
from lib.core.compat import xrange
from plugins.generic.syntax import Syntax as GenericSyntax

class Syntax(GenericSyntax):
    @staticmethod
    def escape(expression, quote=True):
        """
        >>> Syntax.escape("SELECT 'abcdefgh' FROM foobar") == "SELECT CHAR(97)||CHAR(98)||CHAR(99)||CHAR(100)||CHAR(101)||CHAR(102)||CHAR(103)||CHAR(104) FROM foobar"
        True
        """

        def escaper(value):
            return "||".join("CHAR(%d)" % _ for _ in getOrds(value))

        return Syntax._escape(expression, quote, escaper)
