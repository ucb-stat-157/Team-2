#!/usr/bin/env python

############ WORK IN PROGRESS ############

###
#  Classify based on gender and age group
#
#  Gender:
#    1 - male
#    2 - female
#    0 - not classified
#  Age:
#    1 - (0, 12]
#    2 - (12, 18]
#    3 - (18, 24]
#    4 - (24, 30]
#    5 - (30, 40]
#    6 - (40, inf)
#
#  Naive attempt at using sklearn and their decision tree
#  classifier package, training, and predictions at the bottom
###

import sys
import fileinput
import random

massive_user_library = {}

massive_ctr_map = {}

for gender in [0, 1, 2]:
    for age in [1, 2, 3, 4, 5, 6]:
        massive_ctr_map[str(gender) + str(age)] = 0.0

user_id = []
gender = []
age = []
ctr = []

users = [line.strip() for line in open('userid_profile.txt')]

for user in users:
    tokens = user.split('\t')
    if tokens[0] not in massive_user_library:
        massive_user_library[tokens[0]] = [tokens[1], tokens[2], 0, 0]
    else:
        values = massive_user_library[tokens[0]]
        values[0] += tokens[1]
        values[1] += tokens[2]


# for line in sys.stdin:
instances = [line.strip() for line in open('training.txt')]
for line in instances:
    words = line.split()

    if words[11] in massive_user_library:
        values = massive_user_library[words[11]]

        values[2] += int(words[0])
        values[3] += int(words[1])

        user_id.append(words[11])


uid = set(user_id)

ctr = []

for i in uid:
    if i in massive_user_library:
        values = massive_user_library[i]
        ctr.append(float(values[2]) / float(values[3]))

        key = str(values[0]) + str(values[1])

        massive_ctr_map[key] = float(values[2]) / float(values[3])

        gender.append(values[0])
        age.append(values[1])

        print '%s\t%s\t%s' % (values[0], values[1], massive_ctr_map[key])

###
#  Attempt at using sklearn. Work in progress
###

# from sklearn import tree
#
# test = [line.strip() for line in open('instances.txt')]
# predictions = []
# for instance in test:
#     words = instance.split('\t')
#     predictions.append(massive_ctr_map[str(random.randint(0, 2)) + str(random.randint(0, 6))])
#
# clf = tree.DecisionTreeClassifier()
#
# samples = []
#
# for i in range(len(age)):
#     samples.append([gender[i], age[i]])
#
# clf = clf.fit(samples, ctr)
# clf.predict(samples)
