line = input().split(" ")

count = 0
if line[0] == "":
    count += 1

if line[-1] == "":
    count += 1

print(len(line) - count)
