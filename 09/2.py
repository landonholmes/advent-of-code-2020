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


def find_weakness(code, invalid_num):

    for idx in range(len(code)-1):
        current_idx = idx
        current_sum = code[current_idx]
        contiguous_set = [current_sum]  # start with current value

        while current_sum < invalid_num:
            current_idx += 1
            current_sum += code[current_idx]
            contiguous_set.append(code[current_idx])  # add new number to set

            if current_sum < invalid_num:
                pass  # do nothing, continue loop
            elif current_sum == invalid_num:
                contiguous_set.sort()
                return contiguous_set[0] + contiguous_set[len(contiguous_set)-1]
            else:
                break  # we passed our number, need to start building contiguous set from next index


full_code = parse_input()
invalid_number = parse_code(full_code)
encryption_weakness = find_weakness(full_code, invalid_number)
print('Encryption Weakness: ', encryption_weakness) # 4794981

