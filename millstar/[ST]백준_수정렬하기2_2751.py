#start: 8:56
#end: 9:10

import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = []

    for _ in range(n):
        m = int(sys.stdin.readline().strip())
        arr.append(m)
    arr.sort()
    for i in arr:
        print(i)

solve()
     


