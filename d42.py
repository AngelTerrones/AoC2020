#!/usr/bin/env python3

import re
import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    filedata = f.readlines()

# add space at the end to signal end of key:value
kw = [('byr', r'(.*?)byr:(200[0-2]|19[2-9][0-9]) '),
      ('iyr', r'(.*?)iyr:(2020|201[0-9]) '),
      ('eyr', r'(.*?)eyr:(2030|202[0-9]) '),
      ('hgt', r'(.*?)hgt:((19[0-3]|1[5-8][0-9])cm|(7[0-6]|6[0-9]|59)in) '),
      ('hcl', r'(.*?)hcl:(#[0-9a-f]{6}) '),
      ('ecl', r'(.*?)ecl:(amb|blu|brn|gry|grn|hzl|oth) '),
      ('pid', r'(.*?)pid:(\d{9}) ')]  # ignore 'cid'
data = []
valid = 0
for line in filedata:
    if line != '\n':
        # partial data, add
        data.append(line.replace('\n', ' '))
    else:
        # check passport
        valid += 1
        passport = ''.join(data)
        for field, regex in kw:
            match = re.match(regex, passport)
            if match is None:
                # print(f'Passport invalid. Field "{field}" invalid: {passport}')
                valid -= 1
                break

        data.clear()

print(f'valid = {valid}')
