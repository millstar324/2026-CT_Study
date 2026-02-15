def solution(wallpaper):
    rows = len(wallpaper)
    cols = len(wallpaper[0])

    min_r, min_c = 50, 50
    max_r, max_c = -1, -1

    for r in range(rows):
        for c in range(cols):
            if wallpaper[r][c] == '#':
                min_r = min(min_r, r)
                min_c = min(min_c, c)
                max_r = max(max_r, r)
                max_c = max(max_c, c)

    return [min_r, min_c, max_r + 1, max_c + 1]
