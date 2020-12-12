adjacent_tile_list = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
x_max = 0  # computed during input parsing
y_max = 0  # computed during input parsing
adjacent_count_to_leave = 4


def get_seat(x=0, y=0, new_state='', current_state='', old_state=''):
    return {
        'x': x,
        'y': y,
        'new_state': new_state,
        'current_state': current_state,
        'old_state': old_state,
    }


def parse_input():
    grid = {}

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    globals()['x_max'] = len(lines)
    for x_coord in range(globals()['x_max']):
        grid[x_coord] = {}
        current_line = list(lines[x_coord])
        globals()['y_max'] = len(current_line)
        for y_coord in range(globals()['y_max']):
            seat = get_seat(x_coord, y_coord, current_line[y_coord], current_line[y_coord], current_line[y_coord])
            grid[x_coord][y_coord] = seat

    return grid


def compute_seat_state(grid, seat):
    if seat['current_state'] == '.':  # if this "seat" is the floor, we don't need to process anything
        return seat

    seat['old_state'] = seat['current_state']
    seat['current_state'] = seat['new_state']
    adjacent_count = 0
    for adjacent_coord in adjacent_tile_list:
        x_adjacent = seat['x'] + adjacent_coord[0]
        if x_adjacent < 0 or x_adjacent >= globals()['x_max']:
            continue

        y_adjacent = seat['y'] + adjacent_coord[1]
        if y_adjacent < 0 or y_adjacent >= globals()['y_max']:
            continue

        adjacent_seat = grid[x_adjacent][y_adjacent]
        if adjacent_seat['current_state'] == '#':
            adjacent_count += 1

    if adjacent_count >= globals()['adjacent_count_to_leave']:
        seat['new_state'] = 'L'
    elif adjacent_count == 0:
        seat['new_state'] = '#'
    else:
        seat['new_state'] = seat['current_state']
    return seat


def run(grid):
    seats_changed = True
    while seats_changed:  # returns True if seats changed during round
        seats_changed = run_round(grid)

    seats_occupied = 0
    for x_coord in range(globals()['x_max']):
        for y_coord in range(globals()['y_max']):
            if grid[x_coord][y_coord]['new_state'] == '#':
                seats_occupied += 1

    return seats_occupied


def run_round(grid):
    did_any_seats_change = False
    for x_coord in range(globals()['x_max']):
        for y_coord in range(globals()['y_max']):
            grid[x_coord][y_coord] = compute_seat_state(grid, grid[x_coord][y_coord])
            if not did_any_seats_change and grid[x_coord][y_coord]['new_state'] != grid[x_coord][y_coord]['current_state']:
                did_any_seats_change = True

    # print_grid(grid)
    return did_any_seats_change


# for debugging or fun
def print_grid(grid):
    string = '\n'
    for x_coord in range(globals()['x_max']):
        for y_coord in range(globals()['y_max']):
            string += grid[x_coord][y_coord]['current_state']
        string += '\n'

    print(string)


seat_grid = parse_input()
occupied_seats = run(seat_grid)
print('Occupied seats: ', occupied_seats)  # 2801 is wrong, supposed to be 2489


