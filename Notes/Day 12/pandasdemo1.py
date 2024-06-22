# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 18:56:35 2021

@author: anilk
"""

import pandas as pd
df=pd.read_table('http://bit.ly/chiporders')

print(df.shape)
s=df['item_name'] #print column in Series format
print(type(s))

s=df[['item_name']] #print item_name column in DataFrame format
print(type(s))
print(df.columns)  #print all column names

print(df.head())  #prints first 5 lines
print(df.tail())  #prints last 5 lines

print(df.head(12))  #prints first 12 lines
print(df.tail(7))  #prints last 7 lines

print(df.iloc[0:4,1:3])  #to retrieve data by integer position

#it will exclude 7th row
#display rows from 0-6 and columns 1 onward all
print(df.iloc[0:7,1:])

#store all columns except the last column
df1=df.iloc[:,:-1]
#It will not exclude 6 th row
print(df.loc[2:6,['order_id','item_name']]) #this is by location it will include 6 th row also


print(df.mean(axis=0))  #to calculate columnwise mean
print(df.mean(axis=1))  #to calculate rowwise mean
print(df.std())
print(df.median())
print(df.max())
print(df.describe()) #all statistical measures for all integer columns
print(df.info())  #how many not null values and data type of all columns

df['item_price1']=df['item_price'].map(lambda x:x.replace('$','0')) #to replace $ with 0

df['item_price2']=df['item_price1'].astype('float')  #to convert from object data type to int
df['discounted_price']=df['item_price2']*0.85  #add new column

df.pop('choice_description') # to delete the column

index_nm=df[df['discounted_price']>3].index

df.drop(index_nm,inplace=True)  #drop all rows with discounted_price > 3 and ovewrite the original frame
df.drop([2,3,4],axis=0,inplace=True) 

pd.unique(df['item_price'])
pd.value_counts(df['item_price']) #frequency of each distinct value





