from functools import reduce


schedule = []


def parse_input():
    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines[1].split(','):
        if line == 'x':
            line = 0
        schedule.append(int(line))


# wow this was neat: https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfray8m
# uses Chinese Remainder Theorem
def find_timestamp():
    indices = [i for i, bus in enumerate(schedule) if bus]
    diff = indices[-1] - indices[0]
    prod = reduce(lambda a, b: a * b, filter(None, schedule))
    return sum((diff - i) * pow(prod // n, n - 2, n) * prod // n
               for i, n in enumerate(schedule) if n) % prod - diff


parse_input()
answer = find_timestamp()
print('The answer is ', answer)  # 807435693182510
