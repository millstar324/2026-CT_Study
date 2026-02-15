def to_seconds(time_str):
    # mm:ss 형식을 초 단위 정수로 변환
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def to_time_format(seconds):
    # 초 단위 정수를 mm:ss 형식 문자열로 변환
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    # 모든 시간을 초 단위로 변환
    curr = to_seconds(pos)
    v_len = to_seconds(video_len)
    o_start = to_seconds(op_start)
    o_end = to_seconds(op_end)
    
    # 1. 시작 위치가 오프닝 구간인지 확인
    if o_start <= curr <= o_end:
        curr = o_end
        
    for cmd in commands:
        # 2. 명령어 수행
        if cmd == "prev":
            curr = max(0, curr - 10)
        elif cmd == "next":
            curr = min(v_len, curr + 10)
            
        # 3. 수행 후 오프닝 구간인지 다시 확인
        if o_start <= curr <= o_end:
            curr = o_end
            
    return to_time_format(curr)
