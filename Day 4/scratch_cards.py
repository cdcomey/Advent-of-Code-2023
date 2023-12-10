def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# separate out numbers from the list
def isolate_numbers(string):
    nums = [int(i) for i in string.split(' ') if i != '']
    return nums

def score_card(my_nums, winning_nums):
    counter = 0
    for num in my_nums:
        if num in winning_nums:
            counter += 1
    
    if counter == 0:
        return 0
    return 2 ** (counter-1)

def part1():
    data = get_data('input.txt')
    points = 0
    for i, card in enumerate(data.split('\n')):
        if card == '':
            continue

        line_start = card.find(': ')+2
        divider = card.find(' | ')
        my_nums = isolate_numbers(card[line_start:divider])
        winning_nums = isolate_numbers(card[divider+3:])
        points += score_card(my_nums, winning_nums)
        print('CARD', i, 'gets', score_card(my_nums, winning_nums), 'points')
    
    print('The total of your points is', points)

part1()