f = open("01/input.txt", "r")
vals = [int(line.rstrip('\n')) for line in f]

# PART 1
increases = 0
for x in range(len(vals)-1):
    if vals[x+1] > vals[x]:
        increases += 1
print(increases)

# PART 2
increases = 0
for x in range(len(vals)-3):
    sum1 = vals[x] + vals[x+1] + vals[x+2]
    sum2 = vals[x+1] + vals[x+2] + vals[x+3]
    if sum2 > sum1:
        increases += 1
print(increases)