'''좋다'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
result = 0

for i in range(N):
    tmp = nums[:i] + nums[i+1:]
    l, r = 0, N - 2
    while l < r:
        if tmp[l] + tmp[r] == nums[i]:
            result += 1
            break
        if tmp[l] + tmp[r] < nums[i]:
            l += 1
        elif tmp[l] + tmp[r] > nums[i]:
            r -= 1

print(result)