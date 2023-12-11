from functools import cmp_to_key

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def card_value(card):
    card_ranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    return card_ranks.index(card)+1

def find_hand_type(hand):
    num_Js = hand.count('J')
    sorted_hand = [card_value(i) for i in hand]
    sorted_hand = sorted(sorted_hand, reverse=True)

    # five of a kind
    # AAAAA, AAAAJ, AAAJJ, AAJJJ, AJJJJ
    # we need a separate case for this because the following one will return 10
    if hand == 'JJJJJ':
        return 6
    if sorted_hand.count(sorted_hand[0]) + num_Js == 5:
        return 6
    
    # four of a kind
    # AAAAB, AAABJ, AABJJ, ABJJJ
    # ABBBB, ABBBJ, ABBJJ
    if sorted_hand.count(sorted_hand[0]) + num_Js == 4:
        return 5
    if sorted_hand.count(sorted_hand[1]) + num_Js == 4:
        return 5
    
    
    # full house
    # AAABB
    if sorted_hand[0] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]:
        return 4
    # AABBJ
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3] and num_Js == 1:
        return 4
    # AABBB
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[4]:
        return 4
    
    # three of a kind
    # AAABC, ABCJJ, AABCJ
    if sorted_hand.count(sorted_hand[0]) + num_Js == 3:
        return 3
    # ABBBC, ABBCJ
    if sorted_hand.count(sorted_hand[1]) + num_Js == 3:
        return 3
    # ABCCC, ABCCJ
    if sorted_hand.count(sorted_hand[2]) + num_Js == 3:
        return 3
    
    # two pairs
    # AABBC or AABCC or ABBCC
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[2] == sorted_hand[3]:
        return 2
    if sorted_hand[0] == sorted_hand[1] and sorted_hand[3] == sorted_hand[4]:
        return 2
    if sorted_hand [1] == sorted_hand[2] and sorted_hand[3] == sorted_hand[4]:
        return 2
    
    # one pair
    # AABCD or ABBCD or ABCCD or ABCDD
    for n in range(len(sorted_hand)-1):
        if sorted_hand[n] == sorted_hand[n+1]:
            return 1
    if num_Js == 1:
        return 1
        
    
    return 0

def compare_card_rank(card1, card2):
    return card_value(card1) - card_value(card2)

def compare_hands(hand1, hand2):
    # print('comparing', hand1, 'and', hand2)
    hand_type1 = find_hand_type(hand1)
    hand_type2 = find_hand_type(hand2)

    if hand_type1 == hand_type2:
        for h1, h2 in zip(hand1, hand2):
            if card_value(h1) != card_value(h2):
                return card_value(h1) - card_value(h2)
    
        return 0

    return hand_type1 - hand_type2

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

def print_hand_type(hand_type):
    if hand_type == 6:
        return 'FIVE'
    if hand_type == 5:
        return 'FOUR'
    if hand_type == 4:
        return 'FULL HOUSE'
    if hand_type == 3:
        return 'THREE'
    if hand_type == 2:
        return 'TWO PAIRS'
    if hand_type == 1:
        return 'ONE PAIR'
    return 'HIGH CARD'

def part2():
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
        print(i+1, hand, bet, print_hand_type(find_hand_type(hand)))

    product = 0
    for i, bet in enumerate(sorted_bets):
        # print((i+1), '+', bet, end=' = ')
        product += (i+1) * bet
        # print(f'{product:,}')
    
    print(product)

part2()