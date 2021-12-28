'''
설탕공장

봉지는 3kg, 5kg이 있다. 설탕 N킬로그램을 배달할 때 봉지 몇 개가 필요한가.
'''

N = int(input())
count = 0

if N % 5 == 0:
    count = N // 5
elif N % 5 == 1 and N // 5 > 0:
    count = N // 5 + 1
elif N % 5 == 3:
    count = N // 5 + 1
elif N % 5 == 2 and N // 5 > 1:
    count = N // 5 + 2
elif N % 5 == 4 and N // 5 > 0:
    count = N // 5 + 2

if count <= 0:
    count = -1

print(count)

