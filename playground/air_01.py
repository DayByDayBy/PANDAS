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

air_quality.plot.box()
plt.show()
air_quality.plot.kde()
plt.show()