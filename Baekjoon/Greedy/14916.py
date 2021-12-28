'''
거스름돈
n원을 2원과 5원 동전을 가지고 개수가 최소가 되도록 거슬러 줄 경우 동전의 개수를 구하라.
'''

n = int(input())
count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    else:
        n -= 2
        count += 1

if n < 0:
    print(-1)