def solution(wallpaper):
    answer = []
    max_x = 0
    max_y = 0
    min_x = len(wallpaper)
    min_y = len(wallpaper[0])
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i < min_x:
                    min_x = i
                if j < min_y:
                    min_y = j
                if i+1 > max_x:
                    max_x = i+1
                if j+1 > max_y:
                    max_y = j+1
                    

    answer.append(min_x)
    answer.append(min_y)
    answer.append(max_x)
    answer.append(max_y)
    return answer