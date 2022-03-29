'''부분수열의 합'''
from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    arr = list(combinations(nums, i))
    for n in arr:
        if sum(n) == s:
            count += 1

print(count)

