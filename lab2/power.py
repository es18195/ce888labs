# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:34:39 2019

@author: es18195
"""
from scipy import stats
import random

def power(sample1, sample2, reps, size, alpha): 
    times = 0
    for i in range(reps):
        for s in range(size):
            matrix1=random.choice(sample1)
            matrix2=random.choice(sample2)
            [x,p_value]=stats.ttest_ind(matrix1,matrix2)
            if p_value < (1-alpha): 
                times +=1 
            
    
    return times / reps
