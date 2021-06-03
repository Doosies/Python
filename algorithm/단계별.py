import sys; read = sys.stdin.readline

# st = '55-50+40' + '+'
st = read().rstrip() + '+'
is_plus = True
string = ''
result = 0

for c in st:
    if c == '-':
        if is_plus:
            result += int(string)
        else:
            result -= int(string)
        is_plus = False
        string = ''
    elif c == '+':
        if is_plus:
            result += int(string)
        else:
            result -= int(string)
        string = ''
    else:
        string += c
print(result)