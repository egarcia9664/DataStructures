import json
import os
from pathlib import Path

def load_weather_date():
  with open(os.path.join(Path(__file__).parent.resolve(), 'ep_weather_data.json'), 'r') as file:
        yearly_data = json.load(file)
    return yearly_data

def max(data):
  maximum = data[0]

  for value in data:
    if value > maximum:
        maximum = value

  return maximum

def mind(data):
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

def main():
    yearly_data = load_weather_data()

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

main()
