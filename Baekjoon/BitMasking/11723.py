'''집합'''
import sys
input = sys.stdin.readline

M = int(input())
s = 0

for _ in range(M):
    command = input().split()

    if command[0] == "all":
        s = (1 << 20) - 1
    elif command[0] == "empty":
        s = 0
    else:
        op = command[0]
        num = int(command[1]) - 1

        if op == "add":
            s |= (1 << num)
        elif op == "remove":
            s &= ~(1 << num)
        elif op == 'check':
            if s & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif op == "toggle":
            s = s ^ (1 << num)
        