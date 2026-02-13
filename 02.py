import pandas as pd

"""Before manipulation
1 - how big is dataset
2 - what are the names of columns"""


df = pd.read_json("data.json")
# print(df)
# print(f"Shape: {df.shape}") #it will show (row,column) wise
# print(f"Column :{df.columns}") #Names of columns



#Steps
#1 - select the specific column
#2- filter rows
#3 - combine multiple conditions (if > , date etc)
#4 - Square brackets and boolean conditions





df = pd.read_json("data.json")
dff = pd.DataFrame(df)
print(df)


#if you work on single columns
print("Single column series")
name = df['Name']
# print(name)



#When working with 2 columns
# print("\nMultiple column series")
name2 = df[['Name', 'Price']]
# print(name2)


#filtering the rows
#Single conditions
df = pd.read_json("data.json")
Higher_prices = df[df["Price"] > 120]
# print(Higher_prices)


#Multiple COndtion on rows
filtered = df[(df['Stock'] >40 ) & (df['Price'] > 10)]
# print(filtered)



#using OR (if even 1 data is correct it print)
filtered_or = df[(df['Stock'] >100 ) | (df['Price'] > 500)]
print(filtered_or)



