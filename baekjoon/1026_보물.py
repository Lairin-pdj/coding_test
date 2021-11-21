import sys
input = sys.stdin.readline

# 파싱
n = int(input())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort(reverse = True)

# 그리디
count = 0
for i, j in zip(a, b):
    count += i * j

# 결과 출력
print(count)
