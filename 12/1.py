instructions = []
ship = {
    'position': [0, 0],
    'degrees': 90
}
facing_directions = {
    90: 'E',
    180: 'S',
    270: 'W',
    360: 'N'
}
allowed_degrees_to_move_by = 90


def move_ship(direction, by_amount):
    if direction == 'N':
        ship['position'] = add_coords(ship['position'], [0, by_amount])
    elif direction == 'S':
        ship['position'] = add_coords(ship['position'], [0, -by_amount])
    elif direction == 'E':
        ship['position'] = add_coords(ship['position'], [by_amount, 0])
    elif direction == 'W':
        ship['position'] = add_coords(ship['position'], [-by_amount, 0])
    elif direction == 'F':
        move_ship(facing_directions[ship['degrees']], by_amount)


def add_coords(coord_1, coord_2):
    return [sum(i) for i in zip(coord_1, coord_2)]


def rotate_ship(by_degrees):
    # this line is just to make sure we're moving by a round number we expect takes 95 -> 90 or 160 -> 180
    by_degrees = int(round(by_degrees/allowed_degrees_to_move_by))*allowed_degrees_to_move_by

    current_degrees = ship['degrees']
    new_degrees = current_degrees + by_degrees

    while new_degrees > 360:
        new_degrees -= 360
    while new_degrees <= 0:
        new_degrees += 360

    ship['degrees'] = new_degrees


def parse_input():
    globals()['instructions'] = []

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    for line in lines:
        instructions.append(line)


def run():
    for instr in instructions:
        action = instr[:1]
        value = int(instr[1:])
        if action in ['N', 'S', 'E', 'W', 'F']:
            move_ship(action, value)
        elif action == 'L':
            rotate_ship(-value)
        elif action == 'R':
            rotate_ship(value)


def calc_manhattan_distance():
    return abs(ship['position'][0]) + abs(ship['position'][1])


parse_input()
run()
print('Answer', calc_manhattan_distance())  # 1565


