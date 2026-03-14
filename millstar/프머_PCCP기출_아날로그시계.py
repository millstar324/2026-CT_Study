"""

"""


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 시작 시간과 종료 시간을 초 단위로 변환
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2
    
    # 0시 혹은 12시 정각에 시작하는 경우, 미리 1번 카운트 (세 바늘이 겹침)
    if start_time == 0 or start_time == 12 * 3600:
        answer += 1
    
    # 1초씩 진행하며 확인
    for t in range(start_time, end_time):
        # 현재 위치 (t초)
        h_curr = (t * 1 + (h1 // 12) * 0) % 43200 # 시침은 초당 1만큼 (12시간 기준)
        # 실제 시침 위치: (h*3600 + m*60 + s) * 1 단위
        # 분침 위치: (m*60 + s) * 12 단위
        # 초침 위치: s * 720 단위
        
        # 더 직관적으로 계산하기 위해 함수화하지 않고 직접 계산 (120배 곱한 값)
        curr_h = (t * 1) % 43200
        curr_m = (t * 12) % 43200
        curr_s = (t * 720) % 43200
        
        next_h = ((t + 1) * 1) % 43200
        next_m = ((t + 1) * 12) % 43200
        next_s = ((t + 1) * 720) % 43200
        
        # 0도(43200)로 돌아가는 경우 예외 처리: 다음 위치가 0이면 43200으로 간주
        if next_h == 0: next_h = 43200
        if next_m == 0: next_m = 43200
        if next_s == 0: next_s = 43200
        
        # 초침이 분침을 추월했는가? (현재는 초침이 뒤에 있었는데, 다음엔 같거나 앞에 있음)
        match_m = curr_s < curr_m and next_s >= next_m
        # 초침이 시침을 추월했는가?
        match_h = curr_s < curr_h and next_s >= next_h
        
        if match_m and match_h:
            # 시침과 분침 위치가 같아져서 초침이 동시에 겹친 경우 (1번만 카운트)
            if next_m == next_h:
                answer += 1
            else:
                answer += 2
        elif match_m or match_h:
            answer += 1
            
    return answer

# def solution(h1, m1, s1, h2, m2, s2):
#     ns_rad = float(6 * s1)
#     nm_rad = float(6 * m1 + 0.1*s1)
#     nh_rad = float(6*h1 + 0.1*m1+ 1/600*s1)
    
#     fs_rad = float(6 * s2)
#     fm_rad = float(6 * m2 + 0.1*s2)
#     fh_rad = float(6*h2 + 0.1*m2+ 1/600*s2)
    
#     #초가 더 크면 1 / 초가 더 작으면 -1/ 같으면 0
#     m_before = 0.0
#     bm_flag = -2
#     nm_flag = -2
    
#     h_before = 0.0
#     bh_flag = -2
#     nh_flag = -2

    
#     count = 0
    
#     while (ns_rad != fs_rad or nm_rad != fm_rad or nh_rad != fh_rad):
#         if ns_rad > nm_rad :
#             nm_flag = 1
#         elif ns_rad == nm_rad :
#             nm_flag = 0
#         else:
#             nm_flag =-1
            
#         if ns_rad > nh_rad :
#             nh_flag = 1
#         elif ns_rad == nh_rad :
#             nh_flag = 0
#         else:
#             nh_flag =-1       
            
        
        
#         #1초 경과
#         ns_rad += 6.0
#         nm_rad += 0.1
#         nh_rad += (1/600)
        
#         bm_flag = nm_flag
#         bh_flag = nh_flag
        
        
        
#         #분check 
#         if nm_flag == 1:
#             if bm_flag == -1:
#                 count +=1
#                 continue
#         if nm_flag == 0:
#             count += 1
#             continue
#         if nm_flag == -1:
#             if bm_flag == 1:
#                 count+= 1
#                 continue
#         #시check   
#         if nh_flag == 1:
#             if bh_flag == -1:
#                 count +=1
#                 continue
#         if nh_flag == 0:
#             count += 1
#             continue
#         if nh_flag == -1:
#             if bh_flag == 1:
#                 count+= 1
#                 continue
            
        
        
#     return count