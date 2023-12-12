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

part1()