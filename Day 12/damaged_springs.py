def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def parse_data(data):
    springs, contig_vals = [], []
    for line in data.split('\n'):
        spring_line, contig_line = line.split(' ')
        springs.append(spring_line)
        contig_vals.append([int(i) for i in contig_line.split(',')])
    
    return springs, contig_vals

# make sure spring_list is a list
def spring_permutations(spring_list, permutations):
    if len(spring_list) == 0:
        return permutations
    if len(permutations) == 0:
        if spring_list[0] == '.' or spring_list[0] == '#':
            permutations = [spring_list[0]]
            return spring_permutations(spring_list[1:], permutations)
        if spring_list[0] == '?':
            permutations = ['.', '#']
            return spring_permutations(spring_list[1:], permutations)
    if spring_list[0] == '.' or spring_list[0] == '#':
        # print('\tcond1')
        permutations = [i + spring_list[0] for i in permutations]
        return spring_permutations(spring_list[1:], permutations)
    if spring_list[0] == '?':
        # print('\tcond2')
        permutations_tmp = permutations
        permutations = [i + '.' for i in permutations] + [i + '#' for i in permutations_tmp]
        return spring_permutations(spring_list[1:], permutations)

def assess_possibilities(permutations, contig_vals_list):
    possibilities = 0
    for permutation in permutations:
        contig_springs_list = [i for i in permutation.split('.') if i != '']
        # print(len(contig_springs_list), len(contig_vals_list))
        if len(contig_springs_list) != len(contig_vals_list):
            continue

        is_possible = True
        for i in range(len(contig_vals_list)):
            if len(contig_springs_list[i]) != contig_vals_list[i]:
                is_possible = False
        
        if is_possible:
            possibilities += 1
    
    return possibilities

def part1():
    data = get_data('input.txt')
    lines, contig_vals_list = parse_data(data)
    possibilities = 0
    for line, contig_vals in zip(lines, contig_vals_list):
        permutations = spring_permutations(line, [])
    # print(permutations)
        p = assess_possibilities(permutations, contig_vals)
        # print(p)
        possibilities += p
    
    print(possibilities)

part1()