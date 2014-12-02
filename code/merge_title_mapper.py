#!/usr/bin/env python

import sys
import fileinput

massive_title_lib = {}

f = open('titleid_tokensid.txt', 'r')
user = f.readline()
while user != '':
    tokens = user.split('\t')
    massive_title_lib[tokens[0]] = '\t' + tokens[1]
    user = f.readline()

for line in sys.stdin:
    instance = line.strip()
    tokens = line.split()
    if tokens[9] in massive_title_lib:
        instance += massive_title_lib[tokens[9]]
        instance = instance.strip()
        print tokens[9] + '\t' + instance

