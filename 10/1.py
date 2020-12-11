from collections import defaultdict


def parse_input():
    temp = []

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines:
        temp.append(int(line))

    return temp


def connect_adapters(adpts):
    current_jolts = 0
    connections_made_by_jump = defaultdict(int)

    adpts.sort()
    adpts.append(adpts[len(adpts)-1] + 3)  # add our own adapter that is always a jump of 3
    for adpt in adpts:
        jump = adpt - current_jolts
        current_jolts = adpt
        connections_made_by_jump[jump] += 1

    return connections_made_by_jump


adapters = parse_input()
differences = connect_adapters(adapters)
print('Differences: ', differences[1] * differences[3])  # 1690

