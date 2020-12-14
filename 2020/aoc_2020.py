# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:09:37 2020

@author: hoskim1
"""
import time

start_time = time.time()


#%% AOC Day 1 Part 1

fp = 'input_day_1.txt'

with open(fp) as f:
    data = f.readlines()
    
clean_data = [int(d.strip()) for d in data]
clean_data.sort()

def sum_looper(nums, target):
    '''
    finds two numbers from inside the collection nums, which sum to target
    returns the two values, and the count
    '''
    c=0
    for idx, i in enumerate(nums):
        for j in nums[idx:]:
            c+=1
            if i + j == target:
                return(i,j,c) # 914 1106 1010884
    
    return('no match')

def summer_d1p1(nums, target):
    v1,v2,c = sum_looper(nums, target)
    return(v1,v2,v1*v2,c)

def print_results_d1p1(res):
    print("DAY 1 PART 1")
    print("{}*{}= {} in {} iter".format(*res))

print_results_d1p1(summer_d1p1(clean_data, 2020))

#%% AOC Day 1 Part 2

fp = 'input_day_1.txt'

with open(fp) as f:
    data = f.readlines()
    
clean_data = [int(d.strip()) for d in data]
clean_data.sort()

def summer_d1p2(nums, target):
    
    c = 0
    for idx_0, i in enumerate(clean_data[:5]):
        for idx_1, j in enumerate(clean_data[idx_0:]):
            for k in clean_data[idx_0 + idx_1:]:
                c+=1
                if i + j + k == target:
                    return(i,j,k, i*j*k, c) # 401 661 958 253928438

def print_results_d1p2(res):
    print("DAY 1 PART 2")
    print("{}*{}*{}= {} in {} iter".format(*res))

print_results_d1p2(summer_d1p2(clean_data, 2020))
#%% AOC Day 2 Part 1

from collections import Counter

fp = 'input_day_2.txt'

with open(fp) as f:
    data = f.readlines()

clean_data = [d.strip() for d in data]
test = ['1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccc']

valid_count = 0
for pw_data in clean_data:
    
    spaced = pw_data.split(' ')
    
    limits = spaced[0].split('-') 
    limits = [int(v) for v in limits]
    
    char = spaced[1][:-1]
    
    counter = Counter(spaced[2])
    
    if counter[char] >= limits[0] and counter[char] <= limits[1]:
        valid_count += 1
        
print(valid_count) #456
    
#%% AOC Day 2 Part 2
    

fp = 'input_day_2.txt'

with open(fp) as f:
    data = f.readlines()

clean_data = [d.strip() for d in data]
test = ['1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc']

valid_count = 0
for pw_data in clean_data:
    
    spaced = pw_data.split(' ')
    
    limits = spaced[0].split('-') 
    limits = [int(v) for v in limits]
    
    char = spaced[1][:-1]

    if ((spaced[2][limits[0] - 1] == char) + (spaced[2][limits[1] - 1] == char)) == 1:
        valid_count += 1
    
print(valid_count) #308
    

#%% AOC Day 3 Part 1
import math

fp = 'input_day_3.txt'

with open(fp) as f:
    data = f.readlines()
    
#split_data = [d.split() for d in data]

width_needed = 3 * len(data)
string_multiplyer = math.ceil(width_needed / len(data[0])) + 1 #unsure as to why maths needs + 1

data_ext = [d.strip() * string_multiplyer for d in data]

tree_count = 0
for row_idx,  row in enumerate(data_ext):
    
    if row[3*row_idx] == '#':
        tree_count += 1

print(tree_count) # 207


#%% AOC Day 3 Part 2
import math

fp = 'input_day_3.txt'
#fp = 'test_day_3.txt'

with open(fp) as f:
    data = f.readlines()
    
rights = [1,3,5,7]
doubles = [0.5]

width_needed = max(rights) * len(data)
string_multiplyer = math.ceil(width_needed / len(data[0])) + 2 #unsure as to why maths needs + 2

data_ext = [d.strip() * string_multiplyer for d in data]

tree_count = {1:0, 3:0, 5:0, 7:0, 0.5:0}
for row_idx,  row in enumerate(data_ext):
    
    for r in rights:
        if row[r*row_idx] == '#':
            tree_count[r] += 1
            
    for d in doubles:
        if row_idx % 2 == 0:
            if row[int(d*row_idx)] == '#':
                tree_count[d] += 1

multiplication_total = 1
for v in tree_count.values():
    multiplication_total *= v
print(multiplication_total) # 2655892800


#%% AOC Day 4 Part 1

mandatory = ['byr', 'iyr','eyr','hgt','hcl','ecl','pid']

def validate(dict_record, mandatory):
    return set(mandatory).issubset(set(dict_record.keys()))

fp = 'input_day_4.txt'
#fp = 'test_day_4.txt'

with open(fp) as f:
    data = f.readlines()

record = []
count_valid = 0
idx = 0
for line in data:
    
    if line != "\n":
        record.extend(line.strip().split(' '))
    
    if line == "\n" or line == data[-1]:
        dict_record = {d.split(':')[0]:d.split(':')[1] for d in record}
        count_valid += validate(dict_record, mandatory)
        record = []

print(count_valid) #210


#%% AOC Day 4 Part 2


def byr(record):
    assert record['byr'].isdigit()
    record['byr'] = int(record['byr'])
    return(record['byr'] >= 1920 and record['byr'] <= 2002)
    
def iyr(record):
    assert record['iyr'].isdigit()
    record['iyr'] = int(record['iyr'])
    return(record['iyr'] >= 2010 and record['iyr'] <= 2020)

def eyr(record):
    assert record['eyr'].isdigit()
    record['eyr'] = int(record['eyr'])
    return(record['eyr'] >= 2020 and record['eyr'] <= 2030)

def hgt(record):
    lims = {'cm':[150,193],
            'in':[59,76]}
    
    h_type = record['hgt'][-2:]
    try:
        val = int(record['hgt'][:-2])
    except ValueError:
        return False
    
    return h_type in lims.keys() and val >= lims[h_type][0] and val <= lims[h_type][1]
      
def hcl(record):
    return record['hcl'][0] == '#' and record['hcl'][1:].isalnum() and len(record['hcl']) == 7

def ecl(record):
    return record['ecl'] in ["amb", "blu", "brn", "grn", "gry", "hzl", "oth"]

def pid(record):
    return len(record['pid']) == 9 and record['pid'].isdigit()
    
def validate(record, mandatory):
    if(set(mandatory.keys()).issubset(set(dict_record.keys()))):
        return all(check(record) for check in mandatory.values())
    else:
        return False

mandatory = {'byr':byr, 'iyr':iyr,'eyr':eyr,'hgt':hgt,'hcl':hcl,'ecl':ecl,'pid':pid}

fp = 'input_day_4.txt'
#fp = 'test_day_4.txt'

with open(fp) as f:
    data = f.readlines()

record = []
count_valid = 0
idx = 0
for line in data:
    
    if line != "\n":
        record.extend(line.strip().split(' '))
    
    if line == "\n" or line == data[-1]:
        dict_record = {d.split(':')[0]:d.split(':')[1] for d in record}
        count_valid += validate(dict_record, mandatory)
        record = []

print(count_valid) #131



#%%AOC Day 5 Part 1

fp = 'input_day_5.txt'

with open(fp) as f:
    data = f.readlines()
    
seat_max_id = 0

for seat in data:
    seat = seat.strip()
    row = int(seat[:7].replace('F','0').replace('B','1'),2)
    col = int(seat[7:].replace('L','0').replace('R','1'),2)
    
    seat_max_id = max(seat_max_id, row * 8 + col)

print(seat_max_id) # 913


#%%AOC Day 5 Part 2

fp = 'input_day_5.txt'

with open(fp) as f:
    data = f.readlines()
    
seat_max_id = 0
seat_info = []

for seat in data:
    seat = seat.strip()
    row = int(seat[:7].replace('F','0').replace('B','1'),2)
    col = int(seat[7:].replace('L','0').replace('R','1'),2)
    
    seat_info.append((row,col))

seat_info.sort()
row_0 = seat_info[0][0]
row_n = seat_info[-1][0]

for row in range(row_0 + 1, row_n):
    for col in range(0,8):
        if (row, col) not in seat_info:
            print(row * 8 + col) #717

#%%AOC Day 6 Part 1
from collections import Counter

fp = 'input_day_6.txt'

with open(fp) as f:
    data = f.read().split('\n\n')

total = 0
for group in data:
#    group_size = group.count('\n')
    group = group.replace('\n','')    
    
#    all_compare = [c == group_size for c in Counter(group).values()]
    total += len(Counter(group))

print(total) #6259

#%%AOC Day 6 Part 2
from collections import Counter

fp = 'input_day_6.txt'
#fp = 'test_day_6.txt'
with open(fp) as f:
    data = f.read().split('\n\n')

total = 0
for group in data:
    group_size = group.count('\n') + 1
    group = group.replace('\n','')  

    all_compare = [c == group_size for c in Counter(group).values()]
    total += sum(all_compare)

print(total) #3178

#%% AOC Day 7 Part 1

fp = 'input_day_7.txt'
#fp = 'test_day_7.txt'

with open(fp) as f:
    data = f.readlines()
    
bag_contents = {}
content_bags = {}

for row in data:    
    
    (source, contents) = row.split(' contain ')
    
    source = source[:-1]
    bags = contents.split(', ')
    for bag in bags:
        
        bag = bag.split(sep=' ',
                        maxsplit=1)
        
        bag[1] = bag[1].strip()
        bag[1] = bag[1].rstrip('.')
        bag[1] = bag[1].rstrip('s')
        
        if 'no' in bag[0]:
            pass
        else:
            if source in content_bags:
                content_bags[source][bag[1]] = int(bag[0])
            else:
                content_bags[source] = {bag[1]: int(bag[0])}
        
        if 'no' in bag[0]:
            bag[0] = 0
        else: 
            if bag[1] in bag_contents:
                bag_contents[bag[1]][source] = int(bag[0])
                
            else:
                bag_contents[bag[1]] = {source: int(bag[0])}
    
    
    
aim = 'shiny gold bag'
carry_bags = []

def search(bag, carry_bags):
    
    if bag in bag_contents:
        
        for b in bag_contents[bag].keys():
            if b not in carry_bags:
                carry_bags.append(b)
            carry_bags.extend(search(b, carry_bags))
            carry_bags = list(set(carry_bags))
            
    else:
        return carry_bags
    
    return carry_bags
    

print('d7p1: ', len(set(search(aim, carry_bags)))) # 115

# %% run code for D7P2
ibc = 0

def count_bags(aim, mult):
    global ibc
    if aim in content_bags.keys():

        ibc += mult * sum(content_bags[aim].values())
        for b, n in content_bags[aim].items():
            
            count_bags(b, mult * n)

count_bags(aim,1)

print('d7p2: ',ibc)
    
    
# %% 

fp = 'input_day_8.txt'
#fp = 'test_day_8.txt'

with open(fp) as f:
    data = f.readlines()

def clean_split(row):
    
    row = row.strip()
    row = row.split(' ')
    
    return (row[0], int(row[1]))

def acc(arg, move = 1):
    global accumulator
    accumulator += arg
    jmp(move)
    

def jmp(arg):
    global working_index
    working_index.append(working_index[-1] + arg)
    
def nop(arg, move = 1):
    jmp(move)



# %%
def execute(instr):
    global working_index
    working_index = [0]

    while(running):
        
        if len(working_index) != len(set(working_index)):
            return('LOOP')
        if working_index[-1] == len(instr):
            return('OK')
        
        op, arg = clean_split(instr[working_index[-1]])

        operations[op](arg)
        
#        if len(working_index) != len(set(working_index)):
#            if op == 'acc':
#                acc(-arg, 0)
#                
#            running = False
    
# %% D8 P 1

operations = {'acc':acc, 
              'jmp':jmp, 
              'nop':nop}

working_index = []
accumulator = 0
running = True
    
print('exit: {0} acc: {1}'.format(execute(data), accumulator))#1394    

# %% D8 P2

for i in range(len(data)):
    working_index = []
    accumulator = 0
    running = True
    
    op, arg = clean_split(data[i])
    
    trial_data = data.copy()
    if op == 'jmp':
        trial_data[i] = 'nop {0}\n'.format(arg)
        
    elif op == 'nop':
        trial_data[i] = 'jmp {0}\n'.format(arg)    
    
#    print(data[i], trial_data[i])
    exit_code = execute(trial_data)
    if exit_code == 'OK':
        print('exit: {0} acc: {1}'.format('OK',accumulator)) #1626
        break

# %% AOC D9 P1

fp = 'input_day_9.txt'

with open(fp) as f:
    data = f.readlines()
    
data = [int(d.strip()) for d in data]

rolling = 25

t = []#
for d_idx in range(25, len(data)):
    search_window = data[d_idx-25:d_idx]
    
    result = sum_looper(search_window, data[d_idx])
    if result == 'no match':
        print(d_idx, data[d_idx]) # 572, 133015568
        sum_index = d_idx
        target_value = data[d_idx]
        break

#AOC D9 P2 function
def find_additive_range(data, target_value, target_idx):
    for d_idx in range(0, len(data)):
        tracking_sum = 0
        counter = d_idx
        while(tracking_sum < target_value):
            tracking_sum += data[counter]
            counter += 1
        if tracking_sum == target_value:
            contig_list = data[d_idx:counter]
            print(d_idx, counter)
            print(min(contig_list), max(contig_list), min(contig_list) + max(contig_list))
            break

find_additive_range(data, target_value, sum_index)

#%% AOC D10 P1
from collections import Counter
fp = 'input_day_10.txt'
#fp = 'test2_day_10.txt'
with open(fp) as f:
    data = f.readlines()
    

clean_data = [int(d.strip()) for d in data]
clean_data.append(0) #handle aircraft
clean_data.sort()
clean_data.append(clean_data[-1] + 3) #handle device

differences = []
for idx, cd in enumerate(clean_data[1:]):
    differences.append(cd-clean_data[idx])

summary = Counter(differences)
print('D10P1', summary[1] * summary[3])


#%% P2
flip = clean_data.copy()
flip.sort(reverse = True)

paths = {flip[0]:1}
for d in flip[1:]:

    paths[d] = sum([paths[i] for i in range(d+1, d+4) if i in paths])

print('D10P2', paths[0])

#%% AOC D11 P1
from copy import deepcopy
fp = 'input_day_11.txt'
#fp = 'test_day_11.txt'

with open(fp) as f:
    data = f.readlines()

def state_change(x_tar, y_tar, initial_state, new_board_state):
#    print('i:',initial_state)
    occ_neighbours = 0
#    print(x_tar, y_tar)
    for x in range(max(x_tar - 1,0), min(x_tar + 2,len(initial_state[0]))):
#        print('x:',x)
        for y in range(max(y_tar - 1,0), min(y_tar + 2,len(initial_state))):
#            print('y:',y)
            if x == x_tar and y == y_tar:
#                print('hit adjusting cell')
                pass
            else:
                try:
                    occ_neighbours += initial_state[y][x] == '#'
#                    print('occ:',occ_neighbours)
                except IndexError:
                    print(x_tar, y_tar, x,y)
#    print('m:',initial_state)
                    
    if initial_state[y_tar][x_tar] == 'L' and occ_neighbours == 0:
#        print('birth at:',y_tar,x_tar)
        new_board_state[y_tar][x_tar] = '#'
    elif initial_state[y_tar][x_tar] == '#' and occ_neighbours >= 4:
#        print('death')
#        print(y_tar,x_tar)
#        print(init_board_state[y_tar][x_tar])
        new_board_state[y_tar][x_tar] = 'L'
    
#    print('e:',initial_state)
#    print(new_board_state[y][x])
    return new_board_state

#%%
data = [d.strip() for d in data]
init_board_state = [[char.strip() for char in d] for d in data]

new_board_state = deepcopy(init_board_state)#.copy()

#%%

#init_board_state = [['L', 'L', 'L'], ['L', 'L', 'L'], ['L', 'L', 'L']]
#new_board_state = deepcopy(init_board_state)



no_match = True
idx = 1
while(no_match):
#    print(idx)
    idx+=1
    for x in range(len(init_board_state[0])):
        for y in range(len(init_board_state)):
            if init_board_state[y][x] != '.':
                new_board_state = state_change(x,y, init_board_state, new_board_state)
#                t = input('enter input')
#            print('n:',new_board_state)
#    print(new_board_state)    

    if new_board_state == init_board_state:
        seat_count = Counter([item for sublist in new_board_state for item in sublist])
        print(seat_count['#'])
        no_match = False
    else:
#        print('set new initial board')
        init_board_state = deepcopy(new_board_state)
#%% AOC 11 P2


#%% AOC 12 

fp = 'input_day_12.txt'
#fp = 'test_day_11.txt'

with open(fp) as f:
    data = f.readlines()
#%%P1

loc = [0,0,0] #x,y,angle from East

for move in data:
    direction = move[0]
    distance = int(move[1:].strip())
    
    if direction == 'E':
        loc[0] += distance
    elif direction == 'W':
        loc[0] -= distance
    elif direction == 'N':
        loc[1] += distance
    elif direction == 'S':
        loc[1] -= distance
    elif direction == 'R':
        loc[2] += distance
        loc[2] = loc[2] % 360
        
    elif direction == 'L':
        loc[2] -= distance
        loc[2] = loc[2] % 360
    
    elif direction == 'F':
        if loc[2] == 0:
            loc[0] += distance
        elif loc[2] == 90:
            loc[1] -= distance
        elif loc[2] == 180:
            loc[0] -= distance
        elif loc[2] == 270:
            loc[1] += distance
    
print(loc, abs(loc[0]) + abs(loc[1]))
    
#%%P1

wp = [10,1]
loc = [0,0]

for move in data:
    direction = move[0]
    distance = int(move[1:].strip())
    
    if direction == 'E':
        wp[0] += distance
    elif direction == 'W':
        wp[0] -= distance
    elif direction == 'N':
        wp[1] += distance
    elif direction == 'S':
        wp[1] -= distance
    elif direction == 'F':
        loc[0] += distance * wp[0]
        loc[1] += distance * wp[1]
    elif direction == 'R':
        n_rot = distance // 90
        for _ in range(n_rot):
            new_wp = [wp[1], -wp[0]]
            wp = new_wp

    elif direction == 'L':
        n_rot = distance // 90
        for _ in range(n_rot):
            new_wp = [-wp[1], wp[0]]
            wp = new_wp

print(loc, abs(loc[0]) + abs(loc[1]))

#%% 

fp = 'input_day_13.txt'
#fp = 'test_day_11.txt'

with open(fp) as f:
    timestamp = int(f.readline().strip())
    timetable = f.readline()

scheds = [int(t) for t in timetable.split(',') if t.isdigit()]

next_arrival = []
for sched in scheds:
    next_arrival.append(timestamp + (sched - timestamp % sched))


print((min(next_arrival)-timestamp) * scheds[next_arrival.index(min(next_arrival))])


#%%


print("elapsed: {0:.2f} seconds".format(time.time() - start_time))




