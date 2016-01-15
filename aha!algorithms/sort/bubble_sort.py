'''
Created on 2016年1月13日
# encoding: utf-8
@author: tcliu
'''
from sort.random_list import RandomList
R = RandomList(5, 10)
lst = R.gen()

def bubble_sort(l = []):
    for i in range(len(l)):
        for j in range(len(l) - i -1):
            if l[j] > l[j + 1]:
                #(l[j + 1], i[j]) = (l[j], l[j + 1])
                t = l[j + 1]
                l[j+1] = l[j]
                l[j] = t
            else:
                continue   
    print(l)    
bubble_sort(lst)         