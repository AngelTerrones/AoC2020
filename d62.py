#!/usr/bin/env python3

import sys
import string

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.read()[:-1].split('\n\n')

acc = 0
for group in filedata:
    choices = group.split('\n')
    common = set(string.ascii_lowercase)
    for choice in choices:
        common = common & set(choice)

    acc += len(common)

print(acc)
