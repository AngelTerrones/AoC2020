#!/usr/bin/env python3

import re
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.read().splitlines()

hID = [0 for _ in range(1024)]
for bp in filedata:
    if re.match(r"([FB]{7})([LR]{3})", bp) is None:
        print(f'Invalid BP: {bp}')

    # do the replacement
    tmp = re.sub('B|R', '1', bp)
    tmp = re.sub('F|L', '0', tmp)
    seatID = int(tmp, base=2)
    hID[seatID] = seatID

print(f"Max ID: {max(hID)}")

idx = 1024
seat = 0
while True:
    idx = idx >> 1
    half = hID[idx:]
    seat = half.index(0) + idx
    if hID[seat + 1] != 0 and hID[seat - 1] != 0:
        break

print(seat)
