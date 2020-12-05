highest_seat_id = 0
plane_size = (128, 8)


def calculate_seat_info(boarding_pass):
    current_seat = {
        'raw': boarding_pass,
        'row': 0,
        'column': 0,
        'seat_id': ''
    }

    vertical_info = boarding_pass[0:7]
    current_seat['row'] = traverse_plane_vertically(vertical_info)

    horizontal_info = boarding_pass[7:10]
    current_seat['column'] = traverse_plane_horizontally(horizontal_info)

    current_seat['seat_id'] = current_seat['row'] * 8 + current_seat['column']

    return current_seat


def traverse_plane_vertically(vertical_info):
    return traverse_generic(plane_size[0], list(vertical_info), 'F', 'B')


def traverse_plane_horizontally(horizontal_info):
    return traverse_generic(plane_size[1], list(horizontal_info), 'L', 'R')


# basically the binary space partitioning stuff
def traverse_generic(size, info_list, lower_half_indicator, upper_half_indicator):
    seats_range = range(size)
    while len(info_list) > 0:
        indicator = info_list.pop(0)
        if indicator == lower_half_indicator:
            seats_range = seats_range[:len(seats_range)//2]
        elif indicator == upper_half_indicator:  # this could probably be else, but I'm weird
            seats_range = seats_range[len(seats_range)//2:]
    return list(seats_range)[0]


# ------------------- THE ACTUAL PROGRAM -------------------

with open('input.txt') as f:
    lines = [l.rstrip('\n') for l in f]

for line in lines:
    seat = calculate_seat_info(line)
    highest_seat_id = seat['seat_id'] if seat['seat_id'] > highest_seat_id else highest_seat_id

print('Highest Seat ID:', highest_seat_id)  # 974
