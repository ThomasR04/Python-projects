import csv
import pandas
#with open("weather_data.csv") as Weather_data:
  #  data = Weather_data.readlines()


#with open("weather_data.csv") as Weather_data:
 #   data = csv.reader(Weather_data)
  #  temperatures = []
   # for row in data:
    #    if row[1] != "temp":
     #       temperatures.append(int(row[1]))

    #print(temperatures)

data =  pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].tolist()
#print(temp_list)

#total = 0
#for temp in temp_list:
 #   temp_to_int = int(temp)
  #  total += temp

#average = total/7
#print(average)

#print(data["temp"].max())

#print(data[data.temp == data.temp.max()])
#mondaytemp = []
#monday = data.temp[0]
#mondaytemp.append(int(monday))
#temp_monday = mondaytemp[0]
#Fahrenheit = temp_monday * 9/5 + 32
#print(Fahrenheit)

# Create dadta frame from scratch
#data_dict = {
 #   "students" : ["Amy", "James", "Angela"],
  #  "Scores": [76,56,65]
#}
#data = pandas.DataFrame(data_dict)
#print(data)


data = pandas.read_csv("squirrel.csv")

grey = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
 "Colors": ["Grey", "Red", "Black"],
  "Count": [grey, Cinnamon, Black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Squirrel_count.csv")
print(data)




