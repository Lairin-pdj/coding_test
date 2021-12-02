import sys
input = sys.stdin.readline

# 파싱
n = int(input())

for _ in range(n):
    s = input()
    idx1 = s.find(" ")
    r = int(s[:idx1])
    idx2 = s[idx1 + 1:].find(" ")
    c = int(s[idx1 + 1:idx1 + idx2 + 1])
    string = s[idx1 + idx2 + 2:]
    mat = [["0" for _ in range(c)] for _ in range(r)]
    
    # 문자열 숫자화
    nums = ""
    for i in string:
        temp = ord(i)
        if temp == 32 or temp == 10:
            nums += "00000"
        else:
            nums += bin(temp - 64)[2:].zfill(5)
    
    # 문자열 행렬에 삽입
    count = -1
    a, b = 0, -1
    check = 1
    asize, bsize = r, c
    while asize and bsize:
        for _ in range(bsize):
            count += 1
            b += check
            if count < len(nums):
                mat[a][b] = nums[count]
        asize -= 1
        
        for _ in range(asize):
            count += 1
            a += check
            if count < len(nums):
                mat[a][b] = nums[count]
        bsize -= 1
            
        check = -check
    
    # 행렬 출력
    for line in mat:
        for i in line:
            print(i, end = "")
    print()
