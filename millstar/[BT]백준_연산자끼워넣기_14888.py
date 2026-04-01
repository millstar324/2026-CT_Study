"""
- 수정1) heapq는 들어있는 값이 작은 순으로 순서가 바뀌기 때문에 리스트를 쓰는 것이 좋음
- 수정2) .count를 하면 매번 리스트 순회를 하면서 개수를 세야되기에 재귀함수에 depth 변수를 매개변수로 주는 것이 나음

"""

# import sys
# import heapq
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline
# n = int(input().strip())

# num_arr = list(map(int, input().split()))
#수정1)
# h = []
# for n in num_arr:
#     heapq.heappush(h, n)

# oper_arr = list(map(int, input().split()))

# ops = {
#     1 : lambda a,b: a+b,
#     2 : lambda a,b: a-b,
#     3 : lambda a,b: a*b,
#     4 : lambda a,b: a/b
# }

# def bt(h, o_arr):
    #수정2)
#     if o_arr.count(0) == 4:
#         return 0
#     for i,v in enumerate(o_arr):
#         if v == 0:
#             continue
#         o_arr[i] -=1
#         re
        
            
        


# first_num = heapq.heappop(h)

# for


import sys

# 입력 속도 향상
input = sys.stdin.readline

def solve():
    # N: 수의 개수
    n = int(input())
    # numbers: 수열
    numbers = list(map(int, input().split()))
    # operators: +, -, *, / 의 개수
    add, sub, mul, div = map(int, input().split())

    # 최댓값과 최솟값 초기화 (문제 범위: -10억 ~ 10억)
    max_value = -float('inf')
    min_value = float('inf')

    def dfs(depth, current_total, add, sub, mul, div):
        nonlocal max_value, min_value

        # 모든 연산자를 다 사용했을 때 (종료 조건)
        if depth == n:
            max_value = max(max_value, current_total)
            min_value = min(min_value, current_total)
            return

        # 각 연산자별로 재귀 호출
        if add > 0:
            dfs(depth + 1, current_total + numbers[depth], add - 1, sub, mul, div)
        if sub > 0:
            dfs(depth + 1, current_total - numbers[depth], add, sub - 1, mul, div)
        if mul > 0:
            dfs(depth + 1, current_total * numbers[depth], add, sub, mul - 1, div)
        if div > 0:
            # 음수를 양수로 나눌 때의 처리를 위해 int(a / b) 사용
            dfs(depth + 1, int(current_total / numbers[depth]), add, sub, mul, div - 1)

    # 첫 번째 숫자를 시작으로 DFS 수행
    dfs(1, numbers[0], add, sub, mul, div)

    print(max_value)
    print(min_value)

if __name__ == "__main__":
    solve()
