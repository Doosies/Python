import heapq  # 우선순위 큐 구현을 위함

# graph = {
#     'A': {'B': 8, 'C': 1, 'D': 2},
#     'B': {},
#     'C': {'B': 5, 'D': 2},
#     'D': {'E': 3, 'F': 5},
#     'E': {'F': 1},
#     'F': {'A': 5}
# }

graph= {
    'A' : { 'B':2, 'C':4, 'D':1 },
    'B' : { 'E':1, 'C':3 },
    'C' : { 'E':2, 'F':2, 'A':4 },
    'D' : { 'F':5, 'G':4 },
    'E' : { 'H':3 },
    'F' : { 'H':3, 'I':2, 'J':4, 'G':3 },
    'G' : {'K':2 },
    'H' : { 'O':8, 'L':1 },
    'I' : { 'L':3, 'M':2, 'J':3 },
    'J' : { 'M':6, 'N':3, 'K':6 },
    'K' : { 'N':4, 'R':2 },
    'L' : { 'O':6, 'M':3 },
    'M' : { 'O':4, 'P':2, 'N':5 },
    'N' : { 'Q':2, 'R':1 },
    'O' : { 'S':6, 'P':2 },
    'P' : { 'S':2, 'T':1, 'Q':2 },
    'Q' : { 'T':3, 'R':8 },
    'R' : { 'T':5 },
    'S' : { 'Z':2 },
    'T' : { 'Z':8 },
    'Z' : {}
}
prev = {

    'A' : None,
    'B' : None,
    'C' : None,
    'D' : None,
    'E' : None,
    'F' : None,
    'G' : None,
    'H' : None,
    'I' : None,
    'J' : None,
    'K' : None,
    'L' : None,
    'M' : None,
    'N' : None,
    'O' : None,
    'P' : None,
    'Q' : None,
    'R' : None,
    'S' : None,
    'T' : None,
    'Z' : None
}
cnt = 0
result = []
def dijkstra(graph, start, end):
  distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  global cnt
  heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.
    # print(current_distance, current_destination)
    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
    #   print(current_destination, new_destination)
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        cnt += 1
        prev[new_destination] = current_destination
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

  result.append(end)
  now = prev[end]
  while now != None:
      result.append(now)
      now = prev[now]
      
    #   if nextt == 0:
    #       break
  
  return distances

print(dijkstra(graph, 'A', 'Z'))
# print(prev)
print(cnt)
# print(list(reversed(result)))