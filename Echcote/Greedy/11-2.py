'''
곱하기 혹은 더하기

각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 호은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하라 (단, 일반적인 방식과 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정)
'''

S = input()
result = 0

for i in range(len(S)):
    cur = int(S[i])
    if result == 0 or cur == 0:
        result += cur
    else:
        result *= cur

print(result)
