'''가희와 카오스 파풀라투스'''

hour, min = map(int, input().split(":"))
clock = list(map(int, input().split()))

L = int(input())
event = [input() for _ in range(L)]

def find_area(hour, min):
    degree = hour * 30 + min * 0.5
    return int(degree // 60)

def time(hour, min):
    if min >= 60:
        hour += min // 60
        min %= 60
    if hour >= 12:
        hour %= 12
    return hour, min

seal = [0] * 6
second = 0

for e in event:
    sec, skill = e.split()
    sec = int(sec.split(".")[0]) + int(sec.split(".")[1]) * 0.001
    
    area = find_area(hour, min)

    if skill == "^":
        seal[area] = 1
    elif skill[-3:] == "MIN":
        min += int(skill[:2])
    elif skill[-4:] == "HOUR":
        hour += int(skill[0])
    
    hour, min = time(hour, min)
    
result = 0
for i in range(6):
    if seal[i] == 0:
        result += clock[i]
if result >= 100:
    print(100)
else:
    print(result)