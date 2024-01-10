import pandas as pd 

titanic = pd.read_csv("data/titanic.csv")
pd.set_option('display.max_rows', titanic.shape[0])
survivors = titanic[titanic["Survived"] == 1]

age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names)

# rock_and_roll_age_of_death_names = titanic.loc[titanic["Age"] == 27, "Name"]
# print(rocknroll_age_of_death_names, '\n', rocknroll_age_of_death_names.shape[0])

# rocknroll_age_of_death_survivors = survivors.loc[survivors["Age"] == 27, "Name"]
# print(rocknroll_age_of_death_survivors, '\n', rocknroll_age_of_death_survivors.shape[0])

print(titanic.iloc[9:25, 2:5])      # loc and iloc are similar, but iloc is purely integer-based indexing, 
                                    # and here is finding rows and columns by index number
     
rocknroll_age_of_death_names = titanic.loc[titanic["Age"] == 27]
print(rocknroll_age_of_death_names.iloc[0:18, 1:5])
