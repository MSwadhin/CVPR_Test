from asyncore import write
import random
import csv


random.seed(1e9+7)

x1 = []
x2 = []
y = []

for i in range(0,99):
    y.append( random.randint(0,1) )
    if y[i] == 0:
        x1.append( random.randint(1,50) )
    else :
        x1.append( random.randint(51,100) )

    x2.append( random.randint(1,100) )


# x1 = random.sample( range(1,100), 50 )
# x2 = random.sample( range(1,100), 50 )
# y  = random.sample( range(0,1), 100 )

header = ['X1','X2','Y']

with open('data/data_1.csv','w') as cf:
    writer = csv.writer(cf)
    writer.writerow(header)
    for i in range(0,99):
        row = []
        row.append(x1[i])
        row.append(x2[i])
        row.append(y[i])
        writer.writerow(row)
