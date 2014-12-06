#!/usr/bin/env python

# Author: Kevin Shieh

# Reducer
# Join on feature ID by appending feature tokens to instance lines
# Assumed that input data is sorted

import sys

current_id = None
feature_id = None
training_lines = []
feature_tokens = None

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    line = line.split(None, 1)

    feature_id = line[0]
    if current_id != feature_id:
        if len(training_lines) > 0 and feature_tokens != None:
            for inst in training_lines:
                print '%s\t%s' % (inst, feature_tokens)
            training_lines = []
            feature_tokens = None

        if len(tokens) == 2:
            feature_tokens = line[1]
        if len(tokens) == 14:
            training_lines.append(line[1])

        current_id = feature_id

    else:
        if len(tokens) == 2:
            feature_tokens = line[1]
        if len(tokens) == 14:
            training_lines.append(line[1])
