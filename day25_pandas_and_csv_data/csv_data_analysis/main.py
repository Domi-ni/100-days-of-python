'''
working with csv:
import csv

with open("./weather_data.csv") as csv_data_file:
    data = csv.reader(csv_data_file)
    temperatures = []
    for row in data:
        temperature = row[1]
        if temperature != "temp":
            temperatures.append(int(temperature))
    print(temperatures)
'''

#working with pandas

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print("\n")
print(data["temp"])
