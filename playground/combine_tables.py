import pandas as pd


no2_long = pd.read_csv('data/air_quality_no2_long.csv', parse_dates=True)
no2_long = no2_long[["date.utc", "location", "parameter", "value"]]
pm25_long = pd.read_csv('data/air_quality_pm25_long.csv', parse_dates=True)
pm25_long = pm25_long[["date.utc", "location", "parameter", "value"]]


print(no2_long.head, pm25_long.head)


# ______ combine:

air_quality = pd.concat([pm25_long, no2_long], axis = 0)
print(air_quality)


# check sizes to confirm concatenation:

print('Shape of the ``pm25_long`` table: ', pm25_long.shape)
print('Shaper of the ``no2`` table: ', no2_long.shape)
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)

air_quality = air_quality.sort_values("date.utc")       # arranged by date, so pm25 and no2 values for each date are together
print(air_quality.head)

air_quality = pd.concat([pm25_long, no2_long], keys=["PM25", "NO2"])    # arranged into two dataframes within the one - head gives two batches of 5, rather than one
print(air_quality.head)

# the parameter column provided by the data 
# ensures that each of the original tables 
# can be identified. This is not always the case. 
# The concat function provides a convenient solution 
# with the keys argument, adding an 
# additional (hierarchical) row index. For example:

# info:
        # Hierarchical indexing or MultiIndex 
        # is an advanced and powerful pandas 
        # feature to analyze higher dimensional data.

        # multi-indexing is out of scope 
        # for this pandas intro. For the 
        # moment, remember that the function reset_index 
        # can be used to convert any level of an index to a 
        # column, e.g. air_quality.reset_index(level=0)
