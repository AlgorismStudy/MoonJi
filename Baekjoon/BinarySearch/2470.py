'''
두 용액

산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.
같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 
산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
target = 2000000000
index = 0
solution.sort(key=lambda x:abs(x))

for i in range(N-1):
    if abs(solution[i] + solution[i + 1]) < target:
        target = abs(solution[i] + solution[i + 1])
        index = i
result = [solution[index], solution[index+1]]
print(*sorted(result), sep=" ")