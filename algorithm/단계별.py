S = input()
rst = []
for i in range(97,123):
    if chr(i) in S:
        rst.append(str(S.index((chr(i)))))
    else:
        rst.append('-1')
print(' '.join(rst))