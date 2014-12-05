import sys
from math import ceil

dic = {}

if sys.argv[1] == 'title':
    filename = 'raymondpls.txt'
elif sys.argv[1] == 'purchased':
    filename = 'raymondpls2.txt'
elif sys.argv[1] == 'description':
    filename = 'raymondpls3.txt'
else:
    sys.exit()


lines = [line.strip() for line in open(filename)]

for line in lines:
    line = line.strip()
    tokens = line.split()

    if tokens[0] not in dic:
        dic[tokens[0]] = (tokens[1], tokens[2])
    else:
        clicks, impressions = dic[tokens[0]]
        clicks += int(tokens[1])
        impressions += int(tokens[2])
        dic[tokens[0]] = (clicks, impressions)

keys = dic.keys()

total_clicks = 0
total_impressions = 0
for key in keys:
    clicks, impressions = dic[key]
    total_clicks += int(clicks)
    total_impressions += int(impressions)


predictor = {}
for key in keys:
    clicks, impressions = dic[key]
    clicks = int(clicks)
    impressions = int(impressions)
    c = str(float(clicks) / total_clicks)
    nc = str(float(impressions - clicks) / (total_impressions - total_clicks))
    print 'lala'
    print key
    print c
    print nc

    if c > nc:
        predictor[key] = 1
    else:
        predictor[key] = 0

print predictor

def scoreClickAUC(num_clicks, num_impressions, predicted_ctr):
    """
    Calculates the area under the ROC curve (AUC) for click rates

    Parameters
    ----------
    num_clicks : a list containing the number of clicks

    num_impressions : a list containing the number of impressions

    predicted_ctr : a list containing the predicted click-through rates

    Returns
    -------
    auc : the area under the ROC curve (AUC) for click rates
    """
    i_sorted = sorted(range(len(predicted_ctr)),key=lambda i: predicted_ctr[i],
                      reverse=True)
    auc_temp = 0.0
    click_sum = 0.0
    old_click_sum = 0.0
    no_click = 0.0
    no_click_sum = 0.0

    # treat all instances with the same predicted_ctr as coming from the
    # same bucket
    last_ctr = predicted_ctr[i_sorted[0]] + 1.0

    for i in range(len(predicted_ctr)):
        if last_ctr != predicted_ctr[i_sorted[i]]:
            auc_temp += (click_sum+old_click_sum) * no_click / 2.0
            old_click_sum = click_sum
            no_click = 0.0
            last_ctr = predicted_ctr[i_sorted[i]]
        no_click += num_impressions[i_sorted[i]] - num_clicks[i_sorted[i]]
        no_click_sum += num_impressions[i_sorted[i]] - num_clicks[i_sorted[i]]
        click_sum += num_clicks[i_sorted[i]]
    auc_temp += (click_sum+old_click_sum) * no_click / 2.0
    auc = auc_temp / (click_sum * no_click_sum)
    return auc


answers = []
clickz = []
impressionz = []

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()

    # sample = float(tokens[3])

    sample = tokens[3]

    if sample != '0.0':
        sample = str(ceil(float(sample) * 10) / 10.0)
    else:
        sample = '0.1'


    # print 'wtf'
    # print sample
    # if sample != '1.0':
    #     sample = "{0:.1f}".format(float(tokens[3]) + 0.1)
    # print sample
    clickz.append(int(tokens[1]))
    impressionz.append(int(tokens[2]))

    if predictor[sample] == 1:
        answers.append(1)
    else:
        answers.append(0)

print scoreClickAUC(clickz, impressionz, answers)


tp = 0
tn = 0
fp = 0
fn = 0

total = 0
for i in range(len(clickz)):
    if int(clickz[i]) > 0 and answers[i] == 1:
        tp += 1
    elif int(clickz[i]) == 0 and answers[i] == 0:
        tn += 1
    elif int(clickz[i]) == 0 and answers[i] == 1:
        fp += 1
    else:
        fn += 1

    total += 1

print tp
print tn
print fp
print fn
print total


