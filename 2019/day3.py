# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:05:23 2019

@author: hoskim1
"""

direction_dictionary = {'U': (0,1),
                        'D': (0,-1),
                        'R': (1,0),
                        'L': (-1,0)}

def read_data():
    ##return
    
    with open("day3_1.txt", "r") as f:
        d = []
        for line in f:
            data = line.split(",")
            data = [(value[0], int(value[1:])) for value in data]
            d.append(data)
            
    return d


def move_dist(location, direction, distance):
    positions = []
    
    cardinal_motion = direction_dictionary[direction]
    for step in range(distance):
        location = (location[0] + cardinal_motion[0], 
                    location[1] + cardinal_motion[1])
        positions.append(location)
        

    
    return positions
    
total_positions = []

for wire in read_data():
    positions = []
    start = (0,0)
    for instruction in wire:
        pos = move_dist(start, instruction[0], instruction[1])
        positions += pos
        start = pos[-1]
        
    total_positions.append(positions)
    

both = set(total_positions[0]) & set(total_positions[1])
min_dist = min([abs(x) + abs(y) for (x,y) in both])
print(min_dist)

#for wire_1_pos in total_positions[0]:
#    if wire_1_pos in total_positions[1]:
#        dist = abs(wire_1_pos[0]) + (wire_1_pos[1])
#        if dist < min_dist:
#            min_dist = dist
#            
#print(min_dist)
#    

### part 2



def move_dist_2(prior_pos, location, direction, distance, prev_dist):
    positions = prior_pos
    
    cardinal_motion = direction_dictionary[direction]
    for step in range(distance):
        location = (location[0] + cardinal_motion[0], 
                    location[1] + cardinal_motion[1])
        
        if location not in positions:
            positions[location] = step + 1 + prev_dist
        
    end_loc = location
    
    return positions, end_loc

total_positions = []

for wire in read_data():
    positions = {}
    start = (0,0)
    prev_dist = 0
    for instruction in wire:
        pos, start = move_dist_2(positions, start, instruction[0], instruction[1], prev_dist)
        prev_dist += instruction[1]
        
    total_positions.append(positions)
    

both = set(total_positions[0].keys()) & set(total_positions[1].keys())
min_dist = min([total_positions[0][key] + total_positions[1][key] for key in both])
print(min_dist)











    
