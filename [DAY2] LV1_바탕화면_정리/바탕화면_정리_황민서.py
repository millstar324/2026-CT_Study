def solution(wallpaper):
    # 초기값 설정: 최소값은 아주 큰 수로, 최대값은 아주 작은 수로 설정
    lux, luy = float('inf'), float('inf')
    rdx, rdy = 0, 0
    
    # 바탕화면 전체를 순회
    for i in range(len(wallpaper)):          # i: 세로 좌표 (행)
        for j in range(len(wallpaper[i])):   # j: 가로 좌표 (열)
            if wallpaper[i][j] == '#':      
                # 시작점 (최소값 찾기)
                lux = min(lux, i)
                luy = min(luy, j)
                
                # 끝점 (최대값 찾기)
                # 드래그 끝점은 파일 위치보다 1칸 더 커야 함
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)
                
    return [lux, luy, rdx, rdy]
