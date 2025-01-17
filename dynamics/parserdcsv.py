import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
Takes the csv as generated by the test data and cleans it for usage in rolldownconverter.py
"""
def clean(file, windspeed = 0):
    data = pd.read_csv(file)
    # Calculate the average measured velocity
    data['average_velocity'] = data['Velocity']
    # The first ~50 data points will always be useless
    data = data.truncate(before = 45)
    # Drop all data from when the throttle is on
    # Drop all the columns where we don't have velocity data
    # Drop data near 0
    #iindex = data[data['average_velocity'] < 4].index
    #data = data.drop(index)
    # Correct time offset
    data['time'] = (data['Time'] - data['Time'].iloc[0])
    # Convert to seconds
    data['time'] = data['time']
    # Adjust and convert to ms
    # Drop unnecessary data
    data = data[['time', 'average_velocity']]
    return data
