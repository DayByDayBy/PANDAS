import pandas as pd



titanic = pd.read_csv('data/titanic.csv')

# print(titanic.shape)

pd.set_option('display.max_rows', 891)
# pd.set_option('display.max_columns', 12)

print(titanic)

