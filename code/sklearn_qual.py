from sklearn import tree
from sklearn import svm
from sklearn.metrics import roc_curve, auc

import ml_metrics as metrics

instances = [line.strip() for line in open('combined_data.txt')]

samples = []
values = []

for instance in instances:
    instance = instance.split('\t')
    # print instance
    sample = [instance[12], instance[13], instance[6]]
    samples.append(sample)

    # print "sample"
    # print sample
    if instance[0] != '0':
        # print 1
        values.append(1)
    else:
        # print 0
        values.append(0)

# spoof
# for i in range(1000):
#     s = [1, 3, 3]
#     samples.append(s)
#     values.append(1)

# for i in range(1000):
#     s = [2, 2, 2]
#     samples.append(s)
#     values.append(1)


clf = tree.DecisionTreeClassifier()
clf.fit(samples, values)

clf2 = svm.SVC()
clf2.fit(samples, values)

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

    sample = [test[12], test[13], test[6]]
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
        if int(val[0]) == 1:
            print 'predicted click'
        right += 1

    if int(val2[0]) == int(test[0]):
        if int(val2[0]) == 1:
            print 'predicted click'
        right2 += 1
    # else:
    #     print 'predicted'
    #     print val[0]
    #     print 'actual'
    #     print test[0]
    total += 1

print "countz"
print right
print right2



print total

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


binary_click = []
for click in clicks:
    if int(click) != 0:
        binary_click.append(1.0)
    else:
        binary_click.append(0.0)


print metrics.auc(ctrs, binary_click)
# print metrics.auc(binary_click, binary_click)
# print binary_click

# print "wtf"
# print metrics.auc(ctrs, ctrs)

# print binary_click
# print ctrs



fpr, tpr, _ = roc_curve(binary_click, ctrs)
print "auc"
# print fpr
# print type(fpr)
# print tpr
print auc(fpr, tpr)
print auc(tpr, tpr)
