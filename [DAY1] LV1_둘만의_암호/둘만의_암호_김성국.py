def solution(s, skip, index):
    skip_set = set(skip)
    res = []
    for ch in s:
        cur = ord(ch)
        moved = 0
        while moved < index:
            cur += 1
            if cur > ord('z'):
                cur = ord('a')
            if chr(cur) in skip_set:
                continue
            moved += 1
        res.append(chr(cur))
    return ''.join(res)
