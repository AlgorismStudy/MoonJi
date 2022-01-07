'''
숫자 카드 2

숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드가 몇 개 인지 구하라.
'''
import collections

N = int(input())
number_card = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

numbers_dict = collections.defaultdict(int)
for number in number_card:
    numbers_dict[number] += 1

for number in numbers:
    if number in numbers_dict.keys():
       print(numbers_dict[number], end=" ")
    else:
        print(0, end=" ")
