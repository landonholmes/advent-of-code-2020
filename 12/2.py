instructions = []
ship = {
    'position': [0, 0],
    'waypoint': [10, 1],  # always relative to ship's position
    'degrees': 90
}
facing_directions = {
    90: 'E',
    180: 'S',
    270: 'W',
    360: 'N'
}
allowed_degrees_to_move_by = 90


def move_waypoint(direction, by_amount):
    if direction == 'N':
        ship['waypoint'] = add_coords(ship['waypoint'], [0, by_amount])
    elif direction == 'S':
        ship['waypoint'] = add_coords(ship['waypoint'], [0, -by_amount])
    elif direction == 'E':
        ship['waypoint'] = add_coords(ship['waypoint'], [by_amount, 0])
    elif direction == 'W':
        ship['waypoint'] = add_coords(ship['waypoint'], [-by_amount, 0])


def move_ship(by_amount):
    original_waypoint = ship['waypoint']
    for i in range(by_amount):
        ship['position'] = add_coords(ship['position'], original_waypoint)


def add_coords(coord_1, coord_2):
    return [sum(i) for i in zip(coord_1, coord_2)]


# I'm not proud of this one, it did not evolve well for part 2 but I don't feel like re-working everything
def rotate_waypoint(by_degrees):
    # this line is just to make sure we're moving by a round number we expect takes 95 -> 90 or 160 -> 180
    by_degrees = int(round(by_degrees/allowed_degrees_to_move_by))*allowed_degrees_to_move_by

    current_degrees = ship['degrees']
    current_direction = facing_directions[current_degrees]
    new_degrees = current_degrees + by_degrees

    while new_degrees > 360:
        new_degrees -= 360
    while new_degrees <= 0:
        new_degrees += 360

    ship['degrees'] = new_degrees
    new_direction = facing_directions[ship['degrees']]

    if (current_direction == 'E' and new_direction == 'S') or (current_direction == 'S' and new_direction == 'W') or (current_direction == 'W' and new_direction == 'N') or (current_direction == 'N' and new_direction == 'E'):
        ship['waypoint'] = [ship['waypoint'][1], -ship['waypoint'][0]]
    elif (current_direction == 'E' and new_direction == 'W') or (current_direction == 'S' and new_direction == 'N') or (current_direction == 'W' and new_direction == 'E') or (current_direction == 'N' and new_direction == 'S'):
        ship['waypoint'] = [-ship['waypoint'][0], -ship['waypoint'][1]]
    elif (current_direction == 'E' and new_direction == 'N') or (current_direction == 'S' and new_direction == 'E') or (current_direction == 'W' and new_direction == 'S') or (current_direction == 'N' and new_direction == 'W'):
        ship['waypoint'] = [-ship['waypoint'][1], ship['waypoint'][0]]


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
        if action in ['N', 'S', 'E', 'W']:
            move_waypoint(action, value)
        elif action == 'L':
            rotate_waypoint(-value)
        elif action == 'R':
            rotate_waypoint(value)
        elif action == 'F':
            move_ship(value)


def calc_manhattan_distance():
    return abs(ship['position'][0]) + abs(ship['position'][1])


parse_input()
run()
print('Answer', calc_manhattan_distance())  # 78883


