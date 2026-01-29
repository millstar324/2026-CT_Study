def solution(s, skip, index):
    skip_set = set(skip)
    allowed = [chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in skip_set]
    pos_map = {ch: i for i, ch in enumerate(allowed)}

    m = len(allowed)
    out = []
    for ch in s:
        out.append(allowed[(pos_map[ch] + index) % m])
    return ''.join(out)
