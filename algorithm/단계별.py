n = input().upper()
m = {}
for char in n:
    m[char] = n.count(char)
    n.strip(char)
    
if len(set(m.values())) != len(m.values()):
    print("?")
else:
    sort = sorted(m.items(), key=lambda x: x[1])
    print(sort[-1][0])