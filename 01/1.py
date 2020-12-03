import itertools

reportNumbers = []
solution = 0

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]
    for line in lines:
        reportNumbers.append(int(line))

for combo in itertools.combinations(reportNumbers, 2):
    first = combo[0]
    second = combo[1]

    if first + second == 2020:
        solution = first * second
        break

print(solution) # 987339
