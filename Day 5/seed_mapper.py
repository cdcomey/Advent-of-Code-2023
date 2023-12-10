class SeedMap:
    # contains three arrays: the dest start, source start, and range
    def __init__(self, data):
        self.dest, self.source, self.map_range = [], [], []
        for line in data.split('\n')[1:]:
            elems = line.split(' ')
            self.dest.append(int(elems[0]))
            self.source.append(int(elems[1]))
            self.map_range.append(int(elems[2]))
    
    # searches through every element in the arrays
    # if the num is within the source range, return its
    # correct mapping to the dest range
    # if it is not in any range, it is to be left unchanged
    def mapping(self, num, verbose=False):
        for dest, source, map_range in zip(self.dest, self.source, self.map_range):
            if num >= source and num <= source + map_range:
                offset = num - source
                if verbose:
                    print(f'mapping from source {source:,}-{source+map_range:,} to {dest:,}-{dest+map_range:,}')
                return dest + offset
        
        return num
    
    def mappping_reverse(self, num, verbose=False):
        for dest, source, map_range in zip(self.dest, self.source, self.map_range):
            if num >= dest and num <= dest + map_range:
                offset = num - dest
                if verbose:
                    print(f'mapping from dest {dest:,}-{dest+map_range:,} to {source:,}-{source+map_range:,}')
                return source + offset
        
        return num


def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# take in the whole text file starting from the first map description
# split them up, pass each of them into the map constructor
# which does most of the heavy lifting, and return an array of those
def create_maps(data):
    data = data.split('\n\n')
    maps = []
    for map_info in data:
        maps.append(SeedMap(map_info))
    
    return maps

def part1():
    # begin parsing our input data
    data = get_data('input.txt')
    seeds = data[data.find('seeds: ')+7:data.find('\n')]
    seeds = [int(seed) for seed in seeds.split(' ')]
    maps = create_maps(data[data.find('seed-to-soil'):])

    lowest_loc = maps[-1].dest[0]
    for seed in seeds:
        print(seed, end='')
        for map in maps:
            seed = map.mapping(seed)
            print(' ->\t', seed, end='')
        print()
        
        lowest_loc = min(lowest_loc, seed)
    
    print(f'The lowest location is {lowest_loc:,}')

def part2():
    data = get_data('input.txt')
    maps = create_maps(data[data.find('seed-to-soil'):])

    seed_ranges = data[data.find('seeds: ')+7:data.find('\n')]
    seed_ranges = [int(seed) for seed in seed_ranges.split(' ')]
    seeds = []
    i = 0
    while i < len(seed_ranges):
        seeds.append((seed_ranges[i], seed_ranges[i+1]))
        i += 2
    
    loc_map = maps[-1]
    lowest_loc_start = loc_map.dest[0]
    lowest_loc_end = loc_map.map_range[0]
    for dest, map_range in zip(loc_map.dest, loc_map.map_range):
        if dest < lowest_loc_start:
            lowest_loc_start = dest
            lowest_loc_end = dest+map_range
    
    print(f'lowest is {lowest_loc_start:,} to {lowest_loc_end:,}')

    found_val = False
    val = 0
    for i in range(lowest_loc_start, lowest_loc_end+1):
        if i % 100000 == 0:
            print(f'{i:,}')
        val = i
        for map in reversed(maps):
            val = map.mappping_reverse(val)
        
        for seed_range in seeds:
            if val >= seed_range[0] and val <= seed_range[0] + seed_range[1]:
                print(f'lowest loc is {i:,}, corresponding to seed {val:,} in range {seed_range[0]:,}-{seed_range[0]+seed_range[1]:,}')
                found_val = True
                break
        
        if found_val:
            break
    
    print(val, end='')
    for map in maps:
        val = map.mapping(val)
        print(' ->\t', val, end='')
    print()
    print(f'location is {val-1:,}')

# incomplete recursion attempt
# def get_loc(seed, maps):
#     loc = seed
#     for map in maps:
#         loc = map.mapping(loc)
    
#     return loc

# def map_rec(start, end, maps):
#     if end < start:
#         # print('returning with -1')
#         return -1
#     if end == start+1:
#         return min(get_loc(start, maps), get_loc(end, maps))
    
#     half_dist = (end-start) // 2
#     mapped_start = get_loc(start, maps)
#     mapped_middle = get_loc(start+half_dist, maps)
#     mapped_end = get_loc(end, maps)

#     if mapped_start + half_dist != mapped_middle:
#         # print(start, end, start+half_dist)
#         return map_rec(start, start+half_dist, maps)
    
#     if mapped_middle + half_dist != mapped_end:
#         return map_rec(start+half_dist, end, maps)
    
#     return mapped_start


# def part2():
#     data = get_data('input.txt')
#     maps = create_maps(data[data.find('seed-to-soil'):])

#     seed_ranges = data[data.find('seeds: ')+7:data.find('\n')]
#     seed_ranges = [int(seed) for seed in seed_ranges.split(' ')]
#     seeds = []
#     i = 0
#     while i < len(seed_ranges):
#         seeds.append((seed_ranges[i], seed_ranges[i] + seed_ranges[i+1]))
#         i += 2
    
#     min_loc = 10 ** 12
#     for seed_range in seeds:
#         start = seed_range[0]
#         end = seed_range[1]
#         min_loc = min(min_loc, map_rec(start, end, maps))
#         print('new min_loc =', min_loc)
    
#     print(f'{min_loc:,}')
        
    
part2()