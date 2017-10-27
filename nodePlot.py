import matplotlib.pyplot as plt
import numpy as np
import datetime
import csv


f = open("dataset101117.txt")
dataList = f.readlines()

with open("dataset101117.txt") as f:
    dataListStp = [word.strip() for word in f]


tempTop = dataListStp[1::22]
tempMid = dataListStp[3::22]
humidTemp = dataListStp[5::22]
timeStamp = dataListStp[9::22]

for i,val in enumerate(tempTop):
    val = float(val)


emptyArray=[]
timeStamp = [datetime.datetime.strptime(elem, '%Y-%m-%d %H:%M:%S.%f') for elem in timeStamp]
for i,val in enumerate(timeStamp):
    timeStamp[i]=val+datetime.timedelta(hours=9)

with open("plotlyData.csv","wb") as f:
    writer = csv.writer(f)
    writer.writerow(emptyArray)
    writer.writerow(timeStamp)
    writer.writerow(tempTop)
    writer.writerow(tempMid)
    writer.writerow(humidTemp)

print(timeStamp)

plt.plot(timeStamp,tempTop)
plt.plot(timeStamp,tempMid)
plt.plot(timeStamp,humidTemp)
plt.show()