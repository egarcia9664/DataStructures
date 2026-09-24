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
