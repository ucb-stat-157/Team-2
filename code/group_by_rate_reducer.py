#!/usr/bin/env python

# Author: Kevin Shieh

# Reducer
# Reduce into corresponding 0.1 width buckets

import sys

running_rate = 0.1
running_clicks = 0
running_impressions = 0
running_info = None
header = None

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    current_rate = float(tokens[0])

    if current_rate >= running_rate and abs(running_rate - 1.0) > 0.01:
        print '%s\t%s\t%s' % (running_rate, running_clicks, running_impressions)
        while current_rate >= running_rate and running_rate <= 0.9:
            running_rate += 0.1
        running_clicks = 0
        running_impressions = 0

    running_clicks += int(tokens[2])
    running_impressions += int(tokens[3])

print '%s\t%s\t%s' % (running_rate, running_clicks, running_impressions)
