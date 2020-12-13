#!/usr/bin/env python3

import re
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.readlines()

regex = r'(\d+)-(\d+) (.+): (.+)\n'
parsed = [m.group(1, 2, 3, 4)
          for line in filedata
          for m in re.finditer(regex, line)]

is_valid = lambda x, low, high: (low <= x) and (x <= high)  # noqa
counts = [pw for min_, max_, char_, pw in parsed if is_valid(pw.count(char_), int(min_), int(max_))]

print(len(counts))
