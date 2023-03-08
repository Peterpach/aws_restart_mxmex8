import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}


for key, value in myVehicle.items():
    print(f"{key} : {value}")

myInventoryList = []

#with open('car_fleet.csv') as csvFile:

for i in range(0,101,2):
    print(i)