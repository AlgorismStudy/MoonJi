'''
기능 개발
'''

def solution(progresses, speeds):    
    answer = []
    stack = []
    speeds_stack = []
    for i in range(len(progresses)-1, -1, -1):
        stack.append(progresses[i])
        speeds_stack.append(speeds[i])
    
    while len(stack) > 0:
        stack = [x + y for x, y in zip(stack, speeds_stack)]
        count = 0
        while stack[-1] >= 100:
            count += 1
            stack.pop()
            if len(stack) <= 0:
                break

        if count > 0:
            answer.append(count)
        print(stack)

    return answer

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
print(solution(progresses, speeds))