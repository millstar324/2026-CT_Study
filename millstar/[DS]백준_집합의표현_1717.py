import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n,m = map(int, input().split())

parent = [ i for i in range(n+1)]

def get_parent(parent, node):
    if parent[node] != node:
        parent[node] =  get_parent(parent, parent[node])
    return parent[node]

def union(parent, x,y):
    p_x = get_parent(parent, x)
    p_y = get_parent(parent, y)
    if p_x < p_y: 
        parent[p_y] = p_x
    else:
        parent[p_x] = p_y

for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:
        union(parent,a,b)
    else:
        p_a = get_parent(parent, a)
        p_b = get_parent(parent, b)
        if p_a == p_b:
            print("YES")
        else:
            print("NO")


