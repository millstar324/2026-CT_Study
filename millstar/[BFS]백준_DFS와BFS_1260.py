"""
1) BFS/DFS는 트리형태가 아닌 그냥 그래프 형태에서 다 쓰이는 것
2) 그래프는 인접리스트 or 인접 행렬로 표현 가능
3) DFS/BFS의 핵심은 이미 가본 곳은 다시 가지 않는 것
"""

# import sys

# def DFS(start,arr):
#     answer = []
#     #start 점을 [0]값에 가지고 있는 리스트 찾기
#         #해당 점의 [1]값을 [0]으로 하는 리스트 찾기
#             #있으면 [1]값을 [0]으로 하는 리스트 찾기 + 
#             #없으면 [1]값이 값은 리스트 찾기

# def solve():
#     n,m, v = map(int, sys.stdin.readline().strip())
#     dictable = {}
#     for i in range(m):
        

import sys
from collections import deque

# 1. 입력 받기
# n: 정점 개수, m: 간선 개수, v: 시작 정점
n, m, v = map(int, sys.stdin.readline().split())

# 2. 인접 리스트 생성 (1번부터 N번까지 사용하기 위해 n+1 크기)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 3. 방문할 수 있는 정점이 여러 개인 경우 번호가 작은 것부터 방문
for i in range(1, n + 1):
    graph[i].sort()

# --- DFS (재귀 사용) ---
def dfs(now):
    visited_dfs[now] = True
    print(now, end=' ')
    for next_node in graph[now]:
        if not visited_dfs[next_node]:
            dfs(next_node)

# --- BFS (큐 사용) ---
def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for next_node in graph[now]:
            if not visited_bfs[next_node]:
                visited_bfs[next_node] = True
                queue.append(next_node)

# 실행 및 결과 출력
visited_dfs = [False] * (n + 1)
dfs(v)
print() # 줄바꿈

visited_bfs = [False] * (n + 1)
bfs(v)