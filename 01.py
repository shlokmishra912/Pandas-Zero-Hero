#Data maipulation
# changing organizing ,preparing to make it useful to understand (To clean , transform)
#Data Analysis
# Extracting patterns and trend and insights from data to solve problem (to answer the question of find the trend)


#Pandas
# Pandas is library designed for dark manipulation and data analysis

"""Series
a series is a one-dimensional labeled array that can hold any data type ,int,floats,string, or even python objects
nique labeled which called index

Data frame
Two-dimensional (Row and Column) same as SQL and Excel"""

import pandas as pd


# (for error
# Explicitly set encoding
"""df_json = pd.read_json("products.json", encoding="utf-8")
df_json = pd.read_json("products.json", encoding="latin-1")

"""
df = pd.read_json("data.json")
# print(df)





## steps
"""1) Understanding the data set ,(Row,(columns) shape of data
2) identify the problems (error ,etc)
3) plan next step"""



#Preview of data
#head(as default) < it show 5 top data if(head(n)) then 1 ,(10) for ten line data
#tail() same as ^
df = pd.read_json("data.json")

print("Display 10 rows of first")
# print(df.head(10))   #only int value is accepted

print("Display 10 rows of last")
# print(df.tail(10))





#Understanding of data
print("Display of info ")
# print(df.info())
#it will show (size of file), (Index ,Columns) ,data type like (int64, object)
print(df.describe())
#it give value (mean , max ,min ,max ,if count == 8,8 means no value error)



#Std (Standard Daviation) (small std)
age = [20,25,26,29,30] [30] the difference in age is mminimal so small std


#Large std
a = [100,300,500,600,300] the difference are 100 - 200
#to maintain consistency  (mean if std is large like 20 for age it means gap are higher , same for salary)



ab = [10,12,13,15,30,40,53,62]
means 25% = [10,12,13] #who are bottom 25%
means of 50% = [15,30] #they stand at middle
 means of 75% =[40,53,62] # mean top 25% of the Data













