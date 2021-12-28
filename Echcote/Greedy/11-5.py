'''
볼링공 고르기

볼링공은 N개가 있으며 무게가 적혀있고 공의 번호는 1번부터 부여됩니다. 같은 무게의 공이 여러 개 있어도 다른 공으로 간주합니다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다. N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하라.
'''

N, M = map(int, input().split())
balls = list(map(int, input().split()))

count = 0
length = len(balls)

for i in range(len(balls)):
    for j in range(i, len(balls)):
        if balls[i] != balls[j]:
            count += 1

print(count)