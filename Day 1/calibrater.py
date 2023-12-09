def read_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def find_calibration_num(line):
    if line == '':
        return 0
    
    first_digit, last_digit = -1, -1
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break
    
    assert(first_digit >= 0)
    assert(last_digit >= 0)
    return 10*first_digit + last_digit

def sum_of_list(list):
    sum = 0
    for num in list:
        sum += num
    
    return sum


data = read_data('data.txt')
nums = []
for line in data.split('\n'):
    nums.append(find_calibration_num(line))

print('The sum of the calibration numbers is', sum_of_list(nums))