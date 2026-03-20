import sys


"""
1. 리스트 인덱스 초과 주의하기
2. 이 문제는 prefix에 슬라이딩 윈도우, 투 포인터 알고리즘도 중요한 로직인 문제인 듯
3. 슬라이딩 윈도우, 투 포인터 알고리즘은 O(n)의 복잡도로 최적화 가능
"""

import sys

n, s = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
current_sum = 0
min_len = float('inf')

while True:
    if current_sum >= s:
        min_len = min(min_len, end - start)
        current_sum -= num_list[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += num_list[end]
        end += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)



# n,s = map(int, sys.stdin.readline().split())

# num_list = list(map(int, sys.stdin.readline().split()))

# prefix = [0]


# sum = 0
# for num in num_list:
#     sum+= num
#     prefix.append(sum)
# start_i = 0
# end_i = 0

# if prefix[n-1] <s:
#     print(0)
    


# else:
#     gap = 1
#     flag = 0
#     while flag == 0:
        
    
#         for i in range(n):
#             start_i = i
#             end_i = i+gap

#             if end_i > n:
#                 break
#             result = prefix[end_i] - prefix[start_i]
#             if result >=  s:
#                 print(gap)
#                 flag = 1
#                 break
#         gap +=1
