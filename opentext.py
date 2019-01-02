key = open("teksts.txt")
n = 0
for line in key:
    n = n + 1
    if line.startswith("pi"):
        print(line)
print(n)
