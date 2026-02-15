def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    valid_chars = [char for char in alphabet if char not in skip]
    
    answer = ''
    
    for char in s:
        current_pos = valid_chars.index(char)
        new_pos = (current_pos + index) % len(valid_chars)
        answer += valid_chars[new_pos]
        
    return answer
