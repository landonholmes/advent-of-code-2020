import itertools

preamble_size = 25


def parse_input():
    temp = []

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines:
        temp.append(int(line))

    return temp


def parse_code(code):
    for idx in range(len(code)-1):
        if idx > preamble_size:

            last_preamble_sized_chunk = code[idx-preamble_size-1:idx-1]
            next_value = code[idx-1]
            is_next_valid = False  # force us to prove the next is valid
            for combo in itertools.combinations(last_preamble_sized_chunk, 2):
                first = combo[0]
                second = combo[1]

                if first + second == next_value:
                    is_next_valid = True

            if not is_next_valid:
                return next_value  # we found our invalid value


full_code = parse_input()
invalid_number = parse_code(full_code)
print('Invalid Number: ', invalid_number) # 32321523

