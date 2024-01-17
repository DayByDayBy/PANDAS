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

#matplotlib labelling:
plt.xlabel("hour of the day"); 
plt.ylabel("$NO_2 (µg/m^3)$");

# plt.show()

no_2 = air_quality.pivot(index="datetime", columns="location", values="value")   # pivot to make the table show locations as columns for comparison
# print(no_2)
# print(air_quality)


print(no_2.index.year, no_2.index.weekday)
# this shows the available indexables for each object:
        # Index([2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
        #        ...
        #        2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019],
        #       dtype='int32', name='datetime', length=1033) Index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        #        ...
        #        3, 3, 3, 3, 3, 3, 3, 3, 3, 4],
        #       dtype='int32', name='datetime', length=1033)
        
        
no_2["2019-05-20":"2019-05-21"].plot()  # plotting a sepcifc date range via the datetime index
# plt.show() 

monthly_max = no_2.resample("M").max()   # monthly max in the still-pivoted table, ie monthly max per location, for any months in data (here there are two)
print(monthly_max)

#  _aliases:
    # B - business day frequency
    # C - custom business day frequency
    # D - calendar day frequency
    # W - weekly frequency
    # M - month end frequency
    # SM - semi-month end frequency (15th and end of month)
    # BM - business month end frequency
    # CBM - custom business month end frequency
    # MS - month start frequency
    # SMS - semi-month start frequency (1st and 15th)
    # BMS - business month start frequency
    # CBMS - custom business month start frequency
    # Q - quarter end frequency
    # BQ - business quarter end frequency
    # QS - quarter start frequency
    # BQS - business quarter start frequency
    # A, Y - year end frequency
    # BA, BY - business year end frequency
    # AS, YS - year start frequency
    # BAS, BYS - business year start frequency
    # BH - business hour frequency
    # H - hourly frequency
    # T, min - minutely frequency
    # S - secondly frequency
    # L, m - milliseconds
    # U, us - microseconds
    # N - nanoseconds

print(monthly_max.index.freq)   # shows the frequency of the monthly max defined above

no_2.resample("D").mean().plot(style="-o", figsize=(10, 5));
plt.show()




______________________________stuff______________________________

        # valid date strings can be converted to datetime objects using to_datetime function or as part of read functions.
        # datetime objects in pandas support calculations, logical operations and convenient date-related properties using the dt accessor.
        # DatetimeIndex contains these date-related properties and supports convenient slicing.
        # resample() is a powerful method to change the frequency of a time series.