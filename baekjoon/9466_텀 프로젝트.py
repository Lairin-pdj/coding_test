import sys
input = sys.stdin.readline

# 파싱
t = int(input())
for _ in range(t):
    n = int(input())
    mans = [0] + list(map(int, input().split()))
    
    # 체크용 배열
    check = [0 for _ in range(n + 1)]

    # 탐색
    for i in range(1, n + 1):
        if mans[i] == i:
            check[i] = 1
        elif mans[i] > i and check[i] == 0:
            line = [i]
            linein = set([i])
            temp = i
            # 연결된 그래프를 따라 진행
            while mans[temp] not in linein and check[mans[temp]] == 0:
                temp = mans[temp]
                line.append(temp)
                linein.add(temp)
            
            # 연결이 제대로 된 경우
            if check[mans[temp]] == 0:
                item = line.pop()
                while item != mans[temp]:
                    check[item] = 1
                    item = line.pop()
                check[item] = 1
            # 도중에 실패할 요소를 만난 
            else:
                for j in line:
                    check[j] = -1

    # 결과 출력
    answer = 0
    for i in range(1, n + 1):
        if check[i] != 1:
            answer += 1
    print(answer)
