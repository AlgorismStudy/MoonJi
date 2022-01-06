'''
듣보잡

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
'''

N, M = map(int, input().split())
dict1 = {}
for _ in range(N):
    dict1[input()] = 0

answer = []
for _ in range(M):
    name = input()
    if name in dict1.keys():
        answer.append(name)

print(len(answer), *sorted(answer), sep="\n")