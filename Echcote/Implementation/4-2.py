'''
시각

정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하라.
'''

N = int(input())
count = 0

for h in range(N+1):
    if h % 10 == 3:
        count += 3600
        continue

    for m in range(60):
        if m % 10 == 3 or m // 10 == 3:
            count += 60
            continue

        for s in range(60):
            if s % 10 == 3 or s // 10 == 3:
                count += 1

print(count)