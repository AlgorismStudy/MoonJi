'''
카드

숫자 카드 N장이 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -2^62보다 크거나 같고, 2^62보다 작거나 같다. 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하라. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
'''
import collections
import sys
input = sys.stdin.readline
N = int(input())
n_dict = collections.defaultdict(int)

for _ in range(N):
    number = int(input())
    n_dict[number] += 1
max_values = max(n_dict.values())
print(min([k for k, v in n_dict.items() if max_values == v]))