# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:35:06 2019

@author: hoskim1
"""

#p1

input_range = "359285-820401"
input_range_num = [int(val) for val in input_range.split('-')]

def count_criteria(low, high):

    match_list = []
    
    for num in range(low, high + 1): #+1 for inclusivity
        
        ascending = True #want all

        num_counter = []
        for idx, digit in enumerate(str(num)):
            
            if idx + 1 != len(str(num)):
                
                #check ascending
                ascending = ascending & (digit <= str(num)[idx + 1])
#                print('num: ', num, ' match_ascend: ', ascending)
                

            if ascending:
               if idx == 0:
                    num_counter.append([digit, 1])
               elif digit == num_counter[-1][0]:
                    num_counter[-1][1] += 1
               else:
                    num_counter.append([digit, 1])
#        print(num_counter)
        n_count = [i[1] for i in num_counter]
        n_count = [i for i in n_count if i > 1]
        pass_value = 2 in n_count #more than for part 1
#        print(pass_value)
        if pass_value and ascending:
            match_list.append(num)
                    
        
    return match_list


def print_count(low, high):
    
    print(len(count_criteria(low,high)))
    

test = (2211, 2233)

print_count(test[0], test[1])

sub_split_test = count_criteria(input_range_num[0], input_range_num[1])

print(len(sub_split_test))


            
            
    
    
    
    
    
    
    
    
    
    
    
    







