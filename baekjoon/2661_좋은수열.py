import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

def check(nums):
    for i in range(1, (len(nums) // 2) + 1):
        if nums[len(nums) - 2 * i:len(nums) - i] == nums[len(nums) - i:]:
            return False
    
    return True


def dfs(nums):
    global isDone
    
    if isDone == True:
        return
    
    if len(nums) == n:
        print(nums)
        isDone = True
        return
    else:
        for i in range(1, 4):
            temp = nums + str(i)
            
            if nums[-1:] != str(i) and check(temp):
                dfs(temp)
        

# 파싱
n = int(input())

answer = ""
isDone = False

dfs("")

print(answer)
