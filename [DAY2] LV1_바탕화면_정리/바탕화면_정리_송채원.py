def find_ls(w, r, c):
    ls = c-1
    for i in w:
        for j, v in enumerate(list(i)):
            if  (v == '#') and (j < ls):
                ls = j
                break
        
    return ls

def find_us(w,r,c):
    us = r-1
    for i,v in enumerate(w):
        if ('#' in v) and i<us: 
            us = i
    
    return us


def find_re(w,r,c,ls):
    re = ls
    for i in w:
        for j,v in reversed(list(enumerate(list(i)))):
            if v=='#' and (j > re):
                re = j
                break
                
    return re

def find_de(w,r,c,us):
    de = us
    for i,v in reversed(list(enumerate(w))):
        if ( '#' in v) and (i> de):
            de = i
            
    return de
            
        
                

def solution(wallpaper):
    row = len(wallpaper)
    col = len(wallpaper[0])
    
    ls = find_ls(wallpaper, row, col)
    us = find_us(wallpaper, row, col)
    re = find_re(wallpaper, row, col, ls)
    de = find_de(wallpaper, row, col, us)
    
    
    
    
    
   
    return [us, ls, de+1, re+1]
2
3
4
5
6
7
8

# def solution(wall):
#     a, b = [], []
#     for i in range(len(wall)):
#         for j in range(len(wall[i])):
#             if wall[i][j] == "#":
#                 a.append(i)
#                 b.append(j)
#     return [min(a), min(b), max(a) + 1, max(b) + 1]