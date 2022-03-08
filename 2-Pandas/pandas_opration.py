"""
Pandas code

"""
import pandas as pd

"""
 Series
 
""" 
# Diffrence with Series and array is series also  have index or lable or name to access the
# the data

age = pd.Series([10,20,30,40],index=['age1','age2','age3','age4'])

# by default index is none. or if you not give it is preceding numbers start from
# zero .It can also string

# filter the series

filtered_age = age[age > 20]

# all value of the series

age_values = age.values

# all index 

age_indexs = age.index


# Rename indexes or reintialize 

age.index = ['A1','A2','A3','A4']

"""
Data Frame

"""
import numpy as np

array = np.array([[20,9,10],[30,7,6],[40,5,3],[27,6,8]])

# cahng nupy arry to dataframe

np_df = pd.DataFrame(array)

# renameing  the index

df = pd.DataFrame(array, index=['s1','s2','s3','s4'])

# rename the columns also

df = pd.DataFrame(array,index=['s1','s2','s3','s4'],columns=['Age','Grade1','Grade2'])

# adding one column

df['Grade3'] = [4,9,7,9]
  

"""

loc and iloc

"""

# loc use on lable or index 
# iloc genrally use similer to python indexing or intiger based data acesss

df.loc['s2']
df.loc[['s1','s2']]
df.loc[['s1','s2'],'Age']
df.loc[['s1','s2'],:]

# iloc
# 2nd rwo and 3rd column
df.iloc[1][2]
#or 
df.iloc[1,2]
# all data
df.iloc[::]

df.iloc[0:2,1:3]
df.iloc[:,0]










