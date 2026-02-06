# 조합(nCr) 사용하기

def solve():
    # M(동쪽)과 N(서쪽) 입력 (예시: M=29, N=13)
    # 실제 문제 풀이 시에는 input()을 활용하자.
    import sys
    # 입력된 모든 글자를 한꺼번에 가져와서 공백이나 줄바꿈 기준으로 다 쪼개서 리스트(data)에 넣는다.
    input = sys.stdin.read
    data = input().split()  # 이미 모든 숫자가 리스트에 담겨 있어서 인덱스로 접근만 하면 됨.
    
    # 테스트 케이스 개수 처리
    T = int(data[0])
    idx = 1
    
    # 1. DP 테이블 초기화 (최대 범위 30x30 정도)
    # dp[i][j]는 iCj의 값을 의미함.
    # dp = [[0] * 31 for _ in range(31)]
    dp = []
    for _ in range(31):
      row = [0] * 31
      dp.append(row)
    
    # 2. 파스칼의 삼각형 채우기
    for i in range(31):
        for j in range(i + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # 점화식: nCr = n-1Cr-1 + n-1Cr
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    # 3. 결과 출력
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        print(dp[M][N])
        idx += 2

solve()
