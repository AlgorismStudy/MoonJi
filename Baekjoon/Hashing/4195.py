'''
친구 네트워크

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하라
'''
import collections

def main():
    T = int(input())
    for _ in range(T):
        find_friends()

def find_friends():
    F = int(input())

    friends = collections.defaultdict(list)
    for _ in range(F):
        name1, name2 = input().split()
        friends[name1].append(name2)
        friends[name2].append(name1)

    

    

main()