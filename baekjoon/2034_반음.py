import sys
input = sys.stdin.readline

# 파싱
n = int(input())
score = [int(input()) for _ in range(n)]

# 건반
piano = ["A", "", "B", "C", "", "D", "", "E", "F", "", "G", ""]

# 순회
for i in range(11):
    if piano[i] != "":
        temp = i
        flag = True
        
        for j in score:
            temp += j
            temp = temp % 12
            if piano[temp] == "":
                flag = False
                break

        if flag:
            print(piano[i], piano[temp])
