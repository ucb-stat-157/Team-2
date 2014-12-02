import random

###
# Randomly samples ARG2 lines from file ARG0 and places them in fle ARG1
###

filename = sys.argv[0]

num_lines = sum(1 for line in open(filename))


indices = random.sample(xrange(num_lines), sys.argv[2])

users = [line.strip() for line in open(filename)]

with open(sys.argv[1], "a") as myfile:
    for index in indices:
        myfile.write(users[index] + '\n')
