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

is_valid = lambda pw, char, low, high: (pw[low] == char) != (pw[high] == char)  # noqa XOR
counts = [pw for min_, max_, char_, pw in parsed if is_valid(pw, char_, int(min_) - 1, int(max_) - 1)]

print(len(counts))
