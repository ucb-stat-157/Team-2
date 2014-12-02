#!/usr/bin/env python

import sys

current_userid = None
userid = None
training_lines = []
user_tokens = None

for line in sys.stdin:
    line = line.strip()
    train_or_tokens = line.split('\t')
    line = line.split('\t', 1)

    userid = line[0]
    # print train_or_tokens
    if current_userid != userid:
        if len(training_lines) > 0 and user_tokens != None:
            for inst in training_lines:
                print '%s\t%s' % (inst, user_tokens)
            training_lines = []
            user_tokens = None

        if len(train_or_tokens) == 3:
            user_tokens = line[1]
        if len(train_or_tokens) == 13:
            training_lines.append(line[1])

        current_userid = userid

    else:
        if len(train_or_tokens) == 2:
            user_tokens = line[1]
        if len(train_or_tokens) == 13:
            training_lines.append(line[1])

for inst in training_lines:
    print '%s\t%s' % (inst, user_tokens)
