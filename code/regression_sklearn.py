from sklearn import tree
from sklearn import svm
import ml_metrics as metrics

instances = [line.strip() for line in open('aggregated_combined_data.txt')]

samples = []
values = []

for instance in instances:
    instance = instance.split('\t')
    print instance


    if int(instance[2]) != 0:
        sample = [instance[3], instance[4]]
        samples.append(sample)
        values.append(float(instance[1])/int(instance[2]))

clf = tree.DecisionTreeRegressor()
clf.fit(samples, values)

tests = [line.strip() for line in open('combined_instances.txt')]

right = 0
total = 0

clicks = []
impressions = []
depth = []
ctrs = []

for test in tests:
    test = test.split('\t')

    sample = [test[12], test[13]]
    clicks.append(int(test[0]))
    impressions.append(int(test[1]))
    val = clf.predict(sample)
    ctrs.append(float(val))

    if int(val[0]) == int(test[0]):
        if int(val[0]) == 1:
            print 'predicted click'
        right += 1

    total += 1

print "countz"
print right



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


print metrics.auc(values, ctrs)
