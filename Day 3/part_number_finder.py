def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def find_next_number(line):
    for i, char in enumerate(line):
        if char.isdigit():
            return i
    return -1

def isolate_number(start_loc, line):
    loc = start_loc+1
    while loc < len(line):
        if line[loc].isdigit():
            loc += 1
        else:
            break

    return int(line[start_loc:loc]), loc-1

def not_period_or_digit(char):
    return not(char.isdigit() or char == '.')

def determine_adjacency(prev_line, line, next_line, start_loc, end_loc):
    left_extreme = max(0, start_loc-1)
    right_extreme = min(end_loc+1, len(line)-1)
    suspects = prev_line[left_extreme:right_extreme+1] + next_line[left_extreme:right_extreme+1]
    suspects += line[left_extreme] + line[right_extreme]

    is_adjacent = any(not_period_or_digit(char) for char in suspects)

    return any(not_period_or_digit(char) for char in suspects)

def part1():
    data = get_data('input.txt')
    lines = data.split('\n')
    counter = 0
    part_numbers = []
    while counter < len(lines):
        line = lines[counter]
        if len(line) == 0:
            counter += 1
            continue

        start_loc = 0
        prev_end = -1

        while True:
            start_loc = find_next_number(line[start_loc:])
            if start_loc == -1:
                break
            start_loc += prev_end+1
            num, end_loc = isolate_number(start_loc, line)
            is_part_number = False
            if counter == 0:
                is_part_number = determine_adjacency('.'*len(line), line, lines[counter+1], start_loc, end_loc)
            elif counter == len(lines)-1:
                is_part_number = determine_adjacency(lines[counter-1], line, '.'*len(line), start_loc, end_loc)
            else:
                is_part_number = determine_adjacency(lines[counter-1], line, lines[counter+1], start_loc, end_loc)
        
            if is_part_number:
                part_numbers.append(num)

            prev_end = end_loc
            start_loc = end_loc+1

        counter += 1
    
    sum = 0
    for part_number in part_numbers:
        sum += part_number
    
    print('The total is', sum)

part1()