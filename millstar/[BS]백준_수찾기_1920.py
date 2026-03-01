#start: 10:32
#finish : 10:56
"""
if in 은 for문이랑 같기에 시간 복잡도가 n*m이랑 같게됨

=> 리스트로 접근(일일히 하나씩 봐봄)하기 보다 
set(해시 테이블이용해서 해당 해시값 갖는 메모리만 확인하면 됨)으로 
찾는 속도 줄일수 있음 

*set은 순서 랜덤으로 바뀜 주의
"""

import sys

def solve():
    n = int(sys.stdin.readline().strip())
    arr = []
    arr = list(map(int,sys.stdin.readline().split()))
    arr = set(arr)
    # print(arr)
    
    m = int(sys.stdin.readline().strip())
    brr = []
    brr = list(map(int,sys.stdin.readline().split()))
    
    # print(brr)

    for b in brr:
        if b in arr:
            print(1)
        else:
            print(0)

    return 0

solve()
