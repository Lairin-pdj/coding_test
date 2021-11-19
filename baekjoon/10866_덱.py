from collections import deque
import sys
input = sys.stdin.readline

# 파싱
n = int(input())

# 쿼리 진행
queue = deque()
for _ in range(n):
    query = input().rstrip().split()

    if query[0] == "push_back":
        queue.append(int(query[1]))
    elif query[0] == "push_front":
        queue.appendleft(int(query[1]))
    elif query[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif query[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif query[0] == "size":
        print(len(queue))
    elif query[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif query[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
