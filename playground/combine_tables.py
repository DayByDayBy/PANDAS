import pandas as pd

pm25 = pd.read_csv('data/air_quality_pm25_long.csv')
no2 = pd.read_csv('data/air_quality_no2.csv')

print(pm25, '\n', no2, '\n')