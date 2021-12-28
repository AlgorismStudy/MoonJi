'''
모험가 길드

공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다. N명의 모험가에 대한 정보가 주어질 때 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라.
'''

N = int(input())
adventurer = sorted(list(map(int, input().split())))

count = 0
i = 0

while i < N:
    fear = adventurer[i]
    i += fear
    if i >= N:
        break
    count += 1

print(count)
