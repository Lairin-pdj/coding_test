n = int(input())

for _ in range(n):
    nums = list(map(int, input().split(" ")))
    avg = sum(nums[1:]) / len(nums[1:])
    
    count = 0
    for i in nums[1:]:
        if i > avg:
            count += 1
    
    print("{:.3f}%".format(round((count / (len(nums) - 1)) * 100, 3)))
