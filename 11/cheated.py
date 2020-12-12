# source:
# https://www.reddit.com/r/adventofcode/comments/kaw6oz/2020_day_11_solutions/gfgaofi
# i hate myself

def readInput():
    with open('input.txt', 'r') as file:
        data = file.read()
    lines = list()
    for d in data.split("\n"):
        if (d != ""):
            lines.append(list(d))
    return lines

def compare(array2d1,array2d2):
    for i in range(len(array2d1)):
        for j in range(len(array2d1[i])):
            if (array2d1[i][j] != array2d2[i][j]):
                return False
    return True

def getValue(array2d, i, j):
    if (i < 0 or j < 0 or i >= len(array2d) or j >= len(array2d[0])):
        return ''
    else:
        return array2d[i][j]

def deepCopy(array2d1):
    array2d2 = list()
    for i in range(len(array2d1)):
        array2d2.append(list())
        for j in range(len(array2d1[i])):
            array2d2[i].append(array2d1[i][j])
    return array2d2

def printArray(cycles, array2d):
    print('Round', cycles)
    for i in array2d:
        for j in i:
            print(j,end='')
        print()
    print()

def countSeats(lines):
    seats = 0
    for l in lines:
        seats += l.count('#')
    return seats

def occupiedSeatsVisible(array2d, i, j):
    around = ['?','?','?',
              '?',    '?',
              '?','?','?']
    radius = 1
    while around.count('?') > 0:
        if (around[0] == '?'): # top left
            t = getValue(array2d, i-radius, j-radius)
            if t in ['#','L','']: around[0] = t
        if (around[1] == '?'): # top
            t = getValue(array2d, i-radius, j)
            if t in ['#','L','']: around[1] = t
        if (around[2] == '?'): # top right
            t = getValue(array2d, i-radius, j+radius)
            if t in ['#','L','']: around[2] = t
        if (around[3] == '?'): # left
            t = getValue(array2d, i,        j-radius)
            if t in ['#','L','']: around[3] = t
        if (around[4] == '?'): # right
            t = getValue(array2d, i,        j+radius)
            if t in ['#','L','']: around[4] = t
        if (around[5] == '?'): # bottom left
            t = getValue(array2d, i+radius, j-radius)
            if t in ['#','L','']: around[5] = t
        if (around[6] == '?'): # bottom
            t = getValue(array2d, i+radius, j)
            if t in ['#','L','']: around[6] = t
        if (around[7] == '?'): # bottom right
            t = getValue(array2d, i+radius, j+radius)
            if t in ['#','L','']: around[7] = t
        # increase search radius
        radius += 1
    return around

def part1():
    lines = readInput()
    modified = True
    cycles = 0
    while modified:
        cycles += 1
        linesNext = deepCopy(lines)
        for i in range(len(linesNext)):
            for j in range(len(linesNext[0])):
                if (lines[i][j] in ['L','#']):
                    t = [getValue(lines,i-1,j-1), getValue(lines,i-1,j), getValue(lines,i-1,j+1),
                         getValue(lines,i  ,j-1),                         getValue(lines,i  ,j+1),
                         getValue(lines,i+1,j-1), getValue(lines,i+1,j), getValue(lines,i+1,j+1)]
                    if (t.count('#') == 0):
                        linesNext[i][j] = '#'
                    elif (t.count('#') >= 4):
                        linesNext[i][j] = 'L'
        #printArray(cycles, lines)
        modified = not compare(lines, linesNext)
        lines = deepCopy(linesNext)
    print('after',cycles,'rounds',countSeats(lines),'seats are in use')

def part2():
    lines = readInput()
    modified = True
    cycles = 0
    while modified:
        cycles += 1
        linesNext = deepCopy(lines)
        for i in range(len(linesNext)):
            for j in range(len(linesNext[0])):
                if (lines[i][j] in ['L','#']):
                    t = occupiedSeatsVisible(lines,i,j)
                    if (t.count('#') == 0):
                        linesNext[i][j] = '#'
                    elif (t.count('#') >= 5 and lines[i][j] in ['L','#']):
                        linesNext[i][j] = 'L'
        #printArray(cycles, lines)
        modified = not compare(lines, linesNext)
        lines = deepCopy(linesNext)
    print('after',cycles,'rounds',countSeats(lines),'seats are in use')

part1()
part2()