from sklearn import tree
from sklearn import svm
import ml_metrics as metrics

instances = [line.strip() for line in open('aggregated_combined_data.txt')]

samples = []
values = []

for instance in instances:
    instance = instance.split('\t')
    # print instance


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


print "mse"
print len(values)
print len(ctrs)
print len(clicks)
mse = 0
for index in range(len(ctrs)):
    actual = float(clicks[index]) / impressions[index]
    mse += (actual - ctrs[index])**2

print mse/len(values)

