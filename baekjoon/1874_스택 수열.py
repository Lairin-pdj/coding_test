from collections import defaultdict
import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# 출력준비
check = False
answer = []
put = 0
get = set()
temp = 0
for _ in range(n):
    goal = int(input())
    if put < goal:
        for _ in range(goal - put):
            answer.append("+")
        put = goal
        answer.append("-")
        get.add(goal)
        temp = goal
    else:
        if goal in get:
            check = True
            break
        else:
            if temp < goal:
                check = True
                break
            else:
                for i in range(temp - 1, goal - 1, -1):
                    if i not in get:
                        answer.append("-")
                        get.add(i)
                temp = goal

# 출력  
if check:
    print("NO")
else:
    for i in answer:
        print(i)
