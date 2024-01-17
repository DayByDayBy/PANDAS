import pandas as pd
titanic = pd.read_csv('data/titanic.csv')  # declaring dataframe variable
titanic["Name"].str.lower()                # changing instances of 'Name' column to lowercase

titanic["Name"].str.split(',')             # splitting 'Name' string by comma, which falls between surname and forenames 

# eg:

titanic["Surname"] = titanic["Name"].str.split(',').str.get(0)  # creating new column for surname using above methodology - split creates list, get(0) grabs index 0 of that list 
print(titanic["Surname"])                                       # printing out all rows, surnames only

print(titanic["Name"].str.contains("Countess"))             # boolean 'does the name have countess' column
print(titanic[titanic["Name"].str.contains("Countess")])    # use that boolean to print only those where contains countess is true

# https://en.wikipedia.org/wiki/Noël_Leslie,_Countess_of_Rothes


# str methods support regex, can be combined with other methods:

print(titanic["Name"].str.len())
print(titanic["Name"].str.len().idxmax())
print(titanic.loc[titanic["Name"].str.len().idxmax(), "Name"])

# Penasco y Castellana, Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo)

titanic["Sex_short"] = titanic["Sex"].replace({"male":"M", "female":"F"})
print(titanic["Sex_short"])

#   see also
#         titanic["Sex_short"] = titanic["Sex"].str.replace("female", "F")
#         titanic["Sex_short"] = titanic["Sex_short"].str.replace("male", "M")

# more useful for one-off replacements, otherwise the dictionary is clearly neater



# _______________ stuff___________________________________
        # string methods are available using the str accessor.
        # string methods work element-wise and can be used for conditional indexing.
        # replace method is a convenient method to convert values according to a given dictionary, can also be used individually 