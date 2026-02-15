#dp(바텀업), 스왑은 브루트포스
#ㅈㄴ어렵네

import sys

def get_min_ops(s):

    n = len(s)
    dp = [[0] * n for _ in range(n)]
    

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:

                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1], dp[i+1][j-1])
    return dp[0][n-1]

def solve():
    s_str = sys.stdin.readline().strip()
    if not s_str:
        print(0)
        return
    
    n = len(s_str)
    s = list(s_str)
    

    ans = get_min_ops(s)
    

    for i in range(n):
        for j in range(i + 1, n):
            if s[i] != s[j]: 

                s[i], s[j] = s[j], s[i]

                ans = min(ans, 1 + get_min_ops(s))
                

                s[i], s[j] = s[j], s[i]
                
    print(ans)

solve()