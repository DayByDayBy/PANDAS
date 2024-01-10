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

