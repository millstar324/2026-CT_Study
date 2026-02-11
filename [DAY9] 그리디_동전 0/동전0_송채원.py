def big_m(ls, k):
    for i in range(len(ls)-1, -1, -1):
        if ls[i] <= k:
            return i
    return 0

    

def main():
    N, K = map(int, input().split())
    money_ls =[]
    count = 0
    
    for i in range(N):
        money_ls.append(int(input()))
    
    while(K!=0):
        index = big_m(money_ls,K)
        n= K// (money_ls[index])
        K %= (money_ls[index])
        count +=n
    
    
    print(count)

if __name__ =="__main__":
    main()


"""
import sys

def main():
    # 1. 빠른 입력을 위해 sys.stdin.readline 사용
    # N: 동전 종류, K: 목표 금액
    input_data = sys.stdin.readline().split()
    if not input_data:
        return
    
    N, K = map(int, input_data)
    
    # 2. 동전 가치 입력 받기 (오름차순으로 주어짐)
    money_ls = []
    for _ in range(N):
        money_ls.append(int(sys.stdin.readline()))
    
    count = 0
    
    # 3. 뒤에서부터(큰 동전부터) 한 번만 순회 (최적화 포인트)
    # reversed()를 사용하면 리스트를 뒤집어서 효율적으로 접근 가능합니다.
    for coin in reversed(money_ls):
        if K == 0: 
            break  # 목표 금액을 다 채웠으면 즉시 종료
        
        if coin <= K:
            # 몫(//)을 통해 한 번에 개수를 더하고, 나머지(%)로 남은 돈 갱신
            count += K // coin
            K %= coin
            
    print(count)

if __name__ == "__main__":
    main()
"""