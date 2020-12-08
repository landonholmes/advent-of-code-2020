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


# returns True/False based on if instructions exited correctly or ran into duplicate instr
def run_instructions(instrs, replace_index):
    idx = 0
    acc = 0
    visited_indexes = set()

    while idx <= len(instrs)-1:
        if idx in visited_indexes:
            return acc, False

        visited_indexes.add(idx)
        instr = instrs[idx]['instruction']
        value = instrs[idx]['value']

        if replace_index != -1 and replace_index == idx:  # see if next instruction will end program
            instr = invert_instruction(instr)  # swap jmp <--> nop

        if instr == 'acc':
            acc += value
        elif instr == 'jmp':
            idx += value
            continue
        elif instr == 'nop':
            pass

        idx += 1

    return acc, True


# will run all instructions and try to see if replacing any jmp <--> nop operations successfully completes them
def fix_corrupt(instrs):
    for idx in range(len(instrs)):
        if instrs[idx]['instruction'] != 'acc':
            acc, is_fixed = run_instructions(instrs, idx)
            if is_fixed:
                return acc
    return -1


instructions = parse_instructions()
accumulator = fix_corrupt(instructions)
print('Accumulator: ', accumulator)
