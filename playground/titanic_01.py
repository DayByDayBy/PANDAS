import pandas as pd  # pd is the agreed abbreviation, may as well use it

df = pd.DataFrame(     # creating a pandas table
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "D'Cap, Master Leon",
        ],
        "Age": [22, 35, 58, 17],
        "Sex": ["male", "male", "female", "male"],
    }
        
)

print(df)  # printing the table out 
print(df["Age"]) # printing out the named column, ie the "Age" series in pandas temrinology 

ages = df["Age"] # assigning series as a variable
print(ages) 

ages = pd.Series([31, 44, 69], name="Age") # setting up a new series
print(ages)


print(max(df["Age"]))    # equiv, all give max age,
print(max(ages))         # but the 'ages' variable is reassigned above
print(ages.max())        # so only the first one is accessing the original table

print(df.describe())     # describe, a numerical method, so ignores textual


# ********* stuff to remember ***********
# 
# Import the package, aka import pandas as pd
# A table of data is stored as a pandas DataFrame
# Each column in a DataFrame is a Series
# You can do things by applying a method to a DataFrame or Series


