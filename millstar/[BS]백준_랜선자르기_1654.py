import sys

"""
- read()는 system call 횟수가 1번이라 readline() 보다 빠름
- 이진탐색 => 절반씩 줄여가기가 핵심
"""

# def solve():
#     k,n = map(int,sys.stdin.readline().split() )
#     arr = []
#     for _ in range(k):
#         arr.append(int(sys.stdin.readline().strip()))
#     set(arr)
#     list_arr = list(arr)
#     flag = 0
#     step=0
#     min_num = arr[0]
#     while flag ==0:
#         #가장 작은 선 길이로 시도후
#             #ok-> break 가장 작은 선 길이
#             #no - 개수 부족->해당 선의 1/(step*2)의 길이로 
#                #- 개수포화-> 해당 선보다 더 긴 길이의 1/step 의 길이로 
#                #=> 이전과 루프와 다른상태 나오면 (+1 or -1) 로 미세조정  



import sys

def solve():
    # 입력 속도 최적화
    input = sys.stdin.read().split()
    if not input:
        return
    
    K = int(input[0])
    N = int(input[1])
    lan_cables = list(map(int, input[2:]))

    # 이분 탐색을 위한 시작점과 끝점 설정
    start = 1
    end = max(lan_cables)
    
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        count = 0
        
        # 현재 중간 길이(mid)로 잘랐을 때 몇 개가 나오는지 계산
        for cable in lan_cables:
            count += cable // mid
            
        # 개수가 충분하다면? 길이를 더 늘려본다 (최댓값을 찾기 위해)
        if count >= N:
            result = mid
            start = mid + 1
        # 개수가 부족하다면? 길이를 줄여야 한다
        else:
            end = mid - 1
            
    print(result)

if __name__ == "__main__":
    solve()