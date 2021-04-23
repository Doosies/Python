# from pprint import pprint
# arrs = [
#     [i*j for j in range(1,10)] # 구구단 뒷자리
#         for i in range(2,10) # 구구단 앞자리
# ]
# pprint( arrs, indent=10)
# for arr in arrs:
#     print(' '.join(map(str,arr)))
# for _,arr  in enumerate(arrs):
#     print(' '.join( map(str,arr) ))


# a = [38, 21, 53, 62, 53, 53]
# # print(a.count(53))

# # a = str(a)
# a = map(str,a)
# print(', '.join(list(a)))


# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# # b = filter(lambda val: len(val) == 5, a)
# b = [val for val in a if len(val) == 5]
# print(list(b))


# first, last = map(int, input().split())
# result = [ 2 ** i for i in range(first,last+1) ]
# del result[1]
# del result[-2 ]
# print(result)

# a = [(10, 20), (30, 40), (50, 60)]
# a[0] = (1,2)
# print(a)

# a = [[j for j in range(4)] for i in range(3)]
# b = [[0]*10]*10
# print(a)
# pprint(b, indent=3)


# a = [3,1,3,2,5]
# b = []

# for i in a:
#     line=[]
#     for j in range(i):
#         line.append(0)
#     b.append(line)
# pprint(b)

# b = [[0 for j in range(length)] for length in a]
# b = [[0]* i for i in a]
# print(b)


# students = [
#     ['john', 'C', 19],
#     ['maria', 'A', 25],
#     ['andrew', 'B', 7]
# ]
# print(sorted(students, key=lambda student: student[1]))
# print(sorted(students, key=lambda student: student[2]))

# test = students.copy()
# test.append([1,2,3])

# print(id(students), id(test))
# print(students)
# print(test)

# arr = [[[0]*3]*4]*2
# print(arr)
#  --------------------------------------------------지뢰찾기
# from pprint import pprint
# col, row = map(int, input().split())
# boards= []
# countBomb = []
# for i in range(row):
#     boards.append(list(map(str,input())))
#     countBomb.append([0*col]*row)

# for i in range(len(boards)):
#     for j in range(len(boards[i])):
#         cnt = 0
#         for i2 in range(-1,2):
#             for j2 in range(-1,2):
#                 if i2 == j2 == 0:
#                     continue
#                 isNotNullY = 0 <= i+i2 < len(boards)
#                 isNotNullX = 0<= j+j2 < len(boards[i])
#                 if isNotNullY and isNotNullX:
#                     if boards[i+i2][j+j2] == "*":
#                         cnt += 1
#                         # print(i+i2, j+j2, '/ ',end=' ')
#         if boards[i][j] != "*":
#             countBomb[i][j] = cnt
#         else:
#             countBomb[i][j] = '*'
#         print(countBomb[i][j], end='')
#     print()
#  --------------------------------------------------지뢰찾기 끝
# inputVar  = input().split(';')
# inputList = sorted(map(int,inputVar), reverse=True)
# for val in inputList:
#     print(f'{val:>9,}')

# keys = input().split()
# values = map(int, input().split())
 
# x = dict(zip(keys, values))
 
# del x['delta']
# x = {key:value for key, value in x.items() if value != 30}
 
# print(x)

# 1 2 5 10
# 1 2 4 5 10 20

# 1 2 5 10

# a1,b1  = map(int,input().split())
# a = {i for i in range(1,a1+1) if a1 % i == 0}
# b = {i for i in range(1,b1+1) if b1 % i == 0}

# divisor = a & b
 
# result = 0
# if type(divisor) == set:
#     result = sum(divisor)
 
# print(result)

# file = open('hello.txt', 'r')
# # file.write('Hello, World!')
# s = file.read()
# print(s)
# file.close()
# lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
# with open('hello.txt', 'r') as file:
#     for line in file:
#         print(line)

# import pickle

# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
# with open('james.p', 'rb') as file:
#     # pickle.dump(name, file)
#     # pickle.dump(age, file)
#     # pickle.dump(address, file)
#     # pickle.dump(scores,file)
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#     print(name, age, address, scores)
# with open('words.txt','r') as file:
#     count = 0
#     for word in file:
#         word = word.strip('\n')
#         if (len(word)) <= 10:
#             count += 1
#     print(count)


# with open('words.txt', 'r') as file:
#     lists = file.read().split()
#     for val in lists:
#         if 'c' in val:
#             print(val.strip(',.'))

# arr = [1,2,3,4,5]
# three_gram = zip(arr, arr[1:])
# for i in three_gram:
#     print(i[0], i[1], sep='')

# n = 7
# text = 'Python is a programming language that lets you work quickly'
# words = text.split()

# if len(words) < n:
#     print('wrong')
# else:
#     n_gram = zip(*[words[i:] for i in range(n)])
#     for i in n_gram:
#         print(i)
# with open('words.txt', 'r') as file:
#     for val in file:
#         w = val.strip('\n')
#         if(w == w[::-1] ):
#             print(w)
    
# def return_lists(val):
#     def add(in1):
#         return val + in1
#     return add

# sum5 = return_lists(5)
# print(sum5(5))


# def get_quotient_remainder(x,y):
#     return x%y, x//y
# x= 10
# y= 3
# quotient, remainder = get_quotient_remainder(x,y)
# print( quotient, remainder)
    

# korean, english, mathematics, science = map(int, input().split())

# def get_min_max_score(*args):
#     return min(args), max(args)
# def get_average(**kwargs):
#     return sum(kwargs.values()) / len(kwargs)

# min_score, max_score = get_min_max_score(korean, english, mathematics, science)
# average_score = get_average(korean=korean, english=english,
#                             mathematics=mathematics, science=science)
# print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
#       .format(min_score, max_score, average_score))
 
# min_score, max_score = get_min_max_score(english, science)
# average_score = get_average(english=english, science=science)
# print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
#       .format(min_score, max_score, average_score))

def hello(count):
    if count == 0:
        return
    print("hello!", count)
    count -= 1
    hello(count)
hello(5)