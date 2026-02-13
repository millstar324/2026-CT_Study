import sys

def solve():
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().strip() for _ in range(n)]


    alpha_weights = {}

    for word in words:

        for i, char in enumerate(word):
            power = 10 ** (len(word) - 1 - i)
            if char in alpha_weights:
                alpha_weights[char] += power
            else:
                alpha_weights[char] = power


    sorted_weights = sorted(alpha_weights.values(), reverse=True)

    total_sum = 0
    current_digit = 9
    for weight in sorted_weights:
        total_sum += weight * current_digit
        current_digit -= 1

    print(total_sum)

if __name__ == "__main__":
    solve()