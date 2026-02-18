#start: 10:42
#end : 

import sys

def solve():
    n ,m = map(int, sys.stdin.readline().split())
    nums = list(map(int,sys.stdin.readline().split()))
    
    
    #[0]:sum [1]:차 
    sim_rst= [ 0 , float('inf') ]

    for i in nums:
        for j in list(filter(lambda x: x!= i, nums)):
            for k in list(filter(lambda x: x!= i and x!= j, nums )):
                pre_sum = i+j+k
                pre_sum_diff = abs(pre_sum - m)
                if pre_sum <= m:
                    if sim_rst[1] > pre_sum_diff:
                        sim_rst[0] = pre_sum
                        sim_rst[1] = pre_sum_diff

    print(sim_rst[0])

solve()



