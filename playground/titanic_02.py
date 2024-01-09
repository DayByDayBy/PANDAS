import pandas as pd

titanic = pd.read_csv('data/titanic.csv')

#  pandas supports different file formats/data sources 
#  (csv, excel, sql, json, parquet, …), each with the prefix 'read_*'

# print(titanic.shape)   # gets shape of  table, ie number of rows, columns

# pd.set_option('display.max_rows', 891)      # sets rows (used rows count from '.shape' above, ie all rows)
# pd.set_option('display.max_columns', 12)  # same idea, but for columns

print(titanic)              # prints table, defaulting to first/last 5; using 'set_option' size above will show all rows
# print(titanic.head(12))     # prints first 12 rows
# print(titanic.tail(9))      # prints last 9 rows
# print(titanic.dtypes)       # prints table of data types

# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index = False)  # creates an excel version of the table; false leaves out the index numbers
# titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")          # the inverse of the above 
# print(titanic)

print(titanic.info())




#   ********* stuff to remember ***********
# 
# getting data in from different file formats/data sources by 'read_*', eg 'read_excel'
# exporting data out is via 'to_*'
# head/tail/info methods and the dtypes attribute are convenient for a first check.