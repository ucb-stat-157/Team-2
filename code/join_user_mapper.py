#!/usr/bin/env python

# Author: Kevin Shieh

# Mapper
# Prepend instance lines with user ID

import sys

len_side = 0
instance_index = 0

for line in sys.stdin:
    line = line.strip()

    train_or_user = line.split('\t')
    if len(train_or_user) == 3:
        print line
    if len(train_or_user) == 12:
        print '%s\t%s' % (train_or_user[11], line)
