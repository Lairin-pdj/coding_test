from math import gcd

def solution(w,h):    
    #총 사각형 갯수 - 직선이 지나가는 선의 갯수 + 교점을 지나는 횟수
    return w * h - (w + h) + gcd(w, h)
