#!/usr/bin/env python

import sys

current_userid = None
userid = None

click_count = 0
impression_count = 0

for line in sys.stdin:
    line = line.strip()
    tokens = line.split('\t')

    userid = tokens[11]
    if current_userid != userid:
        print '%s\t%s\t%s\t%s\t%s' % (userid, click_count, impression_count, tokens[12], tokens[13])
        click_count = 0
        impression_count = 0
        current_userid = userid

    click_count += int(tokens[0])
    impression_count += int(tokens[1])

print '%s\t%s\t%s\t%s\t%s' % (userid, click_count, impression_count, tokens[12], tokens[13])
