f = open("02/input.txt", "r")
lines = [line.rstrip('\n').split() for line in f]

horizontalPosition = 0
depth = 0
aim = 0

for [direction, amount] in lines:
    amount = int(amount)
    if (direction == 'forward'):
        horizontalPosition += amount
        depth += (aim * amount)
    elif (direction == 'down'):
        aim += amount
    elif(direction == 'up'):
        aim -= amount

print(horizontalPosition * depth)