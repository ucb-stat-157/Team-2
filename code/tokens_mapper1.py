#!/usr/bin/env python

### Creating a model for number of shared tokens and CTR prediction

# first we create the function that looks up the tokens given an ID

def get_tokens(id_val, filename):
    f = open(filename)
    for line in f:
        token_list = line.strip().split('\t')
        if token_list[0] == id_val:
            tokens = token_list[1].split('|')
    return tokens

# now we map the ID from a sample of the training data to the tokens

import sys
import random

instances = [line.strip() for line in open('training.txt')]

for line in instances:

    ad = line.split()
    
# because look up files take a long time, we limit our sample to ads that had greater than 10 impressions
    
    if int(ad[1]) > 10:
    
        query = get_tokens(ad[7], 'queryid_tokensid.txt')
        keyword = get_tokens(ad[8], 'purchasedkeywordid_tokensid.txt')
        title = get_tokens(ad[9], 'titleid_tokensid.txt')
        description = get_tokens(ad[10], 'descriptionid_tokensid.txt')

# we include the CTR for this ad

        click = ad[0]
        impressions = ad[1]
    
        ad = [query, keyword, title, description, click, impressions]
    
        print ad


