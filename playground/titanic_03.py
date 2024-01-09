import pandas as pd

titanic = pd.read_csv('data/titanic.csv')       # grabbing data, making into pd dataframe
pd.set_option('display.max_rows', 891)

# print(titanic)                                # checking intake of file 

ages = titanic["Age"]                           # declaring variable for series
# print(ages.head(), '\n')                      # checking vairable via print of head/first five lines
# print(titanic["Age"].shape, '\n')             # getting shape of 'Age' series
# print(type(titanic["Age"]), '\n')             # printing series type check 

fares = titanic["Fare"]                         # declaring variable for series
# print(fares.head(), '\n')                     # checking vairable via print of head/first five lines
# print(type(titanic["Fare"]), '\n')            # printing series type check 

age_sex = titanic[["Age", "Sex"]]               # declaring new variable, a dataframe containing two series from larger table 
# print(age_sex.head())

age_sex_fare = titanic[["Age", "Sex", "Fare"]]  # declaring variable, df cont three series. (inner sq-brackets define list, outer select series) ) 
# print(age_sex_fare)                             # checking variable via print
# print(type(age_sex_fare))                       # printing dataframe type check 

# print(max(ages))

above_35 = titanic[titanic["Age"] > 35]         # declaring 35+ age table  - without the outer sq-brackets would be a boolean check, returning df of indexed true/false
# print(above_35, '\n', 'shape of table: ', above_35.shape)

class_1 = titanic[titanic["Pclass"] == 1]                                   # first class variable declaration
# print(class_1, '\n', 'shape of table: ', class_1.shape)
class_23 = titanic[titanic["Pclass"].isin([2, 3])]                          # second or third class declaration 
print(class_23, '\n', 'shape of table: ', class_23.shape)
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]     # second or third class declaration
# print(class_23)

# _________________________________________

# practicing with some analysis,
# ratio of ticket-class to likelihood of survival

survived = titanic[titanic["Survived"] == 1]
survival_ratio = survived.shape[0] / titanic.shape[0]
first_class_survived = titanic[(titanic["Survived"] == 1) & (titanic["Pclass"] == 1)] 
first_class_survival_ratio = first_class_survived.shape[0] / class_1.shape[0]

second_survived = titanic[titanic["Survived"] == 1 & (titanic["Pclass"] == 2)]
third_survived = titanic[titanic["Survived"] == 1 & (titanic["Pclass"] == 3)]
second_third_survived = titanic[(titanic["Survived"] == 1) & (titanic["Pclass"].isin([2, 3]))]
second_third_survival_ratio = second_third_survived.shape[0] / class_23.shape[0]

print('\n', 'survivors: ', survived.shape[0], '\n', '1st class survivors: ', first_class_survived.shape[0], '\n', '2nd/3rd class survivors: ', second_third_survived.shape[0])
print('\n', 'survival ratio: ', survival_ratio, '\n', '1st class survival ratio; ', first_class_survival_ratio, '\n', '2nd/3rd class survival ratio; ', second_third_survival_ratio)

first_versus_second_third = second_third_survival_ratio / first_class_survival_ratio

print('2/3rd vs 1st: ', first_versus_second_third)

# the dataset suggests you were twice as likely to die if you're not in first, 
# but it's worth considering that the data set is only 891/2224 passengers, and
# while the dataset survival ratio is 0.3838383838383838, the overall survival ratio is 0.3471223022
# given the tendency of investigators to prioritise those passengers, 
# upper class is overrepresented:
#   of the 325 aboard, 219 are in the dataset
#   of the other 1899 passengers, 675 are on the list 
# that means that 0.6738461538 of the first class are included, whereas 0.355450237 of the others are in the data
# 
# the broken dataset can be supported by external information, but some data is simply missing, and/or unknowable



# creep-check, for some more practice, 
# inpsired by reading wikipedia and finding out about 
# the 47yo plutocrat divorcee colonel astor and his already-pregnant, 18yo, second wife:

male = titanic[(titanic["Sex"] == "male")]
female = titanic[(titanic["Sex"] == "female")]
adults_under_22 = titanic[(titanic["Age"] < 22) & (titanic["Age"] > 17)]
over_45 = titanic[(titanic["Age"] > 45)]
male_under_22 = titanic[(titanic["Sex"] == "male") & (titanic["Age"] < 22)]
female_under_22 = titanic[(titanic["Sex"] == "female") & (titanic["Age"] < 22)]
male_45_plus = titanic[(titanic["Sex"] == "male") & (titanic["Age"] >= 45)]
female_45_plus = titanic[(titanic["Sex"] == "female") & (titanic["Age"] >= 45)]

# print('women: ', female.shape[0], '\n', 'men: ', male.shape[0])
# print('18-21: ', adults_under_22.shape[0], '\n', 'over 45: ', over_45.shape[0])
# print('\n\n', 'women 18-21: ', female_under_22.shape[0], '\n', 'men over 45: ', male_45_plus.shape[0], '\n', 'female over 45: ', female_45_plus.shape[0], '\n', 'men 18-21: ', male_under_22.shape[0], '\n')

# print(male_45_plus, '\n', female_under_22, '\n', male_45_plus.shape, '\n', female_under_22.shape)  

# young_ratio_male = male_under_22.shape[0] / male.shape[0]
# young_ratio_female = female_under_22.shape[0] / female.shape[0]
# print('m: ', young_ratio_male, 'f: ', young_ratio_female)

# older_ratio_male = male_45_plus.shape[0] / male.shape[0]
# older_ratio_female = female_45_plus.shape[0] / female.shape[0]
# print('m: ', older_ratio_male, 'f: ', older_ratio_female)

# youth ratios are 0.20797 for male, 0.26751 for female
# older ratios are 0.13692 for male, 0.11465 for female

# male_under_22_first = titanic[(titanic["Age"] < 22) & (titanic["Age"] > 17) & (titanic["Sex"] == "male") & (titanic["Pclass"] == 1)]
# female_under_22_first = titanic[(titanic["Age"] < 22) & (titanic["Age"] > 17) & (titanic["Sex"] == "female") & (titanic["Pclass"] == 1)]
                
# print(male_under_22_first)
# print(female_under_22_first)

# first_ratios = {'m': male_under_22_first.shape[0] / male.shape[0], 'f': female_under_22_first.shape[0] / female.shape[0]}
# print(first_ratios)
# m_f_ratio = first_ratios["m"] / first_ratios["f"]
# print(m_f_ratio)

# 4 young men in first, 8 women
# a ratio of 0.006932409012131715 vs 0.025477707006369428
# an m/f ratio of .272















