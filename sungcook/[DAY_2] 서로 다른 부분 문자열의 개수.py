# 1. 백준, 정렬, 64.417%, https://www.acmicpc.net/problem/11478

def solve():
    input_str = input("")
    
    lst = []
    for i in range(1, len(input_str)+1):
        a = len(input_str)-i
        for j in range(0, a+1):
            lst.append(input_str[j:j+i])
    print(len(set(lst)))
        
        



solve()