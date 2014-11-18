#!/usr/bin/env python

###
#  Simple reducer that groups and averages ctr's for
#  same grouped users
###

from operator import itemgetter
import sys

current_gender = 0
current_age = 0
current_ctr = 0
count = 0

for line in sys.stdin:
    instance = instance.strip()
    values = instance.split('\t', 2)

    if current_gender != values[0] and current_age != values[1]:
        print '%s\t%s\t%s' % (current_gender, current_age, current_ctr / float(count))
        current_gender = values[0]
        current_age = values[1]
        current_ctr = values[2]
        count = 1
    else:
        current_ctr += values[1]
        count += 1
