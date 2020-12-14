#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.read().split('\n\n')

acc = 0
for group in filedata:
    merge = group.replace('\n', '')
    acc += len(set(merge))

print(acc)
