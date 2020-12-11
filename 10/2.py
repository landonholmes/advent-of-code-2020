

def parse_input():
    temp = []

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines:
        temp.append(int(line))

    return temp


def compute_difference_jumps(adpts):
    dif = []
    current_jolts = 0

    adpts.sort()
    for adpt in adpts:
        dif.append(adpt-current_jolts)
        current_jolts = adpt

    dif.append(3)  # make sure to add our adapter onto it
    return dif


# from https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfdy1yx
# creating a list for every sequence of 1's between 3's,
# then finding all possible combinations in the list and multiplying all of them.
# I still don't know about this one and I've picked it apart a bit
def compute_adapter_combinations(diff_jumps):
    temp_list = []
    number_of_possible_combinations = []

    for jump in diff_jumps:
        if jump != 3:
            temp_list.append(jump)
        elif jump == 3:
            number_of_one_jumps = (len(temp_list)-1)*2
            if len(temp_list) > 3:
                what_is_this_pls = (len(temp_list)-3)  # it's always 1, idk
                number_of_possible_combinations.append(number_of_one_jumps + what_is_this_pls)
            elif len(temp_list) > 1:
                number_of_possible_combinations.append(number_of_one_jumps)
            temp_list = []

    total_combinations_multiplied = 1
    for combination in number_of_possible_combinations:
        total_combinations_multiplied *= combination

    return total_combinations_multiplied


adapters = parse_input()
difference_jumps = compute_difference_jumps(adapters)
possible_configurations = compute_adapter_combinations(difference_jumps)
print('Number of Possible Configurations: ', possible_configurations)  # 5289227976704

