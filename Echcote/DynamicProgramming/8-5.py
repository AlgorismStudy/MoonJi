'''
1로 만들기

정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
1. X가 5로 나누어 떨어지면, 5로 나눈다.
2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
3. X가 2로 나누어 떨어지면, 2로 나눈다.
4. X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 사용해서 1을 만들려고 할 때, 연산을 사용하는 횟수의 최솟값을 출력하라.
'''

X = int(input())
count = [0] * 30001

for i in range(2, X + 1):
    count[i] = count[i-1] + 1
    if i % 2 == 0:
        count[i] = min(count[i], count[i//2] +1)
    if i % 3 == 0:
        count[i] = min(count[i], count[i//3] +1)
    if i % 5 == 0:
        count[i] = min(count[i], count[i//5] +1)
        
print(count[X])