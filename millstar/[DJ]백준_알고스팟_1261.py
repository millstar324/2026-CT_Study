#start: 11:31 
#fin: 12:00

"""
[1]다익스트라: 가중치값이 다를때 유용(O(elogv))

[2]BFS: 가중치 값이 다 비슷하면(0-1) bfs가 유용(O(log(v+e)))

[3]플로이드 워셜: 시작점이 여러개일때

[4]벨만 포드: 음수 사이클도 계산 가능, BUT 느림

수정1) 벽돌 몇개 깨는게 핵심이기에 그냥 1,1에서 시작해도 됨.


"""
# import sys
# import heapq

# n,m = map(int, sys.stdin.readline().split())

# table = []

# first_list = []

# for i in range(n):
#     new_list = list(map(int, sys.stdin.readline().split()))
#     table.append(new_list)
#     if i == 0:
#         first_list = new_list


# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# start_spots = []

# #start지점들
# #dfs로 구함

# #각 start지점들을 for문으로 하면서 
# #깨부술 벽을 시간처럼 생각하고 다익스트라최단경로 구하기

# def dijkstra(x):






import sys
from collections import deque

# 가로 M, 세로 N 입력 (순서 주의!)
m, n = map(int, sys.stdin.readline().split())
# 미로 상태 입력
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 방문 여부 및 부순 벽의 개수 저장 (-1로 초기화)
dist = [[-1] * m for _ in range(n)]

def bfs():
    # 시작점 (0, 0)
    q = deque([(0, 0)])
    dist[0][0] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        # 도착점에 도달하면 종료
        if x == n - 1 and y == m - 1:
            return dist[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위를 벗어나지 않고 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                # 빈 방(0)일 경우: 벽을 안 부숴도 되므로 앞에 추가 (우선순위 높음)
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                # 벽(1)일 경우: 벽을 하나 부숴야 하므로 뒤에 추가
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

print(bfs())