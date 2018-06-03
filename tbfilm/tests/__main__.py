#!/usr/bin/env python

"""
Run unit tests. This is invoked by:

$ python -m tbfilm.tests
"""

import contextlib
import optparse
import os
import ssl
import sys
import tempfile
try:
    from urllib.request import urlopen  # py3
except ImportError:
    from urllib2 import urlopen

from tbfilm.tests import run_suite

def main():
    usage = "python -m tbfilm.tests [opts]"
    parser = optparse.OptionParser(usage=usage, description="run unit tests")

    opts, args = parser.parse_args()
    run_suite()

main()
