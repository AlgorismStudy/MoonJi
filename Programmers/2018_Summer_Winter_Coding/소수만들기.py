from itertools import combinations
def solution(nums):
    answer = 0

    for i in list(combinations(nums, 3)):
        if isPrime(sum(i)):
            answer+=1

    return answer

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True