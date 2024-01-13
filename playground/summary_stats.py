import pandas as pd

titanic = pd.read_csv(
    'data/titanic.csv')

# print(titanic)

print('mean age: ', titanic["Age"].mean())

# such operations exclude missing data and operate across rows by default

print(titanic[["Age", "Fare"]].median())

# multi column (note list brackets) returns dataframe

print(titanic[["Age", "Fare"]].describe())

#  describes named rows - count of non-missing data, etc (notice that not all passengers ages were recorded, all passenger fares _were_ recorded)

# specific stats can be chosen, rather than 'describe()' defaults:

print(
    titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)
)

# side note - printing in-script like this is feeling more and more clumsy, may make a swicth to jupyter. 
# def will if i do another pass over the docs; not sure how useful the script-syle 
# approach really is where there isnt any real engineering being done 


print(titanic[["Sex", "Age", "Fare"]].groupby("Sex").mean())    # averages ages and fares by sex


# on average men were older, women had more expensive tickets:

#    Sex        Age       Fare                      
# female  27.915709  44.479818
# male    30.726645  25.523893



# Calculating a given statistic (e.g. mean age) for each category in a column 
# (e.g. male/female in the Sex column) is a common pattern. 
# The groupby method is used to support this type of operations. 
# This fits in the more general split-apply-combine pattern:
        # Split the data into groups
        # Apply a function to each group independently
        # Combine the results into a data structure
        # The apply and combine steps are typically done together in pandas.




print(titanic.groupby("Sex").mean(numeric_only=True))


# this returns averages, but obvs some don't really make data-sense. 
# pclass, for example:

    # Sex     PassengerId  Survived    Pclass        Age     SibSp     Parch       Fare                                                                         
    # female   431.028662  0.742038  2.159236  27.915709  0.694268  0.649682  44.479818
    # male     454.147314  0.188908  2.389948  30.726645  0.429809  0.235702  25.523893



# more compact syntax that gives much the same data as a few lines above, albeit with added data instead of the age header:

print(titanic.groupby("Sex")["Age"].mean())   

# prints out:

        # Sex
        # female    27.915709
        # male      30.726645
        # Name: Age, dtype: float64
        
        
# earlier version was:

print(titanic[["Sex", "Age"]].groupby("Sex").mean()) 

# which prints out:

        #               Age
        # Sex              
        # female  27.915709
        # male    30.726645


# ___________________________________________________________________

# categorical:



print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

# prints out:

            # Sex     Pclass
            # female  1         106.125798
            #         2          21.970121
            #         3          16.118810
            # male    1          67.226127
            #         2          19.741782
            #         3          12.661633
            # 
            # Name: Fare, dtype: float64
            
            
# grouping can be done by multiple columns at the same time, 
# just provide the column names as a list to the groupby() method.



print(titanic.groupby(["Sex", "Age"])["Fare"].mean())

# this is less usueful, as it prints out the average far for each age, 
# and the ages are much more varied than classes; this prints out 145 rows 


# counting by category:


print(titanic["Pclass"].value_counts())
# this counts each differfent value for Pclass, ie 491, 216, and 184 (891 total)

print(titanic.groupby("Pclass")["Pclass"].count())
#  this does the same, but in order oof Pclass

# note - 'size()' can also be used, but this counts NaN values, 
# ie it counts the rows rather than data points, whereas 'count()' excludes missing values




#          ______________stuff________________

    # aggregation statistics can be calculated on entire columns or rows.
    # groupby provides the power of the split-apply-combine pattern.
    # value_counts is a convenient shortcut to count the number of entries in each category of a variable.