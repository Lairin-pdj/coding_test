import sys
input = sys.stdin.readline

# 선언
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

# 파싱
first = input().rstrip()
second = input().rstrip()
third = input().rstrip()

# 결과 출력
print(((color.index(first) * 10) + color.index(second)) * (10 ** color.index(third)))
