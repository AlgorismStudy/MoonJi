'''가장 긴 증가하는 부분 수열'''

N = int(input())
array = list(map(int, input().split()))

d = [array[0]]
for i in range(1, N):
    if array[i] > d[-1]:
        d.append(array[i])
    if len(d) > 1 and d[-2] < array[i] < d[-1]:
        d.pop()
        d.append(array[i])
    if len(d) == 1 and array[i] < d[-1]:
        d[0] = array[i]
        
print(len(d))