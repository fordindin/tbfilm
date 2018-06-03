#!/usr/bin/env python

import argparse
import config
from unseen import unseen

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

unseen_parser = subparsers.add_parser('unseen')
unseen_parser.set_defaults(func=unseen)  # set the default function to hello

"""
goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('name')
goodbye_parser.set_defaults(func=goodbye)
"""

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function
