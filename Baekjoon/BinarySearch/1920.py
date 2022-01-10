'''
수 찾기

N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    X = list(map(int, input().split()))

    A.sort()
    for x in X:
        print(binary_search(A, x, 0, N-1))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

main()