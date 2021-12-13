f = open("03/input.txt", "r")
lines = [line.rstrip('\n') for line in f]

# # PART 1
gamma = ''
epsilon = ''
for pos in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if (line[pos] == '0'):
            zeros += 1
        else:
            ones+= 1
    if (zeros > ones):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma, 2) * int(epsilon, 2))

# PART 2
oxygen = 0
carbon = 0

def countZerosAndOnes(lines, pos):
    zeros = 0
    ones = 0
    for line in lines:
        if (line[pos] == '0'):
            zeros += 1
        else:
            ones += 1
    return [zeros, ones]

for pos in range(len(lines[0])):
    [zeros, ones] = countZerosAndOnes(lines, pos)
    for line in list(lines):
        if line[pos] == '0' and zeros <= ones:
            lines.remove(line)
        elif line[pos] == '1' and zeros > ones:
            lines.remove(line)
        if len(lines) == 1:
            oxygen = lines[0]

f = open("03/input.txt", "r")
lines = [line.rstrip('\n') for line in f]
for pos in range(len(lines[0])):
    [zeros, ones] = countZerosAndOnes(lines, pos)
    for line in list(lines):
        if line[pos] == '0' and zeros > ones:
            lines.remove(line)
        elif line[pos] == '1' and zeros <= ones:
            lines.remove(line)
        if len(lines) == 1:
            carbon = lines[0]

print(int(oxygen, 2) * int(carbon, 2))
