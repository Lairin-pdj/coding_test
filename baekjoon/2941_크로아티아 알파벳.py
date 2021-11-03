line = input()

count = 0
i = 0
while i < len(line):
    # 3개
    if line[i:i + 3] == "dz=":
        count += 1
        i += 3
        continue
    
    # 2개
    if line[i:i + 2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        count += 1
        i += 2
        continue
    
    # 1개
    count += 1
    i += 1

print(count)
