# Author: Eileen Li

### the goal is to calculate how similar an ad's tokens are within itself, between its Keyword, Title, and Description then create groups based on # of shared tokens


def get_tokens(id_val, filename):
    f = open(filename)
    for line in f:
        token_list = line.strip().split('\t')
        if token_list[0] == id_val:
            tokens = token_list[1].split('|')
    return tokens

def ctr_token_prediction(testfile, trainfile):

### we create groups based on number of shared tokens

    shared0, shared1, shared2, shared3, shared4, shared5, shared6, shared7, shared8, shared9, shared10, sharedn = [], [], [], [], [], [], [], [], [], [], [], []

### first we calculate number of shared tokens for our training data

    data = [line.strip() for line in open("instances.txt")]
    ads = [line.split('\t') for line in data]

    for line in ads:

        query = get_tokens(line[7], 'queryid_tokensid.txt')
        keyword = get_tokens(line[8], 'purchasedkeywordid_tokensid.txt')
        title = get_tokens(line[9], 'titleid_tokensid.txt')
        description = get_tokens(line[10], 'descriptionid_tokensid.txt')

        kt = [x for x in keyword if x in title]
        ktd = [x for x in description if x in kt]

        ctr = int(line[0])/int(line[1])

### We also want to calculate the similarity index between the search query and the Ad keywords

        count_same = 0
        all_tokens = keyword + title + description
        for i in query:
            if i in all_tokens:
                count_same += 1
        similarity = float(count_same)/len(query

### creating the groups

        if len(ktd) == 0:
            shared0.append(ctr)
        else if len(ktd) == 1:
            shared1.append(ctr)
        else if len(ktd) == 2:
            shared2.append(ctr)
        else if len(ktd) == 3:
            shared3.append(ctr)
        else if len(ktd) == 4:
            shared4.append(ctr)
        else if len(ktd) == 5:
            shared5.append(ctr)
        else if len(ktd) == 6:
            shared6.append(ctr)
        else if len(ktd) == 7:
            shared7.append(ctr)
        else if len(ktd) == 8:
            shared8.append(ctr)
        else if len(ktd) == 9:
            shared9.append(ctr)
        else if len(ktd) == 10:
            shared10.append(ctr)
        else if len(ketd) > 10:
            sharedn.append(ctr)


### we calculate the average CTR for each group
    def avg(ctr):
        return sum(ctr)/len(ctr)

    ctr0, ctr1, ctr2, ctr3, ctr4, ctr5, ctr6, ctr7, ctr8, ctr9, ctr10, ctrn = avg(shared0), avg(shared1), avg(shared2), avg(shared3), avg(shared4), avg(shared5), avg(shared6), avg(shared7), avg(shared8), avg(shared9), avg(shared10), avg(sharedn)

### now we calculate the number of shared tokens for our test data
    predicted_ctr = []

    test = [line.strip() for line in open("test.txt")]
    test_ads = [line.split('\t') for line in data]

    for line in test_ads:

        query = get_tokens(line[7], 'queryid_tokensid.txt')
        keyword = get_tokens(line[8], 'purchasedkeywordid_tokensid.txt')
        title = get_tokens(line[9], 'titleid_tokensid.txt')
        description = get_tokens(line[10], 'descriptionid_tokensid.txt')

        kt = [x for x in keyword if x in title]
        ktd = [x for x in description if x in kt]

### fit the test data into the training data groups then return the AdID and its group's ctr

        if len(ktd) == 0:
            predicted_ctr.append(line[3], ctr0)
        else if len(ktd) == 1:
            predicted_ctr.append(line[3], ctr1)
        else if len(ktd) == 2:
            predicted_ctr.append(line[3], ctr2)
        else if len(ktd) == 3:
            predicted_ctr.append(line[3], ctr3)
        else if len(ktd) == 4:
            predicted_ctr.append(line[3], ctr4)
        else if len(ktd) == 5:
            predicted_ctr.append(line[3], ctr5)
        else if len(ktd) == 6:
            predicted_ctr.append(line[3], ctr6)
        else if len(ktd) == 7:
            predicted_ctr.append(line[3], ctr7)
        else if len(ktd) == 8:
            predicted_ctr.append(line[3], ctr8)
        else if len(ktd) == 9:
            predicted_ctr.append(line[3], ctr9)
        else if len(ktd) == 10:
            predicted_ctr.append(line[3], ctr10)
        else if len(ketd) > 10:
            predicted_ctr.append(line[3], ctrn)

    return predicted_ctr


adsimilarity("instances.txt")






