'''가희와 방어율 무시'''

a, b = map(int, input().split())

defense = a * (100 - b) / 100

if defense >= 100:
    print(0)
else:
    print(1)