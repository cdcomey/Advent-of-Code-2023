NUM_REDS = 12
NUM_GREENS = 13
NUM_BLUES = 14

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

def analyze_color(pull_string):
    if pull_string == '':
        return False
    assert(' ' in pull_string)

    space_loc = pull_string.find(' ')
    amount = int(pull_string[:space_loc])
    color = pull_string[space_loc+1:]
    # print(amount, color)

    if color == 'red' and amount > NUM_REDS:
        # print('TOO MANY RED')
        return False
    if color == 'green' and amount > NUM_GREENS:
        # print('TOO MANY GREEN')
        return False
    if color == 'blue' and amount > NUM_BLUES:
        # print('TOO MANY BLUE')
        return False
    
    return True

# determines if a round was possible
def game_analyzer(line):
    rounds = line.split('; ')
    rounds[0] = rounds[0][rounds[0].find(': ')+2:]
    for round in rounds:
        if ', ' in round:
            if not all(analyze_color(pull) for pull in round.split(', ')):
                return False
        else:
            if not analyze_color(round):
                return False
            
    return True

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
    pass