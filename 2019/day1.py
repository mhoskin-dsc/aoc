# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:17:55 2019

@author: hoskim1
"""
import time 
### day 1 part 1

# Floor ( Mass / 3 ) - 2

fuel = 0
with open("day1_1.txt", "r") as f:
    for line in f:
        fuel += ((int(line) // 3) - 2)
        

print(fuel)



### day 2 part 2

def get_fuel(mass):
    print('mass: ', mass)

    fuel = (mass // 3) - 2
    if fuel <= 0:
        print("fuel: hope")
        return 0
    else:
        print('fuel: ', fuel)
        return fuel + get_fuel(fuel)
    



fuel = 0
with open("day1_1.txt", "r") as f:
    for line in f:
        init_mass = int(line)
        
        fuel += get_fuel(init_mass)

print(fuel)

