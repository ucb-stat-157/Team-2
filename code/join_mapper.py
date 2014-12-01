#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()

    train_or_user = line.split('\t')
    if len(train_or_user) == 3:
        print line
    if len(train_or_user) == 12:
        print '%s\t%s' % (train_or_user[11], line)
