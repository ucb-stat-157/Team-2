import random

indices = random.sample(xrange(23669283), 10000)

users = [line.strip() for line in open('userid_profile.txt')]

with open("test_data_pls.txt", "a") as myfile:
    for index in indices:
        myfile.write(users[index] + '\n')


