import sys
input = sys.stdin.readline

# 파싱
n = int(input())
m = int(input())
string = input().rstrip()
temp = string[:2 * n]

# 체킹
count = 0
check = 0
pos = 0
while pos < m - 2:
    if string[pos] == "I" and string[pos + 1] == "O" and string[pos + 2] == "I":
        check += 1
        if check == n:
            count += 1
            check -= 1
        pos += 2
    else:
        check = 0
        pos += 1

# 결과 출력
print(count)
