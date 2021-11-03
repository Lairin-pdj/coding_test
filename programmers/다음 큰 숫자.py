from collections import Counter

def solution(n):
    answer = n + 1
    count = Counter(str(bin(n))[2:])["1"]
    
    while True:
        if Counter(str(bin(answer))[2:])["1"] == count:
            return answer
        answer += 1
