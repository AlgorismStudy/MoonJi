'''
소트인사이드

수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''

N = input()

array = [N[i] for i in range(len(N))]
array.sort(reverse=True)
print(''.join(array))