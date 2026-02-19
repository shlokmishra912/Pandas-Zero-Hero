import pandas as pd

#adding a new columns
df = pd.read_csv(r"C:\Users\Shlok\Downloads\Python and module\Pandas\Part 2\sample_pandas_dataset.csv", encoding="latin-1")
# print(df)
df['Bonus'] = df["Salary"] *0.2 #the new column "Bonus will add" (i just give logical syntax)
# print(df)


#using insert columns
df.insert(0,"Employee ID" ,[1,2,3,4,7,6,7,8,9,10]) #0 is idex of column so it mean 1at ,name ,assign value for name etc
# print(df)
#making new column at specific place we use insert



#Updating
#df.loc[row_index , "Column Name",] = new value
df = pd.read_csv(r"C:\Users\Shlok\Downloads\Python and module\Pandas\Part 2\sample_pandas_dataset.csv", encoding="latin-1")
df.loc[2,"Salary"] = 600200
# print(df)



#Increasing salary by 5%  (it update and adding add new column)
df["Salary"] = df["Salary"] * 1.05
# print(df)
#while single column use loc (but for whole df(name) = df(name) -100 )




#REmoving
df = pd.read_csv(r"C:\Users\Shlok\Downloads\Python and module\Pandas\Part 2\sample_pandas_dataset.csv", encoding="latin-1")
# print(df)
df.drop(columns= ["Joining_Date"] ,inplace=True)
#inplace means type  'True' will modify data , 'false = new data made , old keep as it is ,for multiple columns use ['','',]
print(df)



#Handling Misisng data


print(df.isnull().sum())
"""If there is True means the value is missing it isnull (else False all correct) 
for multiple we can use (.isnull().sum())"""



#DEleting directly
df.dropna(axis=0, inplace=True)
#Axis=0 means for row , and axis=1 for columns if you don't set axis it will automatically remove all Not a number  value

#filling value at missing value
df.fillna(0 ,implace=True) #Zero but for specific like age etc we can use mean
df['Salary'].fillna(df['Salary'].mean() ,inplace=True)



#Interpolation
#if (1,2,3,4,na,6,7) the na value will we 5 using interpolation (it estimate the value using many methods)
#Methods are (linear,polynimial,spline,time,index) use AI to find their use

df.interpolate(method="index", axis=0 ,implace=True)


df['Salary'] = df['Salary'].interpolate(method="index",implace=True) #for Name ,ID it did't work









