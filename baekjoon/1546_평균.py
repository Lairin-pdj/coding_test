n = int(input())
nums = list(map(int, input().split(" ")))
high = max(nums)

mani = []
for i in nums:
    mani.append((i / high) * 100)

print(sum(mani) / len(mani))
