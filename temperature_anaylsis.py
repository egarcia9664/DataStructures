import json
import os
from pathlib import Path
import numpy as np
import time
import datetime

def load_weather_data():
    with open(os.path.join(Path(__file__).parent.resolve(), 'ep_weather_data.json'), 'r') as file:
        yearly_data = json.load(file)
    return yearly_data

def max(data):
    maximum = data[0]

    for value in data:
        if value > maximum:
            maximum = value

    return maximum

def min(data):
    minimum = data[0]

    for value in data:
        if value < minimum:
            minimum = value

    return minimum

def mean(data):
    total = 0

    for value in data:
        total += value

    return total / len(data)


def monthly_min(month):
    minimum = min(month[0])

    for day in month:
        day_min = min(day)

        if day_min < minimum:
            minimum = day_min

    return minimum

def monthly_max(month):
    maximum = max(month[0])

    for day in month:
        day_max = max(day)

        if day_max > maximum:
            maximum = day_max

    return maximum

def above_90(array):
    return np.sum(array > 90)

def days_above_90(month):
    daily_max = np.max(month, axis=1)
    return above_90(daily_max)
    
def list_test(yearly_data):
    for month in yearly_data:
        monthly_min(month)
        monthly_max(month)

def array_test(yearly_array):
    for month in yearly_array:
        np.min(month)
        np.max(month)
        
def main():
    
    yearly_data = load_weather_data()
    yearly_array = np.array(yearly_data)
    
    september_15 = yearly_data[8][14]
    print("September 15th Min =", min(september_15),
          "Max =", max(september_15),
          "Mean =", mean(september_15))

    january_1 = yearly_data[0][0]
    print("January 1st Min =", min(january_1),
          "Max =", max(january_1),
          "Mean =", mean(january_1))

    december_30 = yearly_data[11][29]
    print("December 30th Min =", min(december_30),
          "Max =", max(december_30),
          "Mean =", mean(december_30))
  
    print()

    print("February Min =", monthly_min(yearly_data[1]),
          "Max =", monthly_max(yearly_data[1]))

    print("August Min =", monthly_min(yearly_data[7]),
          "Max =", monthly_max(yearly_data[7]))
    print()

    september_15_array = yearly_array[8][14]
    print("September 15th Min =", np.min(september_15_array),
          "Max =", np.max(september_15_array),
          "Mean =", np.mean(september_15_array))

    january_1_array = yearly_array[0][0]
    print("January 1st Min =", np.min(january_1_array),
          "Max =", np.max(january_1_array),
          "Mean =", np.mean(january_1_array))

    december_30_array = yearly_array[11][29]
    print("December 30th Min =", np.min(december_30_array),
          "Max =", np.max(december_30_array),
          "Mean =", np.mean(december_30_array))
    print()

    print("February Min =", np.min(yearly_array[1]),
          "Max =", np.max(yearly_array[1]),
          "Mean =", np.mean(yearly_array[1]))

    print("August Min =", np.min(yearly_array[7]),
          "Max =", np.max(yearly_array[7]),
          "Mean =", np.mean(yearly_array[7]))

    print()

    print("There were", days_above_90(yearly_array[4]),
          "days above 90 in May")

    print("There were", days_above_90(yearly_array[7]),
          "days above 90 in August")

    print("There were", days_above_90(yearly_array[10]),
          "days above 90 in November")

    print()

    start = time.time()
    list_test(yearly_data)
    end = time.time()

    print("list test time =", datetime.timedelta(seconds=end-start))

    start = time.time()
    array_test(yearly_array)
    end = time.time()

    print("array test time =", datetime.timedelta(seconds=end-start))
    
main()
