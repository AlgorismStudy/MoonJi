'''
수 정렬하기 3

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하라
'''

import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10001

for _ in range(N):
    numbers[int(input())] += 1

for i in range(len(numbers)):
    for _ in range(numbers[i]):
        print(i)
