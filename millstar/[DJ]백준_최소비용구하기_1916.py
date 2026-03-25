import sys
import heapq
"""
heapq는 튜플의 첫번째 요소를 기준으로 정렬하기 때문에 튜플의 첫번째 요소를 cost 값으로 해서 넣기
수정1) cost 값이 적은 순으로 탐색하기 위함.
수정2) 이미 처리된 노드도 포함해서 생각할 때 그동안 쌓인 비용보다 더 비용이 큰 정보는 무시하기 위함.
"""

INF = float('inf')

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s_pt, e_pt = map(int,input().split())

def dijkstra(start):

    #수정1
    h = [(0,start)]
    distance[start] = 0

    while h:
        startdist, startpt = heapq.heappop(h)

        #수정2
        if distance[startpt] < startdist:
            continue

        paths = graph[startpt]

        for e, c in paths:
            calc_cost = startdist+ c
            if distance[e] > calc_cost:
                distance[e] = calc_cost
                #수정3
                heapq.heappush(h, (calc_cost, e))

dijkstra(s_pt)

print(distance[e_pt])


