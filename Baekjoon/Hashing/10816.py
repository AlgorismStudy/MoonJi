'''
숫자 카드 2

숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드가 몇 개 인지 구하라.
'''

N = int(input())
number_card = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

numbers_dict = {}
for number in numbers:
    numbers_dict[number] = 0

for number in number_card:
    if number in numbers_dict.keys():
        numbers_dict[number] += 1
    
print(*numbers_dict.values(), sep=" ")