# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:46:41 2023

@author: anilk
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("student.xlsx")
print(df)

print(df.info())
print(df['marks'].sum())
print(df['marks'].mean())
print(df.describe())
x=df['name']
y=df['marks']
plt.bar(x,y,color="green")
plt.title("this student marks plot\n studentvs marks")
plt.xlabel("name")
plt.ylabel("marks")
plt.show()
