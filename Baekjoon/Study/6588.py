'''골드바흐의 추측'''
import sys
input = sys.stdin.readline

def isPrime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break

    isGoldbach = False
    for i in range(3, n, 2):
        if isPrime(i) and isPrime(n-i):
            print(f"{n} = {i} + {n-i}")
            isGoldbach = True
            break
    if not isGoldbach:
        print("Goldbach's conjecture is wrong.")