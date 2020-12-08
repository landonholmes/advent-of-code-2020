def parse_instructions():
    instrs = []  # going to be list of dicts

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines:
        instr_split = line.split(' ')
        instr = {
            'instruction': instr_split[0],
            'value': int(instr_split[1]),
        }
        instrs.append(instr)

    return instrs


def invert_instruction(instr):
    if instr == 'jmp':
        return 'nop'
    else:
        return 'jmp'


def run_instructions(instrs):
    idx = 0
    acc = 0
    visited_indexes = set()

    while idx <= len(instrs)-1:
        if idx in visited_indexes:
            return acc

        visited_indexes.add(idx)
        instr = instrs[idx]['instruction']
        value = instrs[idx]['value']

        if instr == 'acc':
            acc += value
        elif instr == 'jmp':
            idx += value
            continue
        elif instr == 'nop':
            pass

        idx += 1


instructions = parse_instructions()
accumulator = run_instructions(instructions)
print('Accumulator: ', accumulator)
