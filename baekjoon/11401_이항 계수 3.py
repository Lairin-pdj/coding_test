import sys
input = sys.stdin.readline

def gop(num, time):
    if time == 0:
        return 1
        
    if time % 2 == 0:
        return gop(num, time // 2) ** 2 % a
    else:
        return gop(num, time // 2) ** 2 * num % a
    

n, k = map(int, input().split(" "))
a = 1000000007

fac = [i for i in range(n + 1)]

for i in range(2, n + 1):
    fac[i] = fac[i - 1] * i % a
    
print(fac[n] * gop((fac[n - k] * fac[k]), (a - 2)) % a)
