# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data: 
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print (data)
# print (type(data)) pandas data frame
# print(data["temp"]) 
# print(type(data["temp"])) pandas data series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# # average = sum(temp_list) / len(temp_list)

# # print(average) or by using pandas:

# print(data["temp"].mean())
# print(data["temp"].max())


# #get data in Columns
# print(data["condition"])
# print(data.condition)

#get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(monday.temp)

# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32 
# print(monday_temp_F)


data_dict = { 
    "student" : ["snow", " annz"],
    "score" : [99, 100]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")