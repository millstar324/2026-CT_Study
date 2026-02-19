#start : 8:35
#finish: 8L47

import sys

def solve():
    n = int(sys.stdin.readline())

    for i in range(1,n+1):
        i_str = str(i)
        calc = i
        for j in i_str:
            calc += int(j)
        
        if calc == n:
            return i
        


    return 0

print(solve())
