import math

def get_data(file_name):
    f = open(file_name)
    data = f.read()
    f.close()
    return data

# for part 1
# simply check every time and add up all the wins
def analyze_race(max_time, max_distance):
    ways_to_win = 0
    for time in range(max_time+1):
        speed = time
        distance = (max_time-time) * speed
        if distance > max_distance:
            ways_to_win += 1
    
    return ways_to_win

'''
we have to exceed D
d = (T-t) * t
D = (T-t) * t
D = Tt - t^2
t^2 - Tt + D = 0

simply use the quadratic formula to find the two intercepts
'''
def analyze_race_formula(max_time, max_distance):
    b = -max_time
    sol1 = (-b + math.sqrt(b**2 - 4*max_distance)) // 2
    sol2 = (-b - math.sqrt(b**2 - 4*max_distance)) // 2

    lower_bound = min(sol1, sol2)
    upper_bound = max(sol1, sol2)

    lower_bound = math.ceil(lower_bound)
    upper_bound = math.floor(upper_bound)

    print(f'{lower_bound:,}, {upper_bound:,}')
    return upper_bound - lower_bound


def part1():
    data = get_data('input.txt')
    times, distances = data.split('\n')

    # isolate nums
    times = [int(i) for i in times.split(' ') if i != '' and i != 'Time:']
    distances = [int(i) for i in distances.split(' ') if i != '' and i != 'Distance:']

    win_product = 1
    for time, distance in zip(times, distances):
        ways_to_win = analyze_race(time, distance)
        print(ways_to_win, 'ways to win')
        win_product *= ways_to_win
    
    print('product is', win_product)

def part2():
    data = get_data('input.txt')
    time, distance = data.split('\n')
    time = int(time[12:].replace(' ', ''))
    distance = int(distance[11:].replace(' ', ''))
    print(time)
    print(distance)
    print(analyze_race_formula(time, distance))


part2()