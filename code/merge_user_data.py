#!/usr/bin/env python

users = [line.strip() for line in open('userid_profile.txt')]

massive_user_lib = {}

for user in users:
    tokens = user.split('\t')
    massive_user_lib[tokens[0]] = '\t' + tokens[1] + '\t' + tokens[2]

instances = [line.strip() for line in open('instances.txt')]

with open("combined_instances.txt", "a") as myfile:
    for instance in instances:
        tokens = instance.split('\t')
        if tokens[11] in massive_user_lib:
            instance += massive_user_lib[tokens[11]]
            myfile.write(instance + '\n')
