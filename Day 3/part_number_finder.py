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

def find_next_special_char(line):
    for i, char in enumerate(line):
        if not_period_or_digit(char):
            return i
    return -1

# assumes starting from beginning
def isolate_number_pt1(start_loc, line):
    loc = start_loc+1
    while loc < len(line):
        if line[loc].isdigit():
            loc += 1
        else:
            break

    return int(line[start_loc:loc]), loc-1

# could be starting from beginning, middle, or end
# assumes 3-digit num
def isolate_number_pt2(loc, line):
    start_loc, end_loc = loc-1, loc+1
    while start_loc >= 0:
        if line[start_loc].isdigit():
            start_loc -= 1
        else:
            start_loc += 1
            break
    
    start_loc = max(start_loc, 0)
    
    while end_loc < len(line):
        if line[end_loc].isdigit():
            end_loc += 1
        else:
            end_loc -= 1
            break
    
    end_loc = min(end_loc, len(line)-1)

    return int(line[start_loc:end_loc+1])

def not_period_or_digit(char):
    return not(char.isdigit() or char == '.')

def determine_gear_ratio(prev_line, line, next_line, loc):
    suspects = ['.' for n in range(9)]
    if loc > 0:
        suspects[0] = (prev_line[loc-1])
        suspects[3] = (line[loc-1])
        suspects[6] = (next_line[loc-1])

    suspects[1] = (prev_line[loc])
    suspects[7] = (next_line[loc])

    if loc < len(line)-1:
        suspects[2] = (prev_line[loc+1])
        suspects[5] = (line[loc+1])
        suspects[8] = (next_line[loc+1])
    
    if suspects[1].isdigit() and suspects[2].isdigit():
        suspects[2] = '.'
    if suspects[0].isdigit() and suspects[1].isdigit():
        suspects[1] = '.'
    if suspects[7].isdigit() and suspects[8].isdigit():
        suspects[8] = '.'
    if suspects[6].isdigit() and suspects[7].isdigit():
        suspects[7] = '.'
    
    adjacent_nums = []

    for i, suspect in enumerate(suspects):
        if suspect.isdigit():
            if i < 3:
                adjacent_nums.append(isolate_number_pt2(loc+i-1, prev_line))
            elif i == 3 or i == 5:
                adjacent_nums.append(isolate_number_pt2(loc+i-4, line))
            else:
                adjacent_nums.append(isolate_number_pt2(loc+i-7, next_line))
    
    if len(adjacent_nums) == 2:
        return adjacent_nums[0] * adjacent_nums[1]
    else:
        return 0


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
            num, end_loc = isolate_number_pt1(start_loc, line)
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

def part2():
    data = get_data('input.txt')
    lines = data.split('\n')
    counter = 0
    gear_sum = 0
    while counter < len(lines):
        line = lines[counter]
        if len(line) == 0:
            counter += 1
            continue

        end_loc = -1
        loc = find_next_special_char(line)
        while loc >= 0:
            loc += end_loc + 1
            if line[loc] != '*':
                end_loc = loc
                loc = find_next_special_char(line[loc+1:])
                continue
            if counter == 0:
                gear_ratio = determine_gear_ratio('.'*len(line), line, lines[counter+1], loc)
            elif counter == len(lines)-1:
                gear_ratio = determine_gear_ratio(lines[counter-1], line, '.'*len(line), loc)
            else:
                gear_ratio = determine_gear_ratio(lines[counter-1], line, lines[counter+1], loc)
            
            gear_sum += gear_ratio
            end_loc = loc
            loc = find_next_special_char(line[loc+1:])
        
        counter += 1
    
    print('The sum of gear ratios is', gear_sum)


part2()