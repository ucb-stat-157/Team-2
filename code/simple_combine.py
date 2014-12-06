import sys

# Author: Kevin Shieh

# Combine multiple similarily formatted files into one file

clicks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
impressions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in sys.stdin:
    line.strip()
    tokens = line.split()

    index = int(round((float(tokens[0]) * 10)) - 1)

    clicks[index] += int(tokens[1])
    impressions[index] += int(tokens[2])


for i in range(len(clicks)):
    if i == 9:
        print '%s\t%s\t%s' % ('1.0', clicks[i], impressions[i])
    else:
        print '%s\t%s\t%s' % ('0.' + str(i + 1), clicks[i], impressions[i])

