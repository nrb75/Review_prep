#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:08:34 2018

@author: natalie
"""

#find the max length of a substring without any repeating letters

s='abcabcbb'


def lenstring(s):
    substring=s[0]#start with first letter
    maxl=0
    #if first letter works, keep adding letters until we get repeat
    if len(s)>=1:
        for i in s[1:]:
            if i in substring:
                maxl=len(substring)
            if i not in substring:
                substring=substring+i
        print(maxl)
        
        
#what about other conditions, where the longest substring starts in the middle of the string?
def lenstring2(s):
    maxl=0
    n=len(s)
    longest=0
    for i in range(n):
        seen=set()
        for j in range(i,n): #keeps shifting over b/c i goes 1,2,3
            if s[j] in seen: break
            else:
                seen.add(s[j])
        longest=max(len(seen), longest)
    return(longest)
    
    if len(s)>=1:
        for i, j in s:
            
            
def lengths(self, word):
    n = len(word)
    longest = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if word[j] in seen: break
            seen.add(word[j])
        longest = max(len(seen), longest)
    return longest