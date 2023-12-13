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

def part1():
    pipe_map = get_data('input.txt').split('\n')
    r, c = find_starting_loc(pipe_map)
    print('found S at', r, c)
    steps = navigate_pipes(pipe_map, r, c)
    print('it took', steps, 'steps')
    
part1()