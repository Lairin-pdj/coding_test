def solution(maps):             
    maps[0][0] = 2
    
    queue = [[0, 0, 1]]                                   
    
    while len(queue) != 0:                                  # bfs를 통한 탐색
        x, y, z = queue.pop(0)

        if len(maps[0]) - 1 == x and len(maps) - 1 == y:    # 도착시 종료
            return z
        
        if len(maps[0]) > x + 1 and maps[y][x + 1] == 1:    # 동쪽으로 이동
            maps[y][x + 1] = 2
            queue.append([x + 1, y, z + 1])
            
        if 0 <= x - 1 and maps[y][x - 1] == 1:              # 서쪽으로 이동
            maps[y][x - 1] = 2
            queue.append([x - 1, y, z + 1])
        
        if len(maps) > y + 1 and maps[y + 1][x] == 1:       # 남쪽으로 이동
            maps[y + 1][x] = 2
            queue.append([x, y + 1, z + 1])
        
        if 0 <= y - 1 and maps[y - 1][x] == 1:              # 북쪽으로 이동
            maps[y - 1][x] = 2
            queue.append([x, y - 1, z + 1])
            
    return -1                                               # 전부 이동하여도 도착하지 못할 경우
