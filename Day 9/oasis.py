def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# will find final vals if bool is true
# will find first vals if bool is false
def find_pyramid(line, final_vals=True):
    init_vals = [int(val) for val in line.split(' ')]

    if final_vals:
        ret_vals = [init_vals[-1]]
    else:
        ret_vals = [init_vals[0]]
    prev_vals = init_vals
    working_vals = []
    while not all([elem == 0 for elem in prev_vals]):
        i = 0
        while i < len(prev_vals)-1:
            working_vals.append(prev_vals[i+1] - prev_vals[i])
            i += 1
        print('working =', working_vals)
        if final_vals:
            ret_vals.append(working_vals[-1])
        else:
            ret_vals.append(working_vals[0])
        prev_vals = working_vals
        working_vals = []
    
    return ret_vals

def test_pyramid():
    data = get_data('input.txt')
    line = data.split('\n')[0]
    print(find_pyramid(line, False))

def predict_next(final_vals):
    next_vals = [0]
    i = len(final_vals)-1
    # B - A = C
    # B = A + C
    while i >= 0:
        next_vals.append(final_vals[i] + next_vals[-1])
        i -= 1
    
    return next_vals[-1]

def predict_prev(first_vals):
    prev_vals = [0]
    i = len(first_vals)-2
    # B - A = C
    # A = B - C
    # first_vals[i] is the first (leftmost) value of that row
    # prev_vals[-1] is the number below that
    # first_vals[i] - prev_vals[i] = prev_vals[-1]
    # prev_vals[i] = 
    while i >= 0:
        print(first_vals[i], '-', prev_vals[-1], '=', first_vals[i] - prev_vals[-1])
        prev_vals.append(first_vals[i] - prev_vals[-1])
        i -= 1
    
    print('prev vals =', prev_vals)
    return prev_vals[-1]

def part1():
    data = get_data('input.txt')
    sum = 0
    for line in data.split('\n'):
        if line == '':
            continue
        final_vals = find_pyramid(line, True)
        # print('final vals', final_vals)
        next_val = predict_next(final_vals)
        # print(next_val)
        sum += next_val
    
    print(sum)

def part2_test():
    data = get_data('input.txt')
    line = data.split('\n')[0]
    print('line =', line)
    first_vals = find_pyramid(line, False)
    print('first vals are', first_vals)
    prev_val = predict_prev(first_vals)
    print('prev val is', prev_val)

def part2():
    data = get_data('input.txt')
    sum = 0
    for line in data.split('\n'):
        if line == '':
            continue
        first_vals = find_pyramid(line, False)
        # print('first vals', first_vals)
        prev_vals = predict_prev(first_vals)
        # print(next_val)
        sum += prev_vals
    
    print(sum)



part2()

'''
    _ 14
     12 21
      9 28
       19 35
    
  4 5 9
   1 4 7
    3 3 3
     0 0
'''