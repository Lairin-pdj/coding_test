def rotate(n):                                                          # 주어진 2차원 배열을 회전시켜주는 함수
    l = len(n)
    t = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            t[j][l - 1 - i] = n[i][j]
    return t

def check(t, m, n):                                                     # t 배열의 특정 가운데가 전부 1인지 체크하는 함수
    for i in range(m, m + n):
        for j in range(m, m + n):
            if t[i][j] != 1:
                return False
    return True

def attach(t, k, m, n, l):                                              # 주어진 배열을 더해주는 함수
    for i in range(l):
        for j in range(l):
            t[m + i][n + j] += k[i][j]
    
def detach(t, k, m, n, l):                                              # 주어진 배열을 빼주는 함수
    for i in range(l):
        for j in range(l):
            t[m + i][n + j] -= k[i][j]

def solution(key, lock):
    l1 = len(key)
    l2 = len(lock)
    
    t = [[0] * (l2 +  2 * l1 - 2) for _ in range(l2 +  2 * l1 - 2)]     # (key point)주변의 추가적인 장소를 생성하여 전부 대입해볼 수 있도록 생성
                                                                        
    attach(t, lock, l1 - 1, l1 - 1, l2)
        
    if check(t, l1 - 1, l2):
        return True  
    
    for _ in range(4):                                                  # 모든 경우의 수를 체크
        for i in range(l1 + l2 - 1):
            for j in range(l1 + l2 - 1):
                attach(t, key, i, j, l1)
                if check(t, l1 - 1, l2):                                # 성립시 바로 반환
                    return True  
                detach(t, key, i, j, l1)
                
        key = rotate(key)
    
    return False                                                        # 모든 경우의 수가 실패할 경우
