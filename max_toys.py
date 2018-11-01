#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:34:49 2018

@author: natalie
"""
#how many toys can he buy with a specific amount of money?
k= 30#total money he can spend on all the toys
prices=[2,3,11,7,17]#prices of individual toys
buy_toys=[]
for i in sorted_prices:
    if i <k and (i+sum(buy_toys))<=k and len(buy_toys)<=len(prices):
        buy_toys.append(i)
        num_toys=(len(buy_toys))
print(num_toys)