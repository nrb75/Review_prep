#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:33:15 2018

@author: natalie
"""

string = ' a,b,c,d \n 1,2,3,4 \n 1,0,1,0 \n 0,0,5,3 \n .5, -3, -3, 9   '


#Natalie's code

# rows=string.split('\n')

# row_list=[]
# for i in rows:
#   rowx=i.split(',')
#   row_list.append(rowx)
# print(row_list)

# key=[]
# for i in row_list:
#   keyx=i[2]
#   key.append(keyx)
#   key=sorted(key)
# print(key)
  
#remove spaces

row_list=string.strip() #removes spaces, still leaves  space in last entry of each item in the list
row_list=row_list.split('\n') #splits up entries by \n
row_list=[item.strip() for item in row_list]#remove the last extr space

#split each item in the list into its own column with individual entries of each 
df=[]
for item in row_list:
    df.append(item.split(','))
    
#make sure we don't sort by the header
dfhead=df[0]#pop pulls off the last thing, but we want the first row popped off, so use 0
df=df[1:]#remove the header

#now we want to sort by the 3rd column,
dfsorted=sorted(df, key=lambda x: x[2], reverse=False)

#add back in the header
df.insert(0,dfhead)#inserts the head object at position 0 and shifts everything else

##Vannia's code
df=[item.split(',') for item in row_list]

print(sorted(df,key=lambda x:x[2]))


class Solution:

    def df_transform(self,string):
        string=string.strip()
        string_1split=string.split('\n')
        rows=[row.split(',') for row in string_1split]
        header=rows.pop(0)
        return header,rows
    
def sortspecial(self,header,df):
    df_sorted=sorted(df,key=lambda x:x[2],reverse=False)
    return [header]+df_sorted



header,df=Solution().df_transform('a,b,c,d \n 1,2,3,4 \n 1,0,1,0 \n 0,0,5,3 \n .5, -3, -3, 9')


print(header,df)
'''
a b c d 

1 2 3 4

1 0 1 0 ...
'''