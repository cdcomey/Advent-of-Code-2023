from math import lcm

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def parse_into_dict(data):
    dictionary = {}
    # print(len(data))
    for line in data:
        if line == '':
            continue
        key = line[:3]
        values = line[line.find('(')+1:-1]
        print(values)
        left, right = values.split(', ')
        dictionary.update({key: (left, right)})
    
    return dictionary

def part1():
    data = get_data('input.txt')
    lines = data.split('\n')
    directions_backup = [char for char in lines[0]]
    directions = directions_backup.copy()
    locations = parse_into_dict(lines[2:])

    steps = 0
    current_location = 'AAA'
    while current_location != 'ZZZ':
        if directions[0] == 'L':
            current_location = locations.get(current_location)[0]
        elif directions[0] == 'R':
            current_location = locations.get(current_location)[1]
        steps += 1
        directions = directions[1:]

        if len(directions) == 0:
            directions = directions_backup.copy()
            print('beginning new cycle')
    
    print('used', steps, 'total steps')

# brute force algorithm
# lcm method below only works because the problem has been
# specially designed for it to work
# def part2():
#     data = get_data('input.txt')
#     lines = data.split('\n')
#     directions_backup = [char for char in lines[0]]
#     directions = directions_backup.copy()
#     locations = parse_into_dict(lines[2:])

#     steps = 0
#     current_locations = [location for location in locations.keys() if location[-1] == 'A']
#     ending_locations = [location for location in locations.keys() if location[-1] == 'Z']
#     ending_locations.sort()

#     while sorted(current_locations) != ending_locations:
#         if directions[0] == 'L':
#             current_locations = [locations.get(loc)[0] for loc in current_locations]
#         else:
#             current_locations = [locations.get(loc)[1] for loc in current_locations]

#         steps += 1
#         directions = directions[1:]

#         if len(directions) == 0:
#             directions = directions_backup.copy()
#             print('beginning new cycle: have been through', steps, 'steps:',\
#                   current_locations, 'vs', ending_locations)
    
#     print('used', steps, 'total steps')

def part2():
    data = get_data('input.txt')
    lines = data.split('\n')
    directions_backup = [char for char in lines[0]]
    directions = directions_backup.copy()
    locations = parse_into_dict(lines[2:])

    current_locations = [location for location in locations.keys() if location[-1] == 'A']
    ending_locations = [location for location in locations.keys() if location[-1] == 'Z']
    step_counters = []

    for current_loc in current_locations:
        print('starting at', current_loc)
        steps = 0
        while current_loc not in ending_locations:
            if directions[0] == 'L':
                current_loc = locations.get(current_loc)[0]
            elif directions[0] == 'R':
                current_loc = locations.get(current_loc)[1]
            steps += 1
            directions = directions[1:]

            if len(directions) == 0:
                directions = directions_backup.copy()
        
        print('used', steps, 'total steps to get to', current_loc)
        step_counters.append(steps)
    
    print('total number of steps should be', lcm(step_counters[0], step_counters[1], step_counters[2], step_counters[3], step_counters[4], step_counters[5]))


part2()