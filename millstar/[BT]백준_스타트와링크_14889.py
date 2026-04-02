"""
해당 문제는 BT 문제지만 굳이 BT 함수 구현 직접 안하고 
- import combinations를 통해 k개씩 튜플을 만들어 주면 그걸로 for문 돌리는게 더 나음
- 절댓값은 abs함수로 구하면 됨

"""

# import sys

# input = sys.stdin.readline
# n = int(input().strip())
# s = [[0]*n for _ in range(n)]

# for i in range(n):
#     s_line = list(map(int, input().split()))
#     for j, v in enumerate(s_line):
#         if v == 0:
#             continue
#         s[i][j] += v
#         s[j][i] += v

# min_diff = float('inf')

# count_list = [i for i in range(n)]

# def Backtracking(depth, cur_start_total, cur_start_id, e_point, fix_s_point, cl):
#     global min_diff
#     global s

#     if s[fix_s_point][e_point] == 0:
#         return 

#     if depth == int(n/2):
#         link_total = 0
#         cur_start_id.append(fix_s_point)
        
#         for i,v_list in enumerate(s):
#             for j, v in enumerate(v_list):
#                 if v == 0:
#                     break
#                 if (i not in cur_start_id) and ( j not in cur_start_id):
#                     link_total += v

#         if cur_start_total > link_total:
#             diff = cur_start_total-link_total
#         else:
#             diff = link_total - cur_start_total
#         min_diff = ( min_diff if min_diff< diff else diff  )
#         return
    
#     depth += 1
    

#     cur_start_total += s[fix_s_point][e_point]
#     cur_start_id.append(e_point)
#     cl.remove(e_point)
#     for c in cl:
#         Backtracking(depth, cur_start_total, cur_start_id, c, fix_s_point, cl)


# real_min_diff = float('inf')
# for i in range(n):
#     portable_cl = count_list[:]
#     portable_cl.remove(i)
#     Backtracking(0, 0, [], 0, i, portable_cl)

#     real_min_diff = min(real_min_diff, min_diff)


# print(real_min_diff)


    
    
import sys
from itertools import combinations

def solve():
    input = sys.stdin.read().split()
    N = int(input[0])
    # 능력치 행렬 S를 2차원 리스트로 변환
    S = []
    idx = 1
    for i in range(N):
        S.append(list(map(int, input[idx:idx+N])))
        idx += N

    # 모든 사람의 인덱스 리스트
    members = list(range(N))
    # N/2명을 뽑는 모든 조합 (첫 번째 멤버를 포함하는 경우만 계산하여 절반으로 최적화)
    # combinations(members[1:], N//2 - 1)을 사용하여 0번 멤버를 스타트 팀에 고정
    min_diff = float('inf')

    # 모든 팀 조합 생성
    for start_team in combinations(members, N // 2):
        # 링크 팀은 스타트 팀에 속하지 않은 나머지 멤버들
        link_team = list(set(members) - set(start_team))
        
        start_score = 0
        link_score = 0
        
        # 각 팀의 능력치 합산 (2명씩 짝지어 계산)
        for i, j in combinations(start_team, 2):
            start_score += S[i][j] + S[j][i]
        
        for i, j in combinations(link_team, 2):
            link_score += S[i][j] + S[j][i]
            
        # 차이 계산 및 최솟값 갱신
        diff = abs(start_score - link_score)
        if diff < min_diff:
            min_diff = diff
        
        # 만약 차이가 0이면 더 이상 계산할 필요 없음 (최적화)
        if min_diff == 0:
            break
            
    print(min_diff)

if __name__ == "__main__":
    solve()