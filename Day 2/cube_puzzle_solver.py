NUM_REDS = 12
NUM_GREENS = 13
NUM_BLUES = 14

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# take in a string, eg '20 green'
# determine if this amount is possible given the min amounts
def analyze_color_possibility(pull_string):
    space_loc = pull_string.find(' ')
    amount = int(pull_string[:space_loc])
    color = pull_string[space_loc+1:]

    if color == 'red' and amount > NUM_REDS:
        return False
    if color == 'green' and amount > NUM_GREENS:
        return False
    if color == 'blue' and amount > NUM_BLUES:
        return False
    
    return True

# determines if a round was possible
def game_analyzer(line):
    if line == '':
        return False
    
    # a round is eg '3 blue, 4 green, 12 red'
    rounds = line.split('; ')

    # remove the 'Game: ' part from the first round
    rounds[0] = rounds[0][rounds[0].find(': ')+2:]

    # if any of the color pulls are not possible, the round is not possible
    # if the round is not possible, neither is the game
    for round in rounds:
        if ', ' in round:
            if not all(analyze_color_possibility(pull) for pull in round.split(', ')):
                return False
        else:
            if not analyze_color_possibility(round):
                return False

    # the game is only possible if every color pull is        
    return True

def update_min_cubes(pull, min_reds, min_greens, min_blues):
    space_loc = pull.find(' ')
    amount = int(pull[:space_loc])
    color = pull[space_loc+1:]

    if color == 'red':
        min_reds = max(min_reds, amount)
    elif color == 'green':
        min_greens = max(min_greens, amount)
    elif color == 'blue':
        min_blues = max(min_blues, amount)
    
    return min_reds, min_greens, min_blues


def min_cubes(line):
    if line == '':
        return 0, 0, 0
    min_reds, min_greens, min_blues = 0, 0, 0
    rounds = line.split('; ')
    rounds[0] = rounds[0][rounds[0].find(': ')+2:]

    for round in rounds:
        if ', ' in round:
            pulls = round.split(', ')
            for pull in pulls:
                min_reds, min_greens, min_blues = update_min_cubes(pull, min_reds, min_greens, min_blues)
        else:
            min_reds, min_greens, min_blues = update_min_cubes(round, min_reds, min_greens, min_blues)
    
    return min_reds, min_greens, min_blues


def part1():
    possible_games = 0
    sum = 0
    data = get_data('input.txt')
    for i, line in enumerate(data.split('\n')):
        print('GAME', i, ':', game_analyzer(line))
        if game_analyzer(line):
            possible_games += 1
            sum += i+1


    print('There are', possible_games, 'possible games')
    print('The sum of the IDs of the possible games is', sum)

def part2():
    sum = 0
    data = get_data('input.txt')
    for i, line in enumerate(data.split('\n')):
        r, g, b = min_cubes(line)
        print('GAME {}: {}R, {}G, {}B'.format(i+1, r, g, b))
        sum += r*g*b
    print('sum of powers:', sum)
    
part2()