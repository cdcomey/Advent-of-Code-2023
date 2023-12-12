def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def find_value_pyramid(line):
    init_vals = [int(val) for val in line.split(' ')]
    ret_vals = [init_vals[-1]]
    prev_vals = init_vals
    working_vals = []
    while not all([elem == 0 for elem in prev_vals]):
        i = 0
        while i < len(prev_vals)-1:
            working_vals.append(prev_vals[i+1] - prev_vals[i])
            i += 1
        # print('working =', working_vals)
        ret_vals.append(working_vals[-1])
        prev_vals = working_vals
        working_vals = []
    
    return ret_vals

def test_pyramid():
    data = get_data('input.txt')
    line = data.split('\n')[0]
    print(find_value_pyramid(line))

def predict_next(final_vals):
    next_vals = [0]
    i = len(final_vals)-1
    while i >= 0:
        next_vals.append(next_vals[-1] + final_vals[i])
        i -= 1
    
    return next_vals[-1]

def part1():
    data = get_data('input.txt')
    sum = 0
    for line in data.split('\n'):
        if line == '':
            continue
        final_vals = find_value_pyramid(line)
        # print('final vals', final_vals)
        next_val = predict_next(final_vals)
        # print(next_val)
        sum += next_val
    
    print(sum)


part1()