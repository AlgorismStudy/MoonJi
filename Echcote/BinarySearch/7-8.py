'''
떡볶이 떡 만들기

절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라.
'''

def main():
    N, M = map(int, input().split())
    dduck = list(map(int, input().split()))

    start, end = 0, max(dduck)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = make_dduck(dduck, mid)
        if total < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)

def make_dduck(dduck, cut):
    result = 0
    for d in dduck:
        if d > cut:
            result += d - cut
    return result


main()