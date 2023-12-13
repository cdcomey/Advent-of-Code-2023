def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def find_starting_loc(pipe_map):
    for r, line in enumerate(pipe_map):
        c = line.find('S')
        if c != -1:
            return r, c

    print('error: unable to find starting location')

def find_next_step(loc, r, c, direction):
    if loc == '|':
        if direction == 'up':
            return r-1, c, 'up'
        elif direction == 'down':
            return r+1, c, 'down'
    elif loc == '-':
        if direction == 'left':
            return r, c-1, 'left'
        elif direction == 'right':
            return r, c+1, 'right'
    elif loc == 'F':
        if direction == 'left':
            return r+1, c, 'down'
        elif direction == 'up':
            return r, c+1, 'right'
    elif loc == '7':
        if direction == 'right':
            return r+1, c, 'down'
        elif direction == 'up':
            return r, c-1, 'left'
    elif loc == 'L':
        if direction == 'down':
            return r, c+1, 'right'
        elif direction == 'left':
            return r-1, c, 'up'
    elif loc == 'J':
        if direction == 'down':
            return r, c-1, 'left'
        elif direction == 'right':
            return r-1, c, 'up'
    
    print('error in find_next_step({}, {}, {})'.format(r, c, direction))

def find_next_step_and_enclosing(loc, r, c, direction, inside_list, outside_list):
    if loc == '|':
        if direction == 'up':
            inside_list.append((r, c+1))
            outside_list.append((r, c-1))
            return r-1, c, 'up', inside_list, outside_list
        elif direction == 'down':
            inside_list.append((r, c-1))
            outside_list.append((r, c+1))
            return r+1, c, 'down', inside_list, outside_list
    elif loc == '-':
        if direction == 'left':
            inside_list.append((r-1, c))
            outside_list.append((r+1, c))
            return r, c-1, 'left', inside_list, outside_list
        elif direction == 'right':
            inside_list.append((r+1, c))
            outside_list.append((r-1, c))
            return r, c+1, 'right', inside_list, outside_list
    elif loc == 'F':
        if direction == 'left':
            inside_list.append((r, c-1))
            inside_list.append((r-1, c))
            return r+1, c, 'down', inside_list, outside_list
        elif direction == 'up':
            outside_list.append((r, c-1))
            outside_list.append((r-1, c))
            return r, c+1, 'right', inside_list, outside_list
    elif loc == '7':
        if direction == 'right':
            outside_list.append((r, c+1))
            outside_list.append((r-1, c))
            return r+1, c, 'down', inside_list, outside_list
        elif direction == 'up':
            inside_list.append((r, c+1))
            inside_list.append((r-1, c))
            return r, c-1, 'left', inside_list, outside_list
    elif loc == 'L':
        if direction == 'down':
            inside_list.append((r, c-1))
            inside_list.append((r+1, c))
            return r, c+1, 'right', inside_list, outside_list
        elif direction == 'left':
            outside_list.append((r, c-1))
            outside_list.append((r+1, c))
            return r-1, c, 'up', inside_list, outside_list
    elif loc == 'J':
        if direction == 'down':
            outside_list.append((r, c+1))
            outside_list.append((r+1, c))
            return r, c-1, 'left', inside_list, outside_list
        elif direction == 'right':
            inside_list.append((r, c+1))
            inside_list.append((r+1, c))
            return r-1, c, 'up', inside_list, outside_list
    
    print('error in find_next_step({}, {}, {})'.format(r, c, direction))

def find_starting_dirs(pipe_map, r, c):
    starting_dirs = []
    starting_locs = []
    
    left_pipe = pipe_map[r][c-1]
    right_pipe = pipe_map[r][c+1]
    up_pipe = pipe_map[r-1][c]
    down_pipe = pipe_map[r+1][c]
    if left_pipe == '-' or left_pipe == 'L' or left_pipe == 'F':
        starting_dirs.append('left')
        starting_locs.append(r)
        starting_locs.append(c+1)
    if right_pipe == '-' or right_pipe == 'J' or right_pipe == '7':
        starting_dirs.append('right')
        starting_locs.append(r)
        starting_locs.append(c+1)
    if up_pipe == '|' or up_pipe == '7' or up_pipe == 'F':
        starting_dirs.append('up')
        starting_locs.append(r-1)
        starting_locs.append(c)
    if down_pipe == '|' or down_pipe == 'L' or down_pipe == 'J':
        starting_dirs.append('down')
        starting_locs.append(r+1)
        starting_locs.append(c)
    
    if len(starting_dirs) != 2:
        print('error in find_starting_dirs({}, {}): found {}'.format(r, c, starting_dirs))
    
    return starting_locs, starting_dirs

