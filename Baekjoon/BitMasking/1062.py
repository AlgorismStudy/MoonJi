'''가르침'''

from collections import defaultdict
print((1 << 26) - 1)

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

alphabet = defaultdict(int)
antarctic  = ['a', 'c', 'i', 'n', 't']

if K < 5:
    print(0)
else:
    
    for word in words:
        for w in word:
            if w not in antarctic:
                alphabet[w] += 1
    
    print(alphabet)