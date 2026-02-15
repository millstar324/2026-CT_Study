import sys

LIMIT = 10**18
TAU_MAX = 150

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

min_val = [LIMIT + 1] * (TAU_MAX + 1)

def dfs(idx: int, last_exp: int, val: int, tau: int) -> None:
    # record best for this divisor count
    if val < min_val[tau]:
        min_val[tau] = val

    if idx >= len(PRIMES):
        return

    p = PRIMES[idx]
    cur = val
    for e in range(1, last_exp + 1):
        cur *= p
        if cur > LIMIT:
            break
        ntau = tau * (e + 1)
        if ntau > TAU_MAX:
            break
        dfs(idx + 1, e, cur, ntau)

dfs(0, 60, 1, 1)

def solve_one(N: int) -> int:
    # Need exactly N rectangle types:
    # either d(M)=2N (non-square) or d(M)=2N-1 (square)
    a = min_val[2 * N]
    b = min_val[2 * N - 1]
    return a if a < b else b

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        out.append(str(solve_one(n)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
