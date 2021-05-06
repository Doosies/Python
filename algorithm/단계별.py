s_list = ['c-', 'd-', 'dz=', 's=', 'z=', 'c=', 'lj', 'nj']
n = input()
i = len(n)-1
sum = 0

def is_in(string):
    for check in s_list:
        if string == check or string[1:] == check:
            if len(check) == 3:
                return 3
            else:
                return 2
    return 1

while i>= 0: 
    string = n[i-2:i+1] if i-2>= 0 else n[i-1:i+1]
    isn = is_in(string)
    i -= isn
    sum += 1
    
print(sum)