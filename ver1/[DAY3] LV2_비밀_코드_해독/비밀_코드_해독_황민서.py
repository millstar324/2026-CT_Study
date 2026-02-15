from itertools import combinations

def solution(n, q, ans):
    count = 0
    # 1부터 n까지의 숫자 중 5개를 뽑는 모든 조합을 생성.
    for candidate in combinations(range(1, n + 1), 5):
        is_possible = True
        
        # 각 시도(q)와 시스템 응답(ans)이 일치하는지 확인.
        for i in range(len(q)):
            # 현재 조합(candidate)과 입력한 정수(q[i]) 사이의 교집합 개수를 구한다.
            # set을 활용하면 교집합 개수를 빠르게 구할 수 있음.
            match_count = len(set(candidate) & set(q[i]))
            
            # 시스템의 응답과 일치하지 않으면 이 조합은 비밀 코드가 될 수 없음.
            if match_count != ans[i]:
                is_possible = False
                break
        
        # 모든 시도 조건을 만족하면 카운트를 증가시킨다.
        if is_possible:
            count += 1
            
    return count
