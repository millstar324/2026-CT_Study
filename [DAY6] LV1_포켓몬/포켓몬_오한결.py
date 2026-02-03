def solution(nums):
    n = len(nums)
    unique = len(set(nums))
    return min(unique, n // 2)
