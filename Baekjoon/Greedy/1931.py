'''
회의실 배정

N개의 회의에 대하여 사용표를 만들려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
'''
import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for i in range(N)]
time.sort(key = lambda x : x[1])

end, count = 0, 0

for i in range(N):
    if end <= time[i][0]:
        end = time[i][1]
        count += 1

print(count)