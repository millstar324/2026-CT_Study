def solution(players, m, k):

    
    cur_server_t = []
    total_c=0
    
    
    
    
    for i, cur_p in enumerate(players):
        # print(f"==={i}번째 시간====")
        #시간 지남 처리 로직
        if len(cur_server_t)> 0:
            for i,t in enumerate(cur_server_t):
                cur_server_t[i] -= 1
                if cur_server_t[i] <= 0:
                    cur_server_t[i] = -1
            cur_server_t = [ x for x in cur_server_t if x != -1]
        
        
        #새로운 서버 추가 체크 로직
        count_live_server = len(cur_server_t)
        need_server = cur_p // m
        add_server = need_server - count_live_server
        # print(f"{add_server}개 서버 추가 필요")
        
        if add_server > 0:
            for _ in range(add_server):
                cur_server_t.append(k)
                total_c += 1
                
        # print(f"현재 서버 상황: {cur_server_t}")
                
        
    return total_c