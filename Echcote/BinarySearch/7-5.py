'''
부품 찾기

부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 손님이 M개 종류의 부품을 대향으로 구매하겠다며 견적서를 요청했다. 이때 가게 안에 부품이 모두 있는지 확인하라.
'''
import sys
input = sys.stdin.readline
def main():
    N = int(input())
    part = list(map(int, input().split()))

    M = int(input())
    order = list(map(int, input().split()))

    result = []
    for o in order:
        result.append(binary_search(part, o, 0, N-1))
    print(*result, sep=" ")

def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

main()