#Griffin Hampton CSE 120 Lab 5

import os
import csv
from Lab5 import *

def searchCsv(file_path, city, month):
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                if cityName == row[0]:
                    if monthName == row[1]:
                        print(f"High temperature of the month: {row[2]}. Low temperature of the month: {row[3]}")
        except StopIteration:
            print("File is empty")

print("Cities in query: Los Angeles, Seattle, Boston, Miami, Chicago")
cityName = input("Enter a city: ")
monthName = input("Enter a month: ")
searchCsv("weather_temps.csv", cityName, monthName)

'''
1: If I opened the file with w it would rewrite the entire file. It would empty the file and add anything you want to add.
You could open it with append (r+) and add to the end of the file among other commands too.
2: I worked by myself.
'''