from functools import cmp_to_key

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def card_value(card):
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    return card_ranks.index(card)+1

# this function is the way it is because i misread the rules
# but i think its a better ranking scheme anyway
# i thought you broke ties by comparing the relevant groupings of cards
# like in poker. eg 77888 beats 88777 because 888 beats 777
# but AoC wants to check in order of the cards, so 77888 would beat 88777
def find_hand_type(hand):
    # types: 
    # five of a kind
    # four of a kind
    # full house
    # three of a kind
    # two pairs
    # one pair
    # high card
    sorted_hand = [card_value(i) for i in hand]
    sorted_hand = sorted(sorted_hand)

    # five of a kind
    # only one possibility: AAAAA
    if sorted_hand[0] == sorted_hand[4]:
        return [6, sorted_hand[0], 0, 0, 0, 0]
    
    # four of a kind
    # AAAAB or ABBBB
    if sorted_hand[0] == sorted_hand[3]:
        return [5, sorted_hand[0], sorted_hand[4], 0, 0, 0]
    if sorted_hand[1] == sorted_hand[4]:
        return [5, sorted_hand[1], sorted_hand[0], 0, 0, 0]
    
    # full house
    # AAABB or 
    if sorted_hand[0] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]:
        return [4, sorted_hand[0], sorted_hand[3], 0, 0, 0]
    # AABBB
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[4]:
        return [4, sorted_hand[2], sorted_hand[0], 0, 0, 0]
    
    # three of a kind
    # AAABC or ABBBC or ABCCC
    if sorted_hand[0] == sorted_hand[2]:
        return [3, sorted_hand[0], sorted_hand[3], sorted_hand[4], 0, 0]
    if sorted_hand[1] == sorted_hand[3]:
        return [3, sorted_hand[1], sorted_hand[0], sorted_hand[4], 0, 0]
    if sorted_hand[2] == sorted_hand[4]:
        return [3, sorted_hand[2], sorted_hand[0], sorted_hand[1], 0, 0]
    
    # two pairs
    # AABBC or AABCC or ABBCC
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3]:
        return [2, sorted_hand[0], sorted_hand[2], sorted_hand[4], 0, 0]
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4]:
        return [2, sorted_hand[0], sorted_hand[3], sorted_hand[2], 0, 0]
    if sorted_hand [1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]:
        return [2, sorted_hand[1], sorted_hand[3], sorted_hand[0], 0, 0]
    
    # one pair
    # AABCD or ABBCD or ABCCD or ABCDD
    if sorted_hand[0] == sorted_hand[1]:
        return [1, sorted_hand[0], sorted_hand[2], sorted_hand[3], sorted_hand[4], 0]
    if sorted_hand[1] == sorted_hand[2]:
        return [1, sorted_hand[1], sorted_hand[0], sorted_hand[3], sorted_hand[4], 0]
    if sorted_hand[2] == sorted_hand[3]:
        return [1, sorted_hand[2], sorted_hand[0], sorted_hand[1], sorted_hand[4], 0]
    if sorted_hand[3] == sorted_hand[4]:
        return [1, sorted_hand[3], sorted_hand[0], sorted_hand[1], sorted_hand[2], 0]
        
    
    return [0, sorted_hand[0], sorted_hand[1], sorted_hand[2], sorted_hand[3], sorted_hand[4]]

def compare_card_rank(card1, card2):
    return card_value(card1) - card_value(card2)

def compare_hands(hand1, hand2):
    # print('comparing', hand1, 'and', hand2)
    rankings1 = find_hand_type(hand1)
    rankings2 = find_hand_type(hand2)
    for r1, r2 in zip(rankings1, rankings2):
        if r1 != r2:
            return r1 - r2
    
    return 0

def pair_sort(hands, bets):
    for i in range(len(hands)):
        for j in range(len(hands)-1):
            if compare_hands(hands[i], hands[j]) < 0:
                tmp = hands[i]
                hands[i] = hands[j]
                hands[j] = tmp

                tmp = bets[i]
                bets[i] = bets[j]
                bets[j] = tmp
    
    return hands, bets


def part1():
    data = get_data('input.txt')
    hands, bets = [], []
    for line in data.split('\n'):
        hand, bet = line.split(' ')
        hands.append(hand)
        bets.append(int(bet))

    # for hand, bet in zip(hands, bets):
    #     print(hand, bet)
    
    sorted_hands, sorted_bets = pair_sort(hands, bets)

    for i, (hand, bet) in enumerate(zip(sorted_hands, sorted_bets)):
        print(i+1, hand, bet)

    product = 0
    for i, bet in enumerate(sorted_bets):
        # print((i+1), '+', bet, end=' = ')
        product += (i+1) * bet
        # print(f'{product:,}')
    
    print(product)

part1()
# 249037474 is too high