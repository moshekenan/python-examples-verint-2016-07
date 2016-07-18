"""
Regular expressions no 1
"""
import sys
import os
import argparse
import re

# Assign description to the help doc
parser = argparse.ArgumentParser(description='Find value of a key.')

# Add arguments
parser.add_argument('-s', '--sourcefile', type=str, help='source definitions file', required=True)
parser.add_argument('-k', '--key', type=str, help='key for search', required=True)

# Array for all arguments passed to script
args = parser.parse_args()

# Assign args to variables
src_file = args.sourcefile
key_to_find = args.key

with open(src_file, "r") as fin:
    for line in fin:
        m = re.search(r'(\w+)\s*=\s*(\w+)', line)
        if m is not None:
            if m.group(1) == key_to_find:
                print "The value of key: '{}' is '{}'".format(key_to_find, m.group(2))
                break


