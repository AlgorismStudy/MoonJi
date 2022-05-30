'''1'''

while True:
    try:
        n = int(input())

        count = 1
        first = 1

        while True:
            first %= n
            if first == 0: break
            first = (first * 10) % n + 1 % n
            count += 1
        print(count)

    except:
        break