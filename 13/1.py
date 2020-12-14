import math

earliest_departure_time = 0
schedule = []

def parse_input():
    globals()['schedule'] = []

    with open('input.txt') as f:
        lines = [l.rstrip('\n') for l in f]

    globals()['earliest_departure_time'] = int(lines[0])
    for line in lines[1].split(','):
        schedule.append(line)


def calculate_next_available_bus():
    bus_dict = {
        'id': 0,
        'minutes_until_arrival': 0,
        'time_required_to_wait': 999999
    }

    for bus in schedule:
        if bus == 'x':
            continue

        bus_id = int(bus)
        arrival_time = math.ceil(earliest_departure_time / bus_id) * bus_id
        wait_time = arrival_time - earliest_departure_time

        if 0 <= wait_time < bus_dict['time_required_to_wait']:
            bus_dict['id'] = bus_id
            bus_dict['minutes_until_arrival'] = arrival_time
            bus_dict['time_required_to_wait'] = wait_time

    return bus_dict


parse_input()
next_bus = calculate_next_available_bus()
print('Answer', next_bus['time_required_to_wait'] * next_bus['id'])  # 261


