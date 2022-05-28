import math

def solution(n, k):
    answer = 0
    k_num = ''
    while n > 0:
        tmp = n % k
        n //= k
        k_num = str(tmp) + k_num
    
    nums = k_num.split("0")

    for num in nums:
        if len(num) > 0:
            num = int(num)
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                if num > 1:
                    answer += 1
            
    return answer