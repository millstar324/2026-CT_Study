"""
1) nx, ny로 x좌표, y좌표를 따로 관리
"""

# import sys
# from collections import deque 

# n,m = map(int, sys.stdin.readline().split())
# graph = []
# for i in range(n):
#     line = list(map(int, sys.stdin.readline().strip()))
#     graph.append(line)

# dy = [1,-1,0,0]
# dx=[0,0,-1,1,]
# visited = [[False]*m for _ in range(n)]
# print(visited)
# def BFS( ):
#     queue = deque()
#     queue.append([1,1])
#     while queue:
        
#         i,j = queue.popleft()
#         if visited[i][j] == True:
#             continue
#         else:
#             if i >= n or j >=m:
#                 continue
#             if graph[i][j] == 0:
#                 continue
#             visited[i][j] = True
#             queue
            

import sys
from collections import deque

# 1. 입력 받기
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    # 공백 없이 입력되므로 strip() 후 list로 변환
    graph.append(list(map(int, sys.stdin.readline().strip())))

# 2. 이동 방향 설정 (상, 하, 좌, 우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(start_x, start_y):
    queue = deque([(start_x, start_y)])
    
    while queue:
        x, y = queue.popleft()
        
        # 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽(0)이거나 이미 방문한 곳(1이 아님)이면 무시
            if graph[nx][ny] == 0:
                continue
            
            # 처음 방문하는 길(1)인 경우에만 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 도착 지점의 최단 거리 반환
    return graph[n-1][m-1]

# (0, 0)에서 시작
print(BFS(0, 0))
