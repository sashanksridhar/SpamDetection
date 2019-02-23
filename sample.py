import csv
import sys

from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
f1 = "headerfeatures.csv"
f2 = "subjectfeatures.csv"
f3 = "bodyfeatures.csv"
fields = []
rows = []
y = []
f = 0
# reading csv file
with open(f1, 'r') as csv1,open(f2,'r') as csv2,open(f3,'r') as csv3:
    # creating a csv reader object
    csvreader1 = csv.reader(csv1)
    csvreader2 = csv.reader(csv2)
    csvreader3 =csv.reader(csv3)
    rows1 = []
    rows2 = []
    rows3 = []
    # extracting each data row one by one
    for row in csvreader1:
        if f == 0:
            f = 1
            continue
        y.append(row[0])
        del(row[0])
        rows1.append(row)
    f = 0
    for row in csvreader2:
        if f == 0:
            f = 1
            continue

        del(row[0])
        rows2.append(row)
    f = 0
    for row in csvreader3:
        if f == 0:
            f = 1
            continue

        del (row[0])
        rows3.append(row)
    for i in range(0,len(rows1)):
        rows1[i].extend(rows2[i])
        rows1[i].extend(rows3[i])
        rows.append(rows1[i])



X = np.array(rows).astype(np.float)
Y = np.array(y).astype(np.float)

model = GaussianNB()
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13,13,13,13,13,13,13),max_iter=1000)
clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100,max_depth=6, min_samples_leaf=32)
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Performing training
clf_entropy.fit(X, Y)
model.fit(X,Y)
mlp.fit(X,Y)
rf.fit(X,Y)
f1 = "headerfeatures1.csv"
f2 = "subjectfeatures1.csv"
f3 = "bodyfeatures1.csv"
rows = []
y = []
f = 0
with open(f1, 'r') as csv1,open(f2,'r') as csv2,open(f3,'r') as csv3:
    # creating a csv reader object
    csvreader1 = csv.reader(csv1)
    csvreader2 = csv.reader(csv2)
    csvreader3 =csv.reader(csv3)
    rows1 = []
    rows2 = []
    rows3 = []
    # extracting each data row one by one
    for row in csvreader1:
        if f == 0:
            f = 1
            continue
        y.append(row[0])
        del(row[0])
        rows1.append(row)
    f = 0
    for row in csvreader2:
        if f == 0:
            f = 1
            continue

        del(row[0])
        rows2.append(row)
    f = 0
    for row in csvreader3:
        if f == 0:
            f = 1
            continue

        del (row[0])
        rows3.append(row)
    for i in range(0,len(rows1)):
        rows1[i].extend(rows2[i])
        rows1[i].extend(rows3[i])
        rows.append(rows1[i])

print(y)
data = np.array(rows).astype(np.float)

predicted= model.predict(data)
p2 = mlp.predict(data)
p3 = clf_entropy.predict(data)
p4 = rf.predict(data)
print(list(predicted))
print(list(p2))
print(list(p3))
j = 0
count = 0
for i in list(predicted):
    if int(i) == int(y[j]):
        count = count+1
print(count)
print((count/len(y))*100)
j = 0
count = 0
for i in list(p2):
    if int(i) == int(y[j]):
        count = count+1
print(count)
print((count/len(y))*100)
j = 0
count = 0
for i in list(p3):
    if int(i) == int(y[j]):
        count = count+1
print(count)
print((count/len(y))*100)
j = 0
count = 0
for i in list(p4):
    if int(i) == int(y[j]):
        count = count+1
print(count)
print((count/len(y))*100)
#print(np.mean(predicted == y))
#print(confusion_matrix(y, predicted))
#df = pd.DataFrame(predicted, columns = ['ouput'])
#df.to_csv(sys.stdout)
'''
j = 1
for i in predicted:
    print(j,end=' ')
    j = j+1
    print(predicted[i])'''

