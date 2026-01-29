def next_char(s):
    return chr(ord(s)+1)

def ls_to_str(ls):
    return "".join(ls)

def cycle(s, sk, i):
    if i == 0:
        return s
    
    if next_char(s) in sk:
        if s == 'z' :
            return cycle('a', sk, i)
        
        return cycle(next_char(s), sk, i)
    
    else:
        if s == 'z' :
            if 'a' in sk:
                return cycle('a', sk, i)
            else:
                return cycle('a', sk, i-1)
            
        return cycle(next_char(s), sk, i-1)

def solution(s, skip, index):
    s_len = len(s)
    s_list = list(s)
    
    for i in range(s_len):
        s_list[i] = cycle(s_list[i], skip, index)
    
    
    
    answer = ls_to_str(s_list)
    return answer