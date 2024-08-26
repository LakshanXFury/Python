# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

### Using CSV import library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if (row[1]) != "temp":
#             temprature.append(int(row[1]))
#     print(temprature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean())  #for average
# print(data["temp"].max()) # for max temp in week

# Get data in Row
# print(data[data.day == "Monday"])
# # print(data[data["day"] == "Monday"])
#
# print(data[data.temp == data.temp.max()])  ##Max temp in week


# #Tap into a value in that particular row
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_f= monday_temp * 9/5 + 32
# print(monday_temp_f)

## Create a data frame from scratch

data_dict = {
    "student": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv") ## To write into a CSV file

