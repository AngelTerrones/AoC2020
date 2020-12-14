#!/usr/bin/env python3

import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    filedata = f.readlines()

kw = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # ignore 'cid'
data = []
valid = 0
for line in filedata:
    if line != '\n':
        # partial data, add
        data.append(line)
    else:
        # check passport
        passport = ''.join(data)
        checks = [field in passport for field in kw]
        valid += 0 if False in checks else 1
        print(passport)
        data.clear()

print(valid)
