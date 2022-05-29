from datetime   import datetime
from collections import defaultdict
import math

def cal_time(t1, t2):
    result = datetime.strptime(t2,"%H:%M") - datetime.strptime(t1,"%H:%M")
    return result.seconds // 60

def cal_fee(fees, time):
    if time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
    
def solution(fees, records):
    answer = []
    index = defaultdict(list)
    cars = []
    for i in range(len(records)):
        record = records[i].split()
        car = record[1]
        index[car].append(i)
        if car not in cars: cars.append(car)
    
    cars.sort()
    for car in cars:
        arr = index[car]
        time = 0
        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):
                time += cal_time(records[arr[i]].split()[0], records[arr[i+1]].split()[0])
            else:
                time += cal_time(records[arr[i]].split()[0], "23:59")
        answer.append(cal_fee(fees, time))
    return answer