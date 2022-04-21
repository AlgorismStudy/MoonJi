'''좋은 수열'''
import sys
N = int(input())

def isGood(n):
    for i in range(1, (len(n))//2 + 1):
        if n[-i:] == n[-(i*2):-i]:
            return False
    else:
        return True

def back(n):
    if len(n) == N:
        print(n)
        sys.exit()
    for i in '123':
        if isGood(n + i):
            back(n + i)
    return

back('1')