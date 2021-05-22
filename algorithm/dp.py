import sys; read = sys.stdin.readline
# 힙생성 알고리즘
# heap = [6,3,2,10,7,5,9,1,4,8]
hp = [7,6,5,4,3,2,1]
hp.insert(0,0)
print("전  -> ", hp)
        
isEnd = False

def heapify(size, i):
    c = i*2 # 왼쪽선택
    print("함수실행")
    # 오른쪽이 존재하면서 오른쪽이 크면
    if c+1 < size and hp[c] < hp[c+1]:
        c += 1 #오른쪽 선택
        
    # 부모보다 자식이 더 크면 둘이 바꿈
    if c < size and hp[i] < hp[c]:
        hp[i], hp[c] = hp[c], hp[i]
        print("노드교체")
    # 바꾼곳의 노드 위치가 맨 아래가 아닐경우
    if c < (size) // 2 :
        heapify(size, c)

for i in range( (len(hp)) //2, 0, -1):
    heapify(len(hp), i)

print("후  -> ", hp)
