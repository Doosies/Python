from math import sqrt, floor

a, b = map(int, input().split())
prime = [True] * (b+1)
prime[1] = False

for i in range( 2, b+1):
    if prime[i]:
        for j in range( i*2, b + 1, i):
            prime[j] = False

for i in range(a, b+1):
    if prime[i]:
        print(i)