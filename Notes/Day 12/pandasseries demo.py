# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:23:04 2021

@author: anilk
"""

import numpy as np
import pandas as pd
print(np.random.randn(5))
s = pd.Series(np.random.randn(5), 
              index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s[s<1]) #filter series and display all values which are < 1
print(s[[4,3,1]])
print(s[['e','d','b']])
np.exp(s)



print(s)
print(s+s)
       # b-e   a-d
print(s[1:]+s[:-1])
print(s[:3])  #retrieve rows from 0 to 2
print(s['d']) #this will retrieve the row with index d
#print(s['f']) #it is Key error

d = {'b' : 1, 'a' : 0, 'c' : 2} #dictionary

s1=pd.Series(d) #keys will become index and values will become value
print(s1)

s1=pd.Series(5,index=[1,2,3]) #keys will become index and values will become value
print(s1)

s=pd.Series(['rainy','no rain','sunny'],
        index=['monday','tuesday','wednesday'])
print(s)
print(s['monday']) 











