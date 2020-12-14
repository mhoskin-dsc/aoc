# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:14:39 2019

@author: hoskim1
"""



def computer(data, input_instr):
    
    running = True
    
    index = 0
    while running == True:
        
        instruction = data[index]
        
        opcode = instruction[-2:]
        
        param = instruction[:-2]
        
        #make param work
        
        if opcode == 99:
            input('99 problems')
            return data
        elif opcode == 4:
            print('diagnostic code: ', data[index + 1])
        else:
            data = _eval_opcode(opcode, index, data, input_instr)
        
        
        index += _opcode_step(opcode)
        
    
    return data

    


def _eval_opcode(opcode, index, data):
    
    if opcode == 1:
        data[data[index + 3]] = data[data[index + 2]] + data[data[index + 1]]
    elif opcode == 2:
        data[data[index + 3]] = data[data[index + 2]] * data[data[index + 1]]
    
    return data

def _opcode_step(opcode):
    if opcode <= 2:
        return 4
    elif opcode <= 4:
        return 2
        
def read_data(data_address):
    with open(data_address, "r") as f:
        d = f.readline()
        data = d.split(",")
        data = [int(value) for value in data]
        
    return data

def correct_data(data, noun, verb):
    data[1] = noun
    data[2] = verb
    
    return data


input_instruction = 1
data_address = "day5_1.txt"
result = computer(read_data(data_address), input_instruction)
        





























