#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.readlines()

dx = 3  # horizontal move
dy = 1  # vertical move
x0 = 0  # initial x
y0 = 0  # initial y
nxt_x = x0 + dx
nxt_y = y0 + dy
len_x = len(filedata[0]) - 1  # ignore \n
len_y = len(filedata)

ded = 0
while nxt_y < len_y:
    if filedata[nxt_y][nxt_x] == '#':
        ded += 1
    # move
    nxt_x = (nxt_x + dx) % len_x
    nxt_y = nxt_y + dy

print(ded)
