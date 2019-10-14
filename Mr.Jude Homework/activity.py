#%%
# A.

import csv
from matplotlib import pyplot as plt
import datetime as dt
import statistics as st

filename = r'C:\Users\hp\Desktop\Mada\Homework\activity.csv'

dict = {}
dictInterval = {}
dictIntervalWeekDays = {}
dictIntervalWeekEnds = {}

with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    for row in reader:
        steps = row[0]
        if (steps!= "NA"):
            date = row[1]
            date2 = int(dt.datetime.strptime(date, "%Y-%m-%d").day)
            interval = int(row[2])
            
            dict.setdefault(str(date), [])
            dict[str(date)].append(int(steps))
            
            dictInterval.setdefault(interval, [])
            dictInterval[interval].append(int(steps))
            
            if (date2 % 7 == 0):
                dictIntervalWeekEnds.setdefault(interval, [])
                dictIntervalWeekEnds[interval].append(int(steps))
            else:
                dictIntervalWeekDays.setdefault(interval, [])
                dictIntervalWeekDays[interval].append(int(steps))
                
listDate = []
listTotal = []
listAve = []

for i in dict.keys():
    listDate.append(i)
    listTotal.append(sum(dict.get(i)))
    listAve.append(st.mean(dict.get(i)))
    
plt.hist(listTotal)
plt.title("Total steps per day")
plt.xlabel("Steps per day")    
plt.ylabel("Frequency")
plt.yticks(range(0, 25, 5))
plt.show()

print("The mean is :", st.mean(listTotal))
print("The median is :", st.median(sorted(listTotal)))    
    
#%%
# B.

import csv
from matplotlib import pyplot as plt
filename = r'C:\Users\hp\Desktop\Mada\Homework\activity.csv'

    
def time_series():
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        step_intervals = [0]*288
        days = 61
        acc = 0
        while True :
            try:
                step = next(reader)[0]
                step_intervals[acc] += int(step) if step != "NA" else 0
                acc += 1
                if acc == 288:
                    acc = 0
            except StopIteration:
                break
        return step_intervals
    
def average (steps_interval):
    days = 61
    avg= []
    for step in steps_interval:
        avg.append(step/days)
    return avg


fig,axs =plt.subplots(2)   
axs[0].set_title("Steps per 5 minutes")
axs[0].plot(time_series())
axs[1].set_title("Average steps per 5 minutes")
axs[1].plot(average(time_series()))
plt.tight_layout()
plt.show() 
    
#%%
# C.

import csv
import statistics as st
import re
import matplotlib.pyplot as plt
filename = r'C:\Users\hp\Desktop\Mada\Homework\activity.csv'


def NAvalue():
    with open(filename) as f :
        x = f.read()
        return len(re.findall("NA",x))
        
print("Total NA in activity.csv is :",NAvalue())

def missing_value():
    with open(filename) as f:
        x = f.read()
    with open(filename,"w+") as f:
        f.write(re.sub("NA","0",x))

def report():
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        medianPerDay = []
        meanPerDay = []
        stepsToday = []
        acc = 0
        while True:
            try:
                acc += 1
                step = next(reader)[0]
                stepsToday.append(int(step) if step != "NA" else 0)
                if acc % 288 == 0:
                    stepsToday.sort()
                    medianPerDay.append(st.median(stepsToday))
                    meanPerDay.append(st.mean(stepsToday))
                    stepsToday = []
            except StopIteration:
                   break
        return medianPerDay, meanPerDay

#%%
# D.

import csv
from matplotlib import pyplot as plt
from datetime import datetime
import statistics as st
filename = r'C:\Users\hp\Desktop\Mada\Homework\activity.csv'

def day_type(rows):
  for row in rows:
    day_of_week = datetime.strptime(row[1], "%Y-%M-%d").weekday()
    if day_of_week <= 4:
      row.append("weekday")
    else:
      row.append("weekend") 

with open(filename) as f:
  reader = csv.reader(f)
  header = next(reader)
  rows = [row for row in reader]
  interval_range = [int(row[2]) for row in rows][:288]
  weekday_averages, weekend_averages = [], []

  

print(rows)

  
for interval in interval_range:
  weekend_interval_sum, weekend_interval_count, weekend_interval_average = 0, 0, 0
  weekday_interval_sum, weekday_interval_count, weekday_interval_average = 0, 0, 0
  for row in rows:
    if int(row[2]) == interval and row[0] != "NA":
      if row[1] == "weekend":
        weekend_interval_sum += int(row[0])
        weekend_interval_count += 1
        weekend_interval_average = weekend_interval_sum / weekend_interval_count
      elif row[1] == "weekday":
        weekday_interval_sum += int(row[0])
        weekday_interval_count += 1
        weekday_interval_average = weekday_interval_sum / weekday_interval_count
  weekend_averages.append(weekend_interval_average)
  weekday_averages.append(weekday_interval_average)
  
plt.plot(interval_range, weekend_averages)
plt.plot(interval_range, weekday_averages)
plt.legend(['Weekend', 'Weekday'])
plt.show()
  
    
    
    
    
    
    
    