#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.read()

data = [int(x) for x in filedata.split('\n') if x != '']

sol = [(x, y, z, x*y*z)
       for i, x in enumerate(data)
       for j, y in enumerate(data[i:])
       for z in data[i + j:]
       if x + y + z == 2020]
print(sol)
