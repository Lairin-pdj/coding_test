import sys
input = sys.stdin.readline
    
# 파싱
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

# 순회
answer = 0
check = 1
tempo = 1
start = [n // 2, n // 2]

# 회전 이동
for _ in range(n):
    for _ in range(tempo):
        start[1] -= check
        
        # 탈출
        if start[1] < 0:
            break
        
        # 모래 배분
        sand = table[start[0]][start[1]]
        if sand != 0:
            table[start[0]][start[1]] = 0
            use = 0
            
            # 벗어나는지 파악
            xm1, xp1 = (start[0] > 0), (start[0] < n - 1)
            xm2, xp2 = (start[0] > 1), (start[0] < n - 2)
            if check == 1:
                ym1, yp1 = (start[1] > 0), (start[1] < n - 1)
                ym2, yp2 = (start[1] > 1), (start[1] < n - 2)
            else:
                yp1, ym1 = (start[1] > 0), (start[1] < n - 1)
                yp2, ym2 = (start[1] > 1), (start[1] < n - 2)
                
            
            temp = (sand * 7) // 100
            use += 2 * temp
            if xm1:
                table[start[0] - 1][start[1]] += temp
            else:
                answer += temp
            if xp1:
                table[start[0] + 1][start[1]] += temp
            else:
                answer += temp
            
            temp = (sand * 2) // 100
            use += 2 * temp
            if xm2:
                table[start[0] - 2][start[1]] += temp
            else:
                answer += temp
            if xp2:
                table[start[0] + 2][start[1]] += temp
            else:
                answer += temp
            
            temp = (sand * 10) // 100
            use += 2 * temp
            if xm1 and ym1:
                table[start[0] - 1][start[1] - check] += temp
            else:
                answer += temp
            if xp1 and ym1:
                table[start[0] + 1][start[1] - check] += temp
            else:
                answer += temp
            
            temp = (sand * 1) // 100
            use += 2 * temp
            if xm1 and yp1:
                table[start[0] - 1][start[1] + check] += temp
            else:
                answer += temp
            if xp1 and yp1:
                table[start[0] + 1][start[1] + check] += temp
            else:
                answer += temp
            
            temp = (sand * 5) // 100
            use += temp
            if ym2:
                table[start[0]][start[1] - (2 * check)] += temp
            else:
                answer += temp
            
            if ym1:
                table[start[0]][start[1] - check] += sand - use
            else:
                answer += sand - use
    
    # 탈출
    if start[1] < 0:
        break

    for _ in range(tempo):
        start[0] += check
        
        # 모래 배분
        sand = table[start[0]][start[1]]
        if sand != 0:
            table[start[0]][start[1]] = 0
            use = 0
            
            # 벗어나는지 파악
            ym1, yp1 = (start[1] > 0), (start[1] < n - 1)
            ym2, yp2 = (start[1] > 1), (start[1] < n - 2)
            if check == 1:
                xm1, xp1 = (start[0] > 0), (start[0] < n - 1)
                xm2, xp2 = (start[0] > 1), (start[0] < n - 2)
            else:
                xp1, xm1 = (start[0] > 0), (start[0] < n - 1)
                xp2, xm2 = (start[0] > 1), (start[0] < n - 2)
                
            
            temp = (sand * 7) // 100
            use += 2 * temp
            if ym1:
                table[start[0]][start[1] - 1] += temp
            else:
                answer += temp
            if yp1:
                table[start[0]][start[1] + 1] += temp
            else:
                answer += temp
            
            temp = (sand * 2) // 100
            use += 2 * temp
            if ym2:
                table[start[0]][start[1] - 2] += temp
            else:
                answer += temp
            if yp2:
                table[start[0]][start[1] + 2] += temp
            else:
                answer += temp
            
            temp = (sand * 10) // 100
            use += 2 * temp
            if xp1 and ym1:
                table[start[0] + check][start[1] - 1] += temp
            else:
                answer += temp
            if xp1 and yp1:
                table[start[0] + check][start[1] + 1] += temp
            else:
                answer += temp
            
            temp = (sand * 1) // 100
            use += 2 * temp
            if xm1 and ym1:
                table[start[0] - check][start[1] - 1] += temp
            else:
                answer += temp
            if xm1 and yp1:
                table[start[0] - check][start[1] + 1] += temp
            else:
                answer += temp
            
            temp = (sand * 5) // 100
            use += temp
            if xp2:
                table[start[0] + (2 * check)][start[1]] += temp
            else:
                answer += temp
            
            if xp1:
                table[start[0] + check][start[1]] += sand - use
            else:
                answer += sand - use

    check = -check
    tempo += 1

# 결과 출력
print(answer)
