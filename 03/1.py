treesFound = 0
slope = (3, 1)

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]

# we start on the first line, so when we start moving down we basically don't need the first line and can remove it
lines.pop(0)

currentPos = (1, 1)
currentLineNumber = 1

for line in lines:
    currentLineNumber += 1
    currentPos = tuple(map(sum, zip(currentPos, slope)))  # so cleeeaaaannnnn

    if currentLineNumber == currentPos[1]:  # check if we've moved to the next line vertically based on our slope
        while len(line) < currentPos[0]:  # check if our line is long enough for our horizontal movement
            line += line  # just add the line to itself since it repeats to the right until we have enough length

        if list(line)[currentPos[0]-1] == '#':  # check if it's a tree
            treesFound += 1

print('Trees hit:', treesFound)  # 220
