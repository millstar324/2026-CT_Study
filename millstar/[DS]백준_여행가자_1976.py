"""
- union 함수는 parent 테이블 업데이트를 완벽히 시켜주지 않음. 그저 두 노드를 연결시겨 주는게 주 목적임
- 한번에 업데이트 완벽히 시키면 모든 노드를 다 뒤져야 되기에 
union 함수를 써서 빠르게 작은 연결 고리 만든 뒤, 마지막에 찐으로 부모노드 찾을 때 getparent 하면 연산량 좋음. 
"""

# import sys

# input = sys.stdin.readline
# n = int(input().strip())
# m = int(input().strip())

# graph = [[] for _ in range(n+1)]

# #수정필요!
# parent = [-1]*(n+1)


# def get_parent(x):   
#     if parent[x] == x:
#         return x
#     else:
#         parent[x] = get_parent(parent[x])
#         return parent[x]
    


# def unionParent(x,y):
#     x = get_parent(x)
#     y = get_parent(y)
#     if x<y: parent[y] = x
#     else : parent[x] = y

# #그래프 생성
# for i in range(1,n+1):
#     nodes = list(map(int, input().split()))
#     for j, ns in enumerate(nodes):
#         index = j+1
#         if ns == 1:
#             unionParent(i, index)
        

# #합집합 처리 
# path = list(map(int, input().split()))

# key = parent[path[0]]
# flag = 0
# for p in path:
#     #수정필요!
#     if parent[p] != key:
#         print("NO")
#         flag = 1
#         break


# if flag == 0:
#     print("YES")



import sys

# 재귀 깊이 제한 해제 (파이썬 기본값은 1000)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축 (Optimization)
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 1. 입력 받기
n = int(input())
m = int(input())

# 2. 부모 테이블 초기화 (자기 자신으로)
parent = [i for i in range(n + 1)]

# 3. 연결 정보 확인 및 Union 연산
for i in range(1, n + 1):
    connections = list(map(int, input().split()))
    for j in range(n):
        if connections[j] == 1:
            union(parent, i, j + 1)

# 4. 여행 계획 확인
plan = list(map(int, input().split()))

# 모든 여행 경로의 도시가 같은 루트(부모)를 가지는지 확인
is_possible = True
root = find(parent, plan[0])

for i in range(1, m):
    if find(parent, plan[i]) != root:
        is_possible = False
        break

# 5. 결과 출력
print("YES" if is_possible else "NO")