'''시험 감독'''

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

A = [n - B for n in A]
result = N

for a in A:
    if a > 0:
        q = a // C
        r = a % C
        result += q if r == 0 else q + 1

print(result)