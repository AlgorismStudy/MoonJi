'''재귀 함수로 구현한 이진 탐색 소스코드'''

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

def main():
    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("No")
    else:
        print(result + 1)

main()