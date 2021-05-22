import sys; read = sys.stdin.readline
# 힙정렬 알고리즘
hp = [14,251,1,10,14,5,2,100]
hp.insert(0,0)

def heapify_sort(size, i):
    c = i*2 # 왼쪽선택
    # 바꾼곳의 노드 위치가 맨 아래가 아닐경우
    shife_down(size,i)
    if c < (size) // 2 :
        heapify_sort(size, c)

def shife_down(size, i):
    c = i*2
    # 오른쪽이 존재하면서 오른쪽이 크면
    if c+1 < size and hp[c] < hp[c+1]:
        c += 1 #오른쪽 선택
    # 부모보다 자식이 더 크면 둘이 바꿈
    if c < size and hp[i] < hp[c]:
        hp[i], hp[c] = hp[c], hp[i]

def heapify_max():
    for i in range( (len(hp)) //2, 0, -1):
        heapify_sort(len(hp), i)
    print("후  -> ", hp)
    
    for i in range( len(hp)-1, 0, -1):
        hp[1], hp[i] = hp[i], hp[1]
        heapify_sort(i, 1)
    

heapify_max()
print("후  -> ", hp)