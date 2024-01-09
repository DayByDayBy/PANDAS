import pandas as pd

titanic = pd.read_csv('data/titanic.csv')       # grabbing data, making into pd dataframe

# print(titanic.head())                         # checking intake of file 

ages = titanic["Age"]                           # declaring variable for series
# print(ages.head(), '\n')                      # checking vairable via print of head/first five lines
# print(titanic["Age"].shape, '\n')             # getting shape of 'Age' series
# print(type(titanic["Age"]), '\n')             # printing series type check 

fares = titanic["Fare"]                         # declaring variable for series
# print(fares.head(), '\n')                     # checking vairable via print of head/first five lines
# print(type(titanic["Fare"]), '\n')            # printing series type check 

age_sex = titanic[["Age", "Sex"]]               # declaring new variable, a dataframe containing two series from larger table 
# print(age_sex.head())

age_sex_fare = titanic[["Age", "Sex", "Fare"]]  # declaring new variable, a dataframe containing three series from larger table 
print(age_sex_fare)                             # checking variable via print
print(type(age_sex_fare))                       # printing dataframe type check 

# print(max(ages))






