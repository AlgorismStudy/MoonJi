'''로또'''
from itertools import combinations
while True:
    s = input()
    if s == '0':
        break
    else:
        arr = list(map(int, s.split()))
        k = arr[0]
        nums = arr[1:]

        result = list(combinations(nums, 6))
        [print(*result[i], sep=" ") for i in range(len(result))]
        print()
