import pandas as pd
air_quality = pd.read_csv(
    'data/air_quality_no2.csv', 
    index_col=0, 
    parse_dates=True)
# print(air_quality)

air_quality[
    "london_mg_per_cubic"
    ] = air_quality[
        "station_london"
        ] * 1.882   
# print(air_quality)

# this calc is based on assumption of temperature of 
# 25 degrees Celsius and pressure of 1013 hPa, 
# for which the conversion factor is 1.882 
# (info given by pydata site, not sure what the maths behind that is)

# also, calculation of the values is done element-wise; 
# all values in the given column are multiplied by the value 1.882 at once, 
# no need to use a loop to iterate each of the rows


air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)

# making a ratio, but obvs all basic operators work
# pd.DataFrame.apply() can also be used for more formulae 
# (see https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)

print(air_quality)

air_quality_renamed = air_quality.rename(           # rename() can be used for both row labels and column labels
    columns = {                                     # use dictionary with the keys of current names/the values of new names to update the corresponding
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

print(air_quality_renamed)

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)  # same idea, but mapping function, ie all str lower case
print(air_quality_renamed.head())




# ___________stuff__________
# create new column by assigning output to  DataFrame with a new column name in between the [].
# operations are element-wise, no need to loop
# use rename with dictionary or function to rename row labels or column names