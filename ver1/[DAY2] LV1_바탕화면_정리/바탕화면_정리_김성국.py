def solution(wallpaper):
    result = []
    listed_wallpaper = []
    
    for i in range(len(wallpaper)):
        listed_wallpaper.append(list(wallpaper[i]))
    
    
    for i in range(len(listed_wallpaper)):
        if '#' in listed_wallpaper[i]:
            result.append(i)
            break
        else:
            continue
            
    min_left = len(listed_wallpaper[0])-1
    
    for i in range(len(listed_wallpaper)):
        if '#' in listed_wallpaper[i] and listed_wallpaper[i].index('#') < min_left:
            min_left = listed_wallpaper[i].index('#')
            
    result.append(min_left)
            
    for j in range(len(listed_wallpaper)-1, -1, -1):
        if '#' in listed_wallpaper[j]:
            result.append(j+1)
            break
        
    
    max_right = 0
    for i in range(len(listed_wallpaper)):
        if '#' in listed_wallpaper[i]:
            for j in range(len(listed_wallpaper[i])):
                if listed_wallpaper[i][j] == '#' and j >= max_right:
                    max_right = j+1
            
    result.append(max_right)
                   
            
            
    
        
    return result