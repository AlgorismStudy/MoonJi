def solution(s):
    answer = len(s)
    result = []
    for i in range(1, len(s)//2 + 1):
        count = 0
        for j in range(i, len(s), i):
            if s[j-i:j] == s[j:j+i]:
                count += 1
            else:
                result.append(count)
                count = 0
        else: 
            result.append(count)
            num_count = [len(str(i+1)) for i in result if i > 0]
            answer = min(answer, len(s) - sum(result) * i + sum(num_count))
            result = []
    return answer