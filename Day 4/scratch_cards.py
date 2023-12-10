def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# separate out numbers from the list
def isolate_numbers(string):
    nums = [int(i) for i in string.split(' ') if i != '']
    return nums

def count_matches(my_nums, winning_nums):
    counter = 0
    for num in my_nums:
        if num in winning_nums:
            counter += 1
    
    return counter

def part1():
    data = get_data('input.txt')
    points = 0
    for card in data.split('\n'):
        if card == '':
            continue

        line_start = card.find(': ')+2
        divider = card.find(' | ')
        my_nums = isolate_numbers(card[line_start:divider])
        winning_nums = isolate_numbers(card[divider+3:])
        num_matches = count_matches(my_nums, winning_nums)
        if num_matches > 0:
            points += 2 ** (num_matches-1)
    
    print('The total of your points is', points)

def part2():
    data = get_data('input.txt')
    cards = [i for i in data.split('\n') if i != '']
    card_winnings = [0 for _ in range(len(cards))]
    i = len(cards)-1
    while i >= 0:
        card = cards[i]
        line_start = card.find(': ')+2
        divider = card.find(' | ')
        my_nums = isolate_numbers(card[line_start:divider])
        winning_nums = isolate_numbers(card[divider+3:])
        matches = count_matches(my_nums, winning_nums)
        running_total = matches

        while matches > 0 and matches+i < len(card_winnings):
            running_total += card_winnings[matches+i]
            matches -= 1
        
        card_winnings[i] = running_total
        i -= 1
    
    total_cards = 0
    for winnings in card_winnings:
        total_cards += winnings
    total_cards += len(cards)
    
    print('You won a total of', total_cards, 'cards')

part2()