def navigate_pipes(pipe_map, r, c):
    starting_locs, starting_dirs = find_starting_dirs(pipe_map, r, c)
    print('starting locs are', starting_locs)
    print('starting dirs are', starting_dirs)
    r1, c1, r2, c2 = tuple(starting_locs)
    dir1, dir2 = tuple(starting_dirs)
    steps = 1

    while not (r1 == r2 and c1 == c2):
        print(steps, ':now checking', r1, c1, dir1, 'against', r2, c2, dir2)
        r1, c1, dir1 = find_next_step(pipe_map[r1][c1], r1, c1, dir1)
        r2, c2, dir2 = find_next_step(pipe_map[r2][c2], r2, c2, dir2)
        steps += 1
    
    return steps

def navigate_pipes_with_enclosing(pipe_map, r, c):
    starting_locs, starting_dirs = find_starting_dirs(pipe_map, r, c)
    ri, ci = starting_locs[2], starting_locs[3]
    dir = starting_dirs[1]
    outside_list, inside_list = [], []

    while not (ri == r and ci == c):
        ri, ci, dir, inside_list, outside_list = find_next_step_and_enclosing(pipe_map[ri][ci], ri, ci, dir, inside_list, outside_list)
    
    return inside_list, outside_list

def paint_fill(pipe_map):
    for i in range(1, len(pipe_map)-1):
        for j in range(len(pipe_map[0])):
            if pipe_map[i][j] == 'I':
                pipe_map[i-1] = pipe_map[i-1][:j-1] + pipe_map[i-1][j-1:j+2].replace('.', 'I') + pipe_map[i-1][j+2:]
                pipe_map[i] = pipe_map[i][:j-1] + pipe_map[i][j-1:j+2].replace('.', 'I') + pipe_map[i][j+2:]
                pipe_map[i+1] = pipe_map[i+1][:j-1] + pipe_map[i+1][j-1:j+2].replace('.', 'I') + pipe_map[i+1][j+2:]
    
    return pipe_map


def convert_pipe_map(pipe_map, loop_list, inside_list, outside_list):
    for line in pipe_map:
        line = '.' * len(line)
    for (r, c) in inside_list:
        if (r, c) not in loop_list:
            pipe_map[r] = pipe_map[r][:c] + 'I' + pipe_map[r][c+1:]
    for (r, c) in outside_list:
        if (r, c) not in loop_list:
            if (r, c) in inside_list:
                pipe_map[r] = pipe_map[r][:c] + 'X' + pipe_map[r][c+1:]
            else:
                pipe_map[r] = pipe_map[r][:c] + 'O' + pipe_map[r][c+1:]
    
    
    return pipe_map

def print_loop(pipe_map, r, c):
    starting_locs, starting_dirs = find_starting_dirs(pipe_map, r, c)
    print('starting locs are', starting_locs)
    print('starting dirs are', starting_dirs)
    r1, c1, r2, c2 = tuple(starting_locs)
    dir1, dir2 = tuple(starting_dirs)
    loop_chars = []
    inside_list, outside_list = navigate_pipes_with_enclosing(pipe_map, r, c)
    # inside_list = paint_fill(inside_list, len(pipe_map), len(pipe_map[0]))
    # outside_list = paint_fill(outside_list, len(pipe_map), len(pipe_map[0]))

    while not (r1 == r2 and c1 == c2):
        # print('now checking', r1, c1, dir1, 'against', r2, c2, dir2)
        r1, c1, dir1 = find_next_step(pipe_map[r1][c1], r1, c1, dir1)
        r2, c2, dir2 = find_next_step(pipe_map[r2][c2], r2, c2, dir2)
        loop_chars.append((r1, c1))
        loop_chars.append((r2, c2))
    

    pipe_map = convert_pipe_map(pipe_map, loop_chars, inside_list, outside_list)
    # pipe_map = paint_fill(pipe_map)
    
    for r, row in enumerate(pipe_map):
        for c, char in enumerate(row):
            if (r, c) in loop_chars or pipe_map[r][c] == 'I' or pipe_map[r][c] == 'O':
                print(char, end='')
            else:
                print('.', end='')
        print()


def part1():
    pipe_map = get_data('input.txt').split('\n')
    r, c = find_starting_loc(pipe_map)
    print('found S at', r, c)
    steps = navigate_pipes(pipe_map, r, c)
    print('it took', steps, 'steps')

def part2():
    pipe_map = get_data('input.txt').split('\n')
    r, c = find_starting_loc(pipe_map)
    print('found S at', r, c)
    print_loop(pipe_map, r, c)
    
part2()
# 566 is too high
# correct number is 563
# must investigate why mine is too high