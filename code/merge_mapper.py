#!/usr/bin/env python

import sys
import fileinput

massive_user_lib = {}

# f = open('userid_profile.txt', 'r')
# user = f.readline()
# while user != '':
#     tokens = user.split('\t')
#     massive_user_lib[tokens[0]] = '\t' + tokens[1] + '\t' + tokens[2]
#     user = f.readline()

for line in sys.stdin:
    instance = line.strip()
    tokens = line.split()
    if tokens[11] in massive_user_lib:
        instance += massive_user_lib[tokens[11]]
        print instance

