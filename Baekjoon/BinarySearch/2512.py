'''
예산

모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.
'''

N = int(input())
request = list(map(int, input().split()))
target = int(input())

start, end = 1, max(request)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = sum([x if x <= mid else mid for x in request])
    if total <= target:
        start = mid + 1
        answer = total
    elif total > target:
        end = mid - 1
    
print(end)
