#!/usr/bin/env python

### Creating a model for number of shared tokens and CTR prediction

### Now that we have our sample of ad tokens, we look at how many tokens they share 

from operator import itemgetter
import sys

for line in sys.stdin:

    count_queryad = 0
    
    instance = instance.strip()
    ad = instance.split('\t')
    
    adtokens = ad[1] + ad[2] + ad[3]
    
    for i in ad[0]:
        if i in adtokens:
            count_queryad += 1
    
    print (count_queryad/len(ad[0]), ad[4], ad[5])
    
