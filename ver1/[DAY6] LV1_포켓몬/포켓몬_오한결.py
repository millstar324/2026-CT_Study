def solution(number, limit, power):
    cnt = [0] * (number + 1)

    for k in range(1, number + 1):
        for m in range(k, number + 1, k):
            cnt[m] += 1

    total = 0
    for i in range(1, number + 1):
        if cnt[i] > limit:
            total += power
        else:
            total += cnt[i]
    return total
