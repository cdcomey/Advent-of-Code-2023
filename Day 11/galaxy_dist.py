import numpy as np

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def find_empty_lines(galaxy_map):
    empty_rows, empty_cols = [], []
    m, n = galaxy_map.shape
    n_dots = np.array(list('.' * n))
    m_dots = np.array(list('.' * m))

    for i in range(m):
        if np.array_equal(galaxy_map[i, :], n_dots):
            empty_rows.append(i)
    
    for i in range(n):
        if np.array_equal(galaxy_map[:, i], m_dots):
            empty_cols.append(i)
    
    return empty_rows, empty_cols


def expand_map(galaxy_map, empty_rows, empty_cols):
    expanded_map = galaxy_map.copy()
    m, n = expanded_map.shape
    n_dots = np.array(list('.' * n))
    
    for i, row_index in enumerate(empty_rows):
        expanded_map = np.insert(expanded_map, i+row_index, n_dots, axis=0)
    
    m, n = expanded_map.shape
    m_dots = np.array(list('.' * m))
    for i, col_index in enumerate(empty_cols):
        expanded_map = np.insert(expanded_map, i+col_index, m_dots, axis=1)
    
    return expanded_map

def expand_map_pt2(galaxy_coords, empty_rows, empty_cols):
    expanded_coords = []
    constant = (10 ** 6) - 1
    for (r, c) in galaxy_coords:
        r_new, c_new = r, c
        for k in empty_rows:
            if r > k:
                # print('r > k')
                r_new += constant
        for k in empty_cols:
            if c > k:
                # print('c > k')
                c_new += constant
        
        expanded_coords.append((r_new, c_new))
    
    return expanded_coords

def find_galaxies(galaxy_map):
    m, n = galaxy_map.shape
    galaxy_coords = []
    for r in range(m):
        for c in range(n):
            if galaxy_map[r, c] == '#':
                galaxy_coords.append((r, c))
    
    return galaxy_coords

def find_shortest_distance(galaxy_coords):
    sum = 0
    for i, (r1, c1) in enumerate(galaxy_coords[:-1]):
        for j, (r2, c2) in enumerate(galaxy_coords[i+1:]):
            sum += abs(r2-r1) + abs(c2-c1)
        
        # print('galaxy', i, (r1, c1))
    
    return sum


def part1():
    data = get_data('input.txt')
    lines = data.split('\n')
    chars = [list(line) for line in lines]
    galaxy_map = np.array(chars)

    empty_rows, empty_cols = find_empty_lines(galaxy_map)
    galaxy_map = expand_map(galaxy_map, empty_rows, empty_cols)
    # print(galaxy_map.shape)
    galaxy_coords = find_galaxies(galaxy_map)
    # print(galaxy_coords)
    print(find_shortest_distance(galaxy_coords))

def part2():
    data = get_data('input.txt')
    lines = data.split('\n')
    chars = [list(line) for line in lines]
    galaxy_map = np.array(chars)
    galaxy_coords = find_galaxies(galaxy_map)
    empty_rows, empty_cols = find_empty_lines(galaxy_map)
    galaxy_coords = expand_map_pt2(galaxy_coords, empty_rows, empty_cols)
    # print(galaxy_coords)
    print(find_shortest_distance(galaxy_coords))

part2()
# 86375060578 is too low
# 86375146944 is too low
# 458191688761