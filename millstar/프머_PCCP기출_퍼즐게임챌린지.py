#start: 9:56
#end: 

"""시간초과이슈
=> while 문 조건을 쓰기
"""
# def test(diffs, times, level):
#     cost = 0
#     #cost계산
#     for i, (d,t) in enumerate(zip(diffs, times)):
#         # print(f"i:{i}, d:{d}, t:{t}")
#         if level >= d:
#             cost += t
#             # print(f"cost:{cost}")
#         else:
#             minus = d-level
#             cost += ((times[i-1]+t)*minus + t)
#             # print(f"cost:{cost}")
#     return cost




# def solution(diffs, times, limit):
#     maxlevel = max(diffs)
#     level=maxlevel//2
    
    

#     under_border = 0
#     upper_border = maxlevel

#     while True:
#         cost = 0
#         cost2 = 0
#         cost3 = 0
#         # print(f"level:{level}")
#         #cost계산
#         for i, (d,t) in enumerate(zip(diffs, times)):
#             # print(f"i:{i}, d:{d}, t:{t}")
#             if level >= d:
#                 cost += t
#                 # print(f"cost:{cost}")
#             else:
#                 minus = d-level
#                 cost += ((times[i-1]+t)*minus + t)
#                 # print(f"cost:{cost}")

#         # 결정
#         if cost <= limit:
#             if test(diffs,times,level-1) > limit:
#                 # print(f"{level-1}이 cost:{test(diffs,times,level-1)}로 limit:{limit} 보다 큼")
#                 return level
#             else:
#                 if upper_border > level:
#                     upper_border = level
                
#                 level = under_border + (upper_border - under_border)//2
#         else:
#             if test(diffs, times, level+1) <= limit:
#                 # print(f"{level+1}이 cost:{test(diffs,times,level+1)}로 limit:{limit} 보다 작음")
#                 return level+1
#             else:
#                 if under_border < level:
#                     under_border = level
#                 level = under_border + (upper_border - under_border)//2
            
#     answer = 0
#     return answer

def solution(diffs, times, limit):
    # 이진 탐색의 범위 설정 (최소 숙련도 1, 최대 숙련도 max(diffs))
    low = 1
    high = max(diffs)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        
        # 1. 현재 level(mid)에서의 총 소요 시간(cost) 계산
        total_time = 0
        prev_time = 0 # 이전 퍼즐의 소요 시간 (times[i-1])
        
        for d, t in zip(diffs, times):
            if mid >= d:
                total_time += t
            else:
                # 틀린 횟수: d - mid
                # 한 번 틀릴 때마다 (이전 시간 + 현재 시간) 추가 소요
                total_time += (d - mid) * (prev_time + t) + t
            
            # 다음 퍼즐을 위해 현재 시간을 prev_time에 저장
            prev_time = t
            
            # 중간에 limit을 넘어가면 더 계산할 필요 없음 (조기 종료)
            if total_time > limit:
                break
        
        # 2. 결과에 따라 탐색 범위 조절
        if total_time <= limit:
            # 시간 내 해결 가능하므로, 더 낮은 숙련도가 있는지 확인
            answer = mid
            high = mid - 1
        else:
            # 시간 초과이므로 숙련도를 높여야 함
            low = mid + 1
            
    return answer