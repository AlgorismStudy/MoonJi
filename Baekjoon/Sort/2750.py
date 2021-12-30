'''
수 정렬하기

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하라.
'''

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()

print(*array, sep='\n')