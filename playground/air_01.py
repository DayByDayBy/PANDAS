import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv(                                        
    'data/air_quality_no2.csv',                   # importing the file
    index_col=0,                                  # and making 'datetime' into the index
    parse_dates=True)                             # and parsing the dates as 'Timestamp' objects 

# print(air_quality)
# air_quality.plot()                          # default plot creates one line per numeric column
# plt.show()                                  # displays plot

# air_quality["station_paris"].plot()         # plots named column only (plot works on Series or DataFrame)
# plt.show()

# air_quality.plot.scatter(                   # scatter plot
#     x="station_london",                     # x declared as london column
#     y="station_paris",                      # y declared as paris column
#     alpha=0.5)                              # alpha transparency
# plt.show()

print(
    [
    method_name
    for method_name in dir(air_quality.plot)        # printing out a list of methods
    if not method_name.startswith("_")
    ]
)

# ['area', 'bar', 'barh', 'box', 'density','hexbin', 'hist', 'kde', 'line', 'pie', 'scatter']

air_quality.plot.box()                                            # box plot 
plt.show()                          
air_quality.plot.kde()                                            # kernel density estimate plot
plt.show()

axs = air_quality.plot.area(figsize = (12, 4), subplots=True)     # subplotting, ie one per column
plt.show()


fig, axs = plt.subplots(figsize=(12, 4))        # creates empty Matplotlib Figure and Axes
air_quality.plot.area(ax=axs)                   # using pandas to put the area plot on the prepared Figure/Axes
axs.set_ylabel("NO$_2$ concentration")          # Matplotlib customization 
fig.savefig("no2_concentrations.png")           # save the Figure/Axes using existing Matplotlib method.
plt.show()                                      # show the plot


# __________ stuff ___________
# '.plot.*' methods are applicable on both Series and DataFrames.
# by default, each of the columns is plotted as a different element (line, boxplot,…).
# any plot created by pandas is a Matplotlib object.


