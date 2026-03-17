import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [ [] for _ in range(n+1) ]
visited_list = [False]*(n+1)

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
first_x = 1

def DFS(x):
    if visited_list[x] == False:
        visited_list[x] = True
        global count
        count += 1
        for i in graph[x]:
            DFS(i)
    else:
        return 0

        

DFS(first_x)
count -= 1

print(count)

