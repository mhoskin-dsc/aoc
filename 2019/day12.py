# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:50:53 2019

@author: hoskim1
"""


input_pos = [[-8, -18, 6],
             [-11, -14, 4],
             [8, -3, -10],
             [-2, -16, 1]]

pos = input_pos
vel  = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

#pos = [[1,1,0],[2,2,0],[3,3,0],[4,4,0]]


def update_vel(pos, vel):
    
    delta_v = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    
    for body_index, body in enumerate(pos):
        for dim_index, dim in enumerate(body):
            dv = 0
            for body_compare in pos:
                other_dim = body_compare[dim_index]
                if dim > other_dim:
                    temp_value = -1
                elif dim < other_dim:
                    temp_value = +1
                else:
                    temp_value = 0
                    
                dv += temp_value
            
            delta_v[body_index][dim_index] = dv
    
    
    for index, velocity in enumerate(vel):
        vel[index] = [v + dv for v, dv in zip(vel[index], delta_v[index])]
    
    return vel

    
def update_pos(pos, vel):
    
    for index, position in enumerate(pos):
        pos[index] = [p + v for p, v in zip(pos[index],vel[index])]
    
    return pos


def energy(pos,vel):
    """
    Takes in two lists of arrays of bodies + returns the total energy
    """
    
    ke = []
    pe = []
    
    energy = 0
    for i in pos:
        
        e = abs(i[0]) + abs(i[1]) + abs(i[2])
        pe.append(e)
        
    for i in vel:
        e = abs(i[0]) + abs(i[1]) + abs(i[2])
        ke.append(e)
        
    me = [k * p for k,p in zip(ke,pe)]
    
    energy = sum(me)
     
    return energy



#for _ in range(1000):
#    
#    vel = update_vel(pos,vel)
#    pos = update_pos(pos,vel)
#    
#print(energy(pos,vel))
input_pos = [[-8, -18, 6],
             [-11, -14, 4],
             [8, -3, -10],
             [-2, -16, 1]]
pos = input_pos[:]
input_vel  = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
vel = input_vel[:]

index = 0 
repeat_count = [0,0,0,0]

no_repeat = True

print("BEGIN PHASE 2")
    
while(no_repeat):
    vel = update_vel(pos, vel)
    pos = update_pos(pos, vel)
    
    index += 1
    
    for body_index in range(len(input_pos)):
        if ((vel[body_index] == input_vel[body_index]) & 
            (pos[body_index] == input_pos[body_index])):
            print(body_index, " : ", index)

            if repeat_count[body_index] == 0:
                repeat_count[body_index] = index
    
    if min(repeat_count) > 0:
        no_repeat = False
            
                
    
#        
#
#
#
#vel_log = []
#pos_log = []
#
#vel_log.append(vel[:])
#pos_log.append(pos[:])
#
#vel_log
#pos_log
#
#no_repeat = True
#while (no_repeat):
#    
#    vel = update_vel(pos,vel)
##    print(vel)
#    pos = update_pos(pos,vel)
#    
#    if (vel in vel_log and pos in pos_log):
#        print("escape: ", i)
#        no_repeat = False
#    else:    
#        vel_log.append(vel[:])
#        pos_log.append(pos[:])
#    
#    
        i += 1




