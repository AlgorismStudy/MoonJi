'''
ATM

ATM앞에 N명의 사람들이 줄을 서있다. 1번부터 N번까지 번호가 매겨져 있으며 i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다. 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하라.
'''

N = int(input())
P = sorted(list(map(int, input().split())))

time = 0

for i in range(N):
    time += sum(P[0:i+1])

print(time)