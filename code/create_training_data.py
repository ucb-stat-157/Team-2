import random

indices = random.sample(xrange(1000000), 10000)

users = [line.strip() for line in open('small_training.txt')]

with open("training_data_pls.txt", "a") as myfile:
    for index in indices:
        myfile.write(users[index] + '\n')


