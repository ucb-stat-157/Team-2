import random

indices = random.sample(xrange(4051441), 10000)

users = [line.strip() for line in open('titleid_tokensid.txt')]

with open("test_title.txt", "a") as myfile:
    for index in indices:
        myfile.write(users[index] + '\n')
