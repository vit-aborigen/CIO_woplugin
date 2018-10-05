def stone_wall(wall):
    wall_normalized = [char for char in wall.split('\n')][1:-1] #conver to list and remove \n
    wall_rotated = list(zip(*wall_normalized[::-1]))            #rotate wall-matrix clockwise
    result = max(wall_rotated, key = lambda x: x.count('0'))
    return wall_rotated.index(result)