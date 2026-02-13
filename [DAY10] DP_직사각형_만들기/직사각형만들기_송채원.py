#topdown(memo) 방식 dp
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41]
memo = {}

def solve(idx, goal, max_e):
    if goal == 1:
        return 1
    if idx >= len(primes):
        return float('inf')
    
    state = (idx, goal, max_e)
    
    if state in memo:
        return memo[state]
    
    res = float('inf')
    
    for e in range(1, max_e+1):
        if goal % (e+1) == 0:
            pre_res = (primes[idx]**e)*solve(idx+1, goal//(e+1), e)
            res = min(res, pre_res)
            
    memo[state] = res
    
    return res
    

def main():
    
    n = int(input())
    while(n!= 0):
        case1 = solve(0,2*n, 60)
        case2 = solve(0,2*n-1, 60)
        print(min(case1, case2))
        n = int(input())
        
    return 

if __name__ == "__main__":
    main()