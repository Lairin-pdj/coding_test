import sys
input = sys.stdin.readline

# 파싱
a, b = map(int, input().split())

# 1 갯수 세는 함수
def count(n):
    start = n
    result = 0
    times = 1

    while n >= 2:
        temp = n % 2
        n = n // 2
        result += n * times
        if temp != 0:
            result += start % times + 1
        times *= 2
    
    result += start - times + 1
    
    return result

# a - 1, b의 갯수를 구한 뒤 빼주는 방식
print(count(b) - count(a - 1))
