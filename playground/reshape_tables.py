import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('data/titanic.csv')
air_quality = pd.read_csv('data/air_quality_long.csv', index_col="date.utc", parse_dates=True)

# print(titanic.head, air_quality.head)

# ________________________________________________________________



# sort table rows:

# print(titanic.sort_values(by="Age").head())                                   # printing youngest five rows
print(titanic.sort_values (by=['Pclass', 'Age'], ascending = False).head())     # descending order via 'ascending = False'. can do tail, but that gives table end, ie the NaN value rows

# prints: 
            #      PassengerId  Survived  Pclass                       Name     Sex   Age  SibSp  Parch  Ticket    Fare Cabin Embarked
            # 851          852         0       3        Svensson, Mr. Johan    male  74.0      0      0  347060  7.7750   NaN        S
            # 116          117         0       3       Connors, Mr. Patrick    male  70.5      0      0  370369  7.7500   NaN        Q
            # 280          281         0       3           Duane, Mr. Frank    male  65.0      0      0  336439  7.7500   NaN        Q
            # 483          484         1       3     Turkula, Mrs. (Hedwig)  female  63.0      0      0    4134  9.5875   NaN        S
            # 326          327         0       3  Nysveen, Mr. Johan Hansen    male  61.0      0      0  345364  6.2375   NaN        S

#  using DataFrame.sort_values(), the rows in the table are sorted according 
#  to the defined column(s), and the index will follow the row order

print('\n\n\n')

# filter for no2:
no2 = air_quality[air_quality["parameter"] == "no2"]
print(no2)
print('\n\n\n')

# filter for 2 different measurements (head(2)) for each location (groupby()):
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)
print('\n\n\n')
# prints out:
            #                                 city country            location parameter  value   unit
            # date.utc                                                                                
            # 2019-04-09 01:00:00+00:00  Antwerpen      BE             BETR801       no2   22.5  µg/m³
            # 2019-04-09 01:00:00+00:00      Paris      FR             FR04014       no2   24.4  µg/m³
            # 2019-04-09 02:00:00+00:00     London      GB  London Westminster       no2   67.0  µg/m³
            # 2019-04-09 02:00:00+00:00  Antwerpen      BE             BETR801       no2   53.5  µg/m³
            # 2019-04-09 02:00:00+00:00      Paris      FR             FR04014       no2   27.4  µg/m³
            # 2019-04-09 03:00:00+00:00     London      GB  London Westminster       no2   67.0  µg/m³
            

print(no2_subset.pivot(columns="location", values="value"))                     # pivot() function is reshaping the data: a single value for each index/column combination is required
print('\n\n\n')

# prints out:


            # location                   BETR801  FR04014  London Westminster
            # date.utc                                                       
            # 2019-04-09 01:00:00+00:00     22.5     24.4                 NaN
            # 2019-04-09 02:00:00+00:00     53.5     27.4                67.0
            # 2019-04-09 03:00:00+00:00      NaN      NaN                67.0
            
            
print(no2.head())
print('\n\n\n')


            #                             city country location parameter  value   unit
            # date.utc                                                                 
            # 2019-06-21 00:00:00+00:00  Paris      FR  FR04014       no2   20.0  µg/m³
            # 2019-06-20 23:00:00+00:00  Paris      FR  FR04014       no2   21.8  µg/m³
            # 2019-06-20 22:00:00+00:00  Paris      FR  FR04014       no2   26.5  µg/m³
            # 2019-06-20 21:00:00+00:00  Paris      FR  FR04014       no2   24.9  µg/m³
            # 2019-06-20 20:00:00+00:00  Paris      FR  FR04014       no2   21.4  µg/m³


no2.pivot(columns="location", values="value").plot()
plt.show()



