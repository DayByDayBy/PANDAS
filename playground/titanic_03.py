import pandas as pd

titanic = pd.read_csv('data/titanic.csv')

# print(titanic.head())

ages = titanic["Age"]
print(ages.head(), '\n')
print(titanic["Age"].shape, '\n')
print(type(titanic["Age"]), '\n')

fares = titanic["Fare"]
print(fares.head(), '\n')
print(type(titanic["Fare"]), '\n')

age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())

age_sex_fare = titanic[["Age", "Sex", "Fare"]]
print(age_sex_fare.tail())

print(max(ages))





