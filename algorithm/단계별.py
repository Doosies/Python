import sys
x,y,w,h = map(int, sys.stdin.readline().split())
near_x = w-x if w-x < x else x
near_y = h-y if h-y < y else y
print(min([near_x, near_y]))