### COMPLETELY NOT IN USE ###

# Author: Kevin Shieh

# Testing using the sklearn package
# Requires sampled data which I don't have anymore

from sklearn import tree
from sklearn import svm
from sklearn.metrics import roc_curve, auc
from sklearn import linear_model
from sklearn.naive_bayes import BernoulliNB

import ml_metrics as metrics

instances = [line.strip() for line in open('combined_data.txt')]

samples = []
values = []

for instance in instances:
    instance = instance.split('\t')
    sample = [int(instance[12]), int(instance[13]), int(instance[6])]
    print sample
    samples.append(sample)

    if instance[0] != '0':
        values.append(1)
    else:
        values.append(0)

clf = tree.DecisionTreeClassifier()
clf.fit(samples, values)

clf2 = svm.SVC()
clf2.fit(samples, values)

bnb = BernoulliNB()
bnb.fit(samples, values)

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(samples, values)

tests = [line.strip() for line in open('combined_instances.txt')]

right = 0
total = 0

right2 = 0

clicks = []
impressions = []
depth = []
ctrs = []
actual69 = []

clicks2 = []
impressions2 = []
depth2 = []
ctrs2 = []

for test in tests:
    test = test.split('\t')

    sample = [int(test[12]), int(test[13]), int(test[6])]
    clicks.append(int(test[0]))
    impressions.append(int(test[1]))
    depth.append(int(test[2]))
    val = clf.predict(sample)
    ctrs.append(float(val))
    if int(test[0]) != 0:
        actual69.append(1)
    else:
        actual69.append(0)

    clicks2.append(int(test[0]))
    impressions2.append(int(test[1]))
    depth2.append(int(test[2]))
    val2 = clf2.predict(sample)
    ctrs2.append(float(val))

    if int(val[0]) == int(test[0]):
        right += 1

    if int(val2[0]) == int(test[0]):
        right2 += 1
    total += 1

# source: http://www.kddcup2012.org/c/kddcup2012-track2/forums/t/1776/understanding-the-auc
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

print scoreClickAUC(clicks, impressions, ctrs)

print scoreClickAUC(clicks2, impressions2, ctrs2)
