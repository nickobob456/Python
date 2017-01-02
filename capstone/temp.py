# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:06:38 2016

@author:
"""
import pandas as pd

Location = 'C:\Users\Nicholas\Documents\berkeley\Capstone\patents.csv'
lib = pd.read_csv(Location)


print len(lib) #prints number of rows

print lib.dtypes #datatypes in each column

#Sum of Patent Values
print lib['xi'].sum() 

#Sum of Patent Citations
print lib['ncites'].sum() 

#Most recent year
print max(lib['fdate']) #Fdate YEAR ERROR

#First year
print min(lib['idate']) #YEAR ERROR

#Most Valuable Patent
#MaxVal = lib['patnum'][lib['xi'] == lib['xi'].max()].values
#print MaxVal
#print lib['xi'].max() 

#Most Cited Patent
#maximum  = lib['ncites'].max()
#for i in range(len(lib['ncites'])):
#    if lib['ncites'][i] == maximum:
#        j = i
#print lib['patnum'][j]
#MaxCite = lib['patnum'][lib['ncites'] == lib['ncites'].max()].values
#print lib['patnum'][3110307]
#print MaxCite
#print lib['ncites'].max() 

#Mean, Variance, Std Dev of Citations
#print lib['ncites'].mean() 
#print lib['ncites'].std() 
#print lib['ncites'].var() 

#Mean, Variance, Std Dev of Value
#print lib['xi'].mean() 
#print lib['xi'].sum() / len(lib) #taking nan elements
#print lib['xi'].mean() 
#print lib['xi'].var() 
