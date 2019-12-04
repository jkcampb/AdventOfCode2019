filename = './input.txt'

fh = open(filename, "r")

total = 0
for line in fh:
    total += int(float(line)/3) - 2

print(int(total))
