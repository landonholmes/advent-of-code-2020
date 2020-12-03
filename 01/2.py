import itertools

reportNumbers = []
solution = 0

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    for line in lines:
        reportNumbers.append(int(line))

for combo in itertools.combinations(reportNumbers, 3):
    first = combo[0]
    second = combo[1]
    third = combo[2]

    if first + second + third == 2020:
        solution = first * second * third
        break

print(solution) # 259521570
