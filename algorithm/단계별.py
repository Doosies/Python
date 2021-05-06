T = int(input())
R = [input().split() for _ in range(T)]
P = [ [result * int(r[0]) 
      for result in r[1]] 
      for r in R
    ]
for i in P:
    pt = ''.join(i[:])
    print(pt)