import pandas as pd
import numpy as np
import haversine as hs


# def parse_data(file_name):


garmin_data = pd.read_csv(
    '../data/activities.csv',  
    parse_dates=True, infer_datetime_format=True)

print(garmin_data)