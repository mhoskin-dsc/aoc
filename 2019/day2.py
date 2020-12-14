# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:14:39 2019

@author: hoskim1
"""



def computer(data):
    indexes = list(range(len(data)))
    indexes_to_sample = indexes[::4]
    
    for index in indexes_to_sample:
        opcode = data[index]
        if opcode == 99:
            #escape!
            return data
        else:
            data = _eval_opcode(opcode, index, data)
        
    return data

def _eval_opcode(opcode, index, data):
    
    if opcode == 1:
        data[data[index + 3]] = data[data[index + 2]] + data[data[index + 1]]
    elif opcode == 2:
        data[data[index + 3]] = data[data[index + 2]] * data[data[index + 1]]
    
    return data
        
def read_data():
    with open("day2_1.txt", "r") as f:
        d = f.readline()
        data = d.split(",")
        data = [int(value) for value in data]
        
    return data

def correct_data(data, noun, verb):
    data[1] = noun
    data[2] = verb
    
    return data
    
test_data = [[[1,0,0,0,99],[2,0,0,0,99]],
             [[2,3,0,3,99],[2,3,0,6,99]],
             [[2,4,4,5,99,0],[2,4,4,5,99,9801]],
             [[1,1,1,4,99,5,6,0,99],[30,1,1,4,2,5,6,0,99]]]


for test in test_data:
    print(computer(test[0]) == test[1])
    
data = correct_data(read_data(), 12, 2)

output_data = computer(data)
print("ex 1:", output_data[0])


####


for n in range(0, 100):
    for v in range(0, 100):
        result = computer(correct_data(read_data(), n, v))[0]
        
        if result == 19690720:            
            print('n: ', n, ' v: ', v)
            print(100 * n + v)




























