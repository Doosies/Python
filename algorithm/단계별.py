n = input().split()
n2 = [''.join(list(reversed(n[i])))
        for i in range(2) 
     ]
n3 = [int(val) for val in n2]
print(max(n3))