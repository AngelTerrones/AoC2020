#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.readlines()


movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # (dx, dy)
x0 = 0  # initial x
y0 = 0  # initial y
len_x = len(filedata[0]) - 1  # ignore \n
len_y = len(filedata)

result = 1
for dx, dy in movements:
    nxt_x = x0 + dx
    nxt_y = y0 + dy

    ded = 0
    while nxt_y < len_y:
        if filedata[nxt_y][nxt_x] == '#':
            ded += 1
        # move
        nxt_x = (nxt_x + dx) % len_x
        nxt_y = nxt_y + dy

    result *= ded

print(result)
