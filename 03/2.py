import math  # we could always use more math

slopes = [
    {'slope': (1, 1), 'currentPos': (1, 1), 'treesFound': 0},
    {'slope': (3, 1), 'currentPos': (1, 1), 'treesFound': 0},
    {'slope': (5, 1), 'currentPos': (1, 1), 'treesFound': 0},
    {'slope': (7, 1), 'currentPos': (1, 1), 'treesFound': 0},
    {'slope': (1, 2), 'currentPos': (1, 1), 'treesFound': 0},
]

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]

numLines = len(lines)

for combo in slopes:
    currentLineNumber = 1

    while currentLineNumber < numLines:
        # move position by slope
        combo['currentPos'] = tuple(map(sum, zip(combo['currentPos'], combo['slope'])))  # so cleeeaaaannnnn

        currentLineNumber = combo['currentPos'][1]
        currentLine = lines[currentLineNumber-1]

        # check if our line is long enough for our horizontal movement
        while len(currentLine) < combo['currentPos'][0]:
            # just add the line to itself since it repeats to the right until we have enough length
            currentLine += currentLine

        if list(currentLine)[combo['currentPos'][0]-1] == '#':  # check if it's a tree
            combo['treesFound'] += 1

treesFound = [combo['treesFound'] for combo in slopes]
print('Trees hit:', math.prod(treesFound))  #
