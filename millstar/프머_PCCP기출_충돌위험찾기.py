#start time: 12:17
#end time: 2:17

"""
문법 이슈)
cur = points[rout[i]]라고 쓰는 순간 cur은 새로운 리스트가 아니라 **points 안에 있는 리스트 그 자체(주소값)**를 가리키게 됨
=> cur = list(points[rout[i]]) #리스트를 새로 만들기

tip)
로직이 복잡할때는 종이에 말로 다 적어본 뒤 코딩하기
=> 로직 엇갈려 적는 경우가 많이 발생함...
"""

# def find_route(past, cur):
#     arr = []
#     step = 0
#     past.append(step)
#     arr.append(tuple(past))
    
#     if past[0] != cur[0]:
#         flag = 0
#         if past[0] > cur[0]:
#             flag = -1
#         else:
#             flag = 1
            
#         while past[0] != cur[0]:
#             step += 1
#             past[0] += flag
#             past[2] += 1
#             arr.append(tuple(past))
            
#     if past[1] != cur[1]:
#         flag = 0
#         if past[1] > cur[1]:
#             flag = -1
#         else:
#             flag = 1
            
#         while past[1] != cur[1]:
#             past[1] += flag
#             past[2] += 1
#             arr.append(tuple(past))
#     return arr

# def solution(points, routes):
#     risk_map = []
#     risk_count = 0
    
#     for i,rout in enumerate(routes):
#         for j, v in enumerate(rout):
#             routes[i][j] = routes[i][j]-1
    
#     rout_len = len(routes[0])
#     rout_map = []
    
#     for rout in routes:
#         cur = []
#         new_map = []
#         for i in range(rout_len):
#             if cur:
      
#                 past = cur
#                 cur = list(points[rout[i]])

#                 #경로&스탭 저장
#                 new_map = find_route(past, cur)
#             else:

#                 cur = list(points[rout[i]])

            
#         for new in new_map:
#             if new in set(rout_map):
#                 if new not in set(risk_map):
#                     risk_map.append(new)
#                     risk_count +=1

#             else:
#                 rout_map.append(new)

#     return risk_count

# solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], 	[[2, 3, 4, 5], [1, 3, 4, 5]])

from collections import Counter

def solution(points, routes):
    all_robot_paths = []
    
    for route in routes:
        path = []
        time = 0
        # 첫 번째 포인트의 좌표 가져오기 (r, c)
        curr_r, curr_c = points[route[0]-1]
        path.append((curr_r, curr_c, time))
        
        # 다음 경유지들로 이동
        for i in range(1, len(route)):
            next_r, next_c = points[route[i]-1]
            
            # 1. r 좌표 먼저 이동 (문제 조건: r부터 이동)
            while curr_r != next_r:
                time += 1
                curr_r += 1 if next_r > curr_r else -1
                path.append((curr_r, curr_c, time))
            
            # 2. c 좌표 이동
            while curr_c != next_c:
                time += 1
                curr_c += 1 if next_c > curr_c else -1
                path.append((curr_r, curr_c, time))
        
        # 이 로봇의 전체 경로를 통합 리스트에 추가
        all_robot_paths.extend(path)

    # 모든 로봇의 (r, c, time) 빈도수를 계산
    location_counts = Counter(all_robot_paths)
    
    # 2대 이상 모인(위험 상황) 좌표-시간 쌍의 개수만 카운트
    answer = 0
    for count in location_counts.values():
        if count > 1:
            answer += 1
            
    return answer