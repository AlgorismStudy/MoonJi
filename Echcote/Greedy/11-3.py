'''
문자열 뒤집기

0과 1로만 이루어진 문자열 S에 있는 모든 숫자를 같게 만드려고 한다. 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 최소 횟수를 출력하라.
'''

S = input()
cur = S[0]
first = S[0]
count = 0

for i in range(len(S)):
    if S[i] != cur:
        cur = S[i]
        if cur != first:
            count += 1

print(count)