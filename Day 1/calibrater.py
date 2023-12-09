def read_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def find_calibration_num(line, reversed=False):
    number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if reversed:
        number_words = [word[::-1] for word in number_words]
        line = line[::-1]

    for i, char in enumerate(line):
        # eg 1,2,3
        if char.isdigit():
            return int(char)
        # check n chars past this one to check with n-length word
        for j, word in enumerate(number_words):
            if line[i:i+len(word)] == word:
                return j+1
    
    return -1

def find_calibration_nums(line):
    if line == '':
        return 0
    
    first_digit = find_calibration_num(line, False)
    last_digit = find_calibration_num(line, True)
    
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
    nums.append(find_calibration_nums(line))

print('The sum of the calibration numbers is', sum_of_list(nums))