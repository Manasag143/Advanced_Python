# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:56:56 2023

@author: anilk
"""
import pandas as pd
df=pd.read_table('http://bit.ly/movieusers',sep="|",header=None);
df.columns=['userid','age','gender','profile','views']
df['views'].replace(to_replace='[a-zA-Z]{1,}', regex=True, value=0,inplace=True)
df['views1']=df['views'].astype(int);
df.views1.mean()

