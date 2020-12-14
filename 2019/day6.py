# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 08:55:58 2019

@author: hoskim1
"""

orb_dict = {}
with open("day6.txt", "r") as f:
    for line in f:
        row = line.split(')')
        orb_dict[row[1].rstrip()] = row[0]
    

steps = 0

for key in orb_dict.keys():
    search_key = key
    chain = True
    while(chain == True):
#        print(search_key)
        if orb_dict[search_key] in orb_dict:
#            print('orbits ', orb_dict[search_key])
            steps += 1
            search_key = orb_dict[search_key]
            
        else:
#            print("last body")
            steps += 1
            chain = False
            
print(steps)


you = "YOU"
san = "SAN"

orbit_list_you = []
orbit_list_san = []

chain = True
search_key = you
while(chain == True):
    print(search_key)
    if orb_dict[search_key] in orb_dict:

        orbit_list_you.append(orb_dict[search_key])
        search_key = orb_dict[search_key]
    else:
        orbit_list_you.append(orb_dict[search_key])
        chain = False

chain = True
search_key = san
while(chain == True):
    if orb_dict[search_key] in orb_dict:
        orbit_list_san.append(orb_dict[search_key])
        search_key = orb_dict[search_key]
    else:
        orbit_list_san.append(orb_dict[search_key])
        chain = False
    
in_both = set(orbit_list_san) & set(orbit_list_you)

common_chain = len(in_both) 

movement =  len(orbit_list_san) + len (orbit_list_you) - 2 * common_chain

print(movement)




    
    
    