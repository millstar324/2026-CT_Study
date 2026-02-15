def solution(nums):
    num = len(nums)/2
    set_num = set(nums)
    if len(set_num) < num:
        return len(set_num)
    else:
        return num