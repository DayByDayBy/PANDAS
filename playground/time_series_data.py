import pandas as pd 
import matplotlib.pyplot as plt

air_quality = pd.read_csv("data/air_quality_no2_long.csv")
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
# print(air_quality.head())

# print(air_quality.city.unique())            # prints out cities, unique ie duolicates only once. does not sort)
print('\n')
# datetime objects:

air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])  
# print(air_quality["datetime"])

    #  applying the to_datetime function, 
    # pandas interprets the strings and 
    # convert these to datetime (i.e. datetime64[ns, UTC]) objects

        # see also pandas.Timestamp: 
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html#pandas.Timestamp



        # if datetime is a column in the data set: 
            # pd.read_csv("data/air_quality_no2_long.csv", parse_dates=["date.utc"])
        # this csv doesnt have that, without the conversion above (line 5)

# ----- usefulness of pandas.Timestamp --------------------------------
    # what is the start and end date of the time 
    # series data set we are working with?
print('\n')
print('\n', air_quality["datetime"].min(), '\n', air_quality["datetime"].max())
print('\n')

    # Using pandas.Timestamp for datetimes enables 
    # us to calculate with date information and make 
    # them comparable. Hence, we can use this to get 
    # the length of the time series:

print(air_quality["datetime"].max() - air_quality["datetime"].min())   # pandas.Timedelta object - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timedelta.html#pandas.Timedelta

    # see also 
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-overview

air_quality["month"] = air_quality["datetime"].dt.month   # new column for month of the measurement
# print(air_quality)
air_quality["weekday"] = air_quality["datetime"].dt.weekday   # new column for day of the week of the measurement
air_quality["quarter"] = air_quality["datetime"].dt.quarter   # new column for quarter of the measurement
# print(air_quality)

# print(air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean())

fig, axs = plt.subplots(figsize = (12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot = 0, ax=axs)      # averages for hours of the day plotted as barchart         

plt.show()
