import sys
input = sys.stdin.readline

# 파싱
n, q = map(int, input().split(" "))
songs = []
for _ in range(n):
    songs.append(int(input()))
queries = []
for _ in range(q):
    queries.append(int(input()))

# 누적합
for i in range(1, n):
    songs[i] += songs[i - 1]

# 쿼리 처리
for query in queries:
    for i in range(n):
        if songs[i] > query:
            print(i + 1)
            break
