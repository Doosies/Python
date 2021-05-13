import sys
t = int(sys.stdin.readline())
inp = [int(sys.stdin.readline()) for _ in range(t)]
mi = max(inp)
prime = [True] * mi

for i in range( 2, int(mi**0.5)+1):
    if prime[i]:
        for j in range( i*2, mi, i):
            prime[j] = False
            
for number in inp:
    for i in range(number//2, number):
        if prime[i] and prime[number-i]:
            print(number-i, i)
            break