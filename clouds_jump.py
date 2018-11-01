#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:35:52 2018

@author: natalie
"""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, id_list):
    jumps=0
    cloud_id=0
    while cloud_id<c-1:
        if cloud_id+2<c and id_list[cloud_id+2]==0:
            jumps+=1
            cloud_id=cloud_id+2
        else:
            jumps+=1
            cloud_id=cloud_id+1
    print(jumps)
    
    #cloud_id+1<c and id_list[cloud_id+1]==0:
            
            