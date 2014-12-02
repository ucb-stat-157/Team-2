#!/usr/bin/env python

import sys

len_side = 0
instance_index = 0

for line in sys.stdin:
    line = line.strip()

    train_or_user = line.split('\t')
    if len(train_or_user) == 2:
        print line
    if len(train_or_user) == 14:
        print '%s\t%s' % (train_or_user[9], line)
