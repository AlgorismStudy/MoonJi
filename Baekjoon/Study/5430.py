'''AC'''
import re
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())

    # r'\d+'는 1회 이상 반복되는 숫자들에 대한 패턴을 의미
    arr = deque(re.findall(r'\d+', input()))

    is_reverse = False
    for i in range(len(p)):
        if p[i] == 'R':
            is_reverse = False if is_reverse else True
        elif arr and p[i] == 'D':
            if is_reverse:
                arr.pop()
            else:
                arr.popleft()
        else:
            print('error')
            break
    else:
        if is_reverse:
            arr.reverse()
        print('[' + ','.join(arr) + ']')