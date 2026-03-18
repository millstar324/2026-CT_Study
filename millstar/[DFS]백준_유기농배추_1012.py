import sys

sys.setrecursionlimit(100000) #보통 recursion이 1000번이 한계임

t = int(sys.stdin.readline().strip())
graph = [ [] for _ in range(t)]
visited_list = [[] for _ in range(t)]
wandh = [[] for _ in range(t)]

for i in range(t):
    w, h, k = map(int, sys.stdin.readline().split())
    wandh[i] = [w,h]
    visited_list[i] = [[False]*h for _ in range(w)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph[i].append([x,y])

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1] 

def DFS(x, j, wid, height):
    if x[0] >= wid or x[1] >= height or x[0] < 0 or x[1] <0:
        return 0

    x0 = x[0]
    x1 = x[1]
    # print(f"dfs 실행됨:[{x0},{x1}] 탐색")
    # print(f"vl:{visited_list[j]}")
    
    if visited_list[j][x0][x1] == False and ([x0,x1] in graph[j]) :
        visited_list[j][x0][x1] = True
        
        for ix, iy in zip(dx, dy):
            DFS([x[0]+ix, x[1]+iy], j, wid, height)



for i in range(t):
    count = 0
    for g in graph[i]:
        # print(f"g:{g}")
        if visited_list[i][g[0]][g[1]] == False:
            w, h = wandh[i]
            
            # print("개별count")
            DFS(g, i, w, h)
            count += 1

    print(count)
    