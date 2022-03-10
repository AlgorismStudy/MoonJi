from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# [+, -, x, /]
op_num = list(map(int, input().split()))
op_list = []
for i in range(4):
    op_list += op_num[i] * [i]

max_value = -987654321
min_value = 987654321

for operators in permutations(op_list, N-1):
    result = A[0]
    for i in range(len(operators)):
        if operators[i] == 0:
            result += A[i+1]
        if operators[i] == 1:
            result -= A[i+1]
        if operators[i] == 2:
            result *= A[i+1]
        if operators[i] == 3:
            result = int(result / A[i+1])
    
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)