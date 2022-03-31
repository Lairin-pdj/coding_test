from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline

def rotate(n):
    # 주어진 2차원 배열을 회전시켜주는 함수
    # 열 단위로 따서 뒤집어서 넣어 90도 회전
    # 1 2 3    1 4 7    7 4 1
    # 4 5 6 -> 2 5 8 -> 8 5 2
    # 7 8 9    3 6 9    9 6 3
    return list(map(list, zip(*n[::-1])))

# 파싱
table = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# 가능한 모양 생성 
shape = []
for i in range(5):
    temp = []
    for _ in range(4):
        temp.append(table[i])
        table[i] = rotate(table[i])
    shape.append(temp)

# 정답 체크
answer = 1000000000
flag = False

# 가능한 경우의 수
for nums in permutations(range(0, 5), 5):
    for a in range(4):
        # 가능성이 존재하지 않는 경우 스킵
        if shape[nums[0]][a][0][0] == 0:
            continue
        # 이미 최소값이 확인 된 경우
        if answer == 12:
            break
        
        for b in range(4):
            # 이미 최소값이 확인 된 경우
            if answer == 12:
                break
            
            for c in range(4):
                # 이미 최소값이 확인 된 경우
                if answer == 12:
                    break
                
                for d in range(4):
                    # 이미 최소값이 확인 된 경우
                    if answer == 12:
                        break
                    
                    for e in range(4):
                        # 이미 최소값이 확인 된 경우
                        if answer == 12:
                            break
                        
                        # 새로운 테이블 조합 생성
                        newtable = [shape[nums[0]][a], shape[nums[1]][b], shape[nums[2]][c], shape[nums[3]][d], shape[nums[4]][e]]
                    
                        # 최단거리 진행
                        if newtable[0][0][0] == 1 and newtable[4][4][4] == 1:
                            queue = deque([(0, 0, 0, 0)])
                            check = set([(0, 0, 0)])
                            dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
                            
                            while queue:
                                x, y, z, count = queue.popleft()
                                
                                # 탈출 성공    
                                if (x, y, z) == (4, 4, 4):
                                    answer = min(answer, count)
                                    flag = True
                                    break
                                
                                for i in range(6):
                                    ax = x + dx[i]
                                    ay = y + dy[i]
                                    az = z + dz[i]
                                    
                                    if 0 <= ax <= 4 and 0 <= ay <= 4 and 0 <= az <= 4 and newtable[ax][ay][az] == 1 and (ax, ay, az) not in check:
                                        queue.append((ax, ay, az, count + 1))
                                        check.add((ax, ay, az))

# 결과 출력
if flag:
    print(answer)
else:
    print(-1)
