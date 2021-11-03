import math

def solution(arr):
    
    # 두 수를 뽑아 두 수의 최소공배수를 다시 삽입하는 과정을 반복
    while len(arr) > 1:
        n1 = arr.pop()
        n2 = arr.pop()
        
        arr.append((n1 * n2) // math.gcd(n1, n2))
    
    return arr[0]
