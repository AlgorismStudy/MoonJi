'''
전화번호 목록

전화번호 목록이 주어질 때 이 목록이 일관성이 있는지 없는지 구하라. 전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.
'''
import sys
input = sys.stdin.readline

def consist_number(n, numbers):
    numbers.sort()
    print(numbers)
    for i in range(n-1):
        if numbers[i+1].startswith(numbers[i]):
            return 'No'
    return 'Yes'


t = int(input())
result = []
for i in range(t):
    n = int(input())
    numbers = [input().strip() for _ in range(n)]
    result.append(consist_number(n, numbers))

print(*result, sep='\n')