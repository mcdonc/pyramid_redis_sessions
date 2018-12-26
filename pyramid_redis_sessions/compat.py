# -*- coding: utf-8 -*-

"""
Compatability module for various pythons and environments.
"""

import sys

# PY3 is left as bw-compat but PY2 should be used for most checks.
PY2 = sys.version_info[0] == 2


if PY2: # pragma: no cover
    text_type = unicode
    binary_type = str
else: # pragma: no cover
    text_type = str
    binary_type = bytes

try:
    import cPickle
except ImportError: # pragma: no cover
    # python 3 pickle module
    import pickle as cPickle

def text_(s, encoding='latin-1', errors='strict'): # pragma: no cover
    """ If ``s`` is an instance of ``binary_type``, return
    ``s.decode(encoding, errors)``, otherwise return ``s``"""
    if isinstance(s, binary_type):
        return s.decode(encoding, errors)
    return s

def bytes_(s, encoding='latin-1', errors='strict'): # pragma: no cover
    """ If ``s`` is an instance of ``text_type``, return
    ``s.encode(encoding, errors)``, otherwise return ``s``"""
    if isinstance(s, text_type):
        return s.encode(encoding, errors)
    return s
