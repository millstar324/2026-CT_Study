#start : 11:29
#end: 

"""
recursion -시간초과 => queue 이용해서 풀기(시간제한 큐는 없음)

"""

# def solution(land):
#     g_group = [[-1]*len(land[0]) for _ in range(len(land)) ]
#     g_id = -1
#     id_list = [0]*250000
#     best = 0
    
#     for j, col in enumerate(zip(*land)):
#         c = list(col)
#         gain = 0
#         cur_gid = []
        
#         for i, r in enumerate(c):
            
#             if r == 1:
#                 # print(f"{i}행 {j}열 석유발견")
#                 if g_group[i][j] == -1:
#                     g_id +=1
#                     # print(f"새로운 발견 : {g_id}")
                    
#                     #탐색
#                     def search_g(cur_i, cur_j, gid):
                        
#                         if cur_i < len(land) and cur_j < len(land[0]):
                            
#                             current = land[cur_i][cur_j]
#                             if current == 1:
#                                 if g_group[cur_i][cur_j] != gid:
#                                     g_group[cur_i][cur_j] = gid
#                                     id_list[gid] +=1
                                    
#                                     search_g(cur_i, cur_j+1, gid)
#                                     search_g(cur_i+1, cur_j, gid)
#                                     return 0
#                             else:
#                                 return 0
#                         else:
#                             return 0
                    
#                     search_g(i, j, g_id)
#                     # print(f"=> {g_id}에 {id_list[g_id]} 만큼의 석유 발견")
#                     gain += id_list[g_id]
#                     # print(f"현 {j}열 gain:{gain}")
#                     cur_gid.append(g_id)
                    
#                 else:
                    
#                     if g_group[i][j] not in cur_gid:
#                         cur_gid.append(g_id)
#                         gain += id_list[g_group[i][j]]
#                         # print(f"현 {j}열 gain:{gain}")
                    
#         # print("====다음열====")
#         if gain > best:
#             best = gain
        
#     return best            
                
                                
                            
from collections import deque

def solution(land):
    n = len(land)      # 세로 길이
    m = len(land[0])   # 가로 길이
    
    # 각 열마다 얻을 수 있는 총 석유량을 저장할 리스트
    result = [0] * m
    # 방문 여부 체크
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            # 석유가 있고 아직 방문하지 않은 덩어리 발견!
            if land[i][j] == 1 and not visited[i][j]:
                # BFS를 통해 덩어리 크기와 차지하는 열 범위 확인
                size = 0
                queue = deque([(i, j)])
                visited[i][j] = True
                
                # 이 덩어리가 걸쳐 있는 열(column)들을 저장 (중복 제거를 위해 set 사용)
                columns = set()
                
                while queue:
                    r, c = queue.popleft()
                    size += 1
                    columns.add(c)
                    
                    # 상하좌우 탐색
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                
                # BFS 종료 후, 이 덩어리가 속한 모든 열에 덩어리 크기를 더해줌
                for col in columns:
                    result[col] += size
                    
    return max(result)
