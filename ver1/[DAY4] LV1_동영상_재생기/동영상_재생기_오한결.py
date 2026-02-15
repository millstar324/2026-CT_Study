def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(t):
        m, s = map(int, t.split(':'))
        return m * 60 + s

    def to_str(x):
        return f"{x//60:02d}:{x%60:02d}"

    L = to_sec(video_len)
    p = to_sec(pos)
    os = to_sec(op_start)
    oe = to_sec(op_end)

    if os <= p <= oe:
        p = oe

    for cmd in commands:
        if cmd == "prev":
            p = max(0, p - 10)
        else:  # "next"
            p = min(L, p + 10)

        if os <= p <= oe:
            p = oe

    return to_str(p)
