def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# '13  8  6 25 57  4' ->
# [13, 8, 25, 57, 4]
def isolate_numbers(string):
    nums = [int(i) for i in string.split(' ') if i != '']
    return nums

# count the number of matches between the scratch card
# and the winning numbers for that card
def count_matches(my_nums, winning_nums):
    counter = 0
    for num in my_nums:
        if num in winning_nums:
            counter += 1
    
    return counter

# obtain my nums and winning nums from the line
def get_nums(card):
    line_start = card.find(': ')+2
    divider = card.find(' | ')
    my_nums = isolate_numbers(card[line_start:divider])
    winning_nums = isolate_numbers(card[divider+3:])

    return my_nums, winning_nums

# calculate the number of points the scratch cards earn
def part1():
    data = get_data('input.txt')
    points = 0
    for card in data.split('\n'):
        # skip empty lines
        if card == '':
            continue

        # isolate the important data from the divider
        # and useless text at the start
        my_nums, winning_nums = get_nums(card)
        matches = count_matches(my_nums, winning_nums)
        
        # this is the formula for points for the cards
        if matches > 0:
            points += 2 ** (matches-1)
    
    print('The total of your points is', points)

def part2():
    # get the cards from the data while skipping empty lines
    data = get_data('input.txt')
    cards = [i for i in data.split('\n') if i != '']

    # each entry of this list corresponds to a card
    # since how many cards each card wins is fixed,
    # and is a number used frequently in other iterations,
    # we save that number in this list for fast lookups
    # this saves us from recursions telling us data we already found
    card_winnings = [0 for _ in range(len(cards))]

    # we will go in reverse, since by the time we get to card n,
    # we know how much each card after it it might win
    i = len(cards)-1
    while i >= 0:
        card = cards[i]
        my_nums, winning_nums = get_nums(card)
        matches = count_matches(my_nums, winning_nums)
        running_total = matches

        # for n matches, add up the totals for the next n cards
        while matches > 0 and matches+i < len(card_winnings):
            running_total += card_winnings[matches+i]
            matches -= 1
        
        card_winnings[i] = running_total
        i -= 1
    
    # add up our winnings, inluding all our original cards
    total_cards = 0
    for winnings in card_winnings:
        total_cards += winnings
    total_cards += len(cards)
    
    print('You won a total of', total_cards, 'cards')

part2()