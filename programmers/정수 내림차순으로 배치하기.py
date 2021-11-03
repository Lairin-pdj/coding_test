def solution(n):
    temp = list(str(n))
    temp.sort(reverse = True)
    return int("".join(temp))
