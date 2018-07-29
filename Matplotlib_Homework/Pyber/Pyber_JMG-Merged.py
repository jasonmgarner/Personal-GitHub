%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_data = "data/city_data.csv"
ride_data = "data/ride_data.csv"

# Read the City and Ride Data
City_Data_df = pd.read_csv(city_data)
Ride_Data_df = pd.read_csv(ride_data)


# Combine the data into a single dataset
City_Ride = Ride_Data_df.merge(City_Data_df, on='city')

## Display the data table for preview
City_Ride.head()

## Bubble Plot of Ride Sharing Data

# Obtain the x and y coordinates for each of the three city types
#Average Fare, Total Number of Rides(Per City)
City_Type = City_Ride.groupby(['type', "city"])
City_Type.head()

Total_Fare = City_Type["fare"].sum()
City_Count = City_Type["city"].count()
Avg_Fare = Total_Fare / City_Count
Avg_Fare

Total_Ride = City_Type["ride_id"].count()
Total_Ride

Driver_Count = City_Type["driver_count"].value_counts()
Driver_Count

Urban_Scatter = plt.scatter(City_Count["Urban"], Avg_Fare["Urban"], s=Driver_Count['Urban']*10, c="coral", label="Urban", marker="o", edgecolors="black", alpha=0.75)
Rural_Scatter = plt.scatter(City_Count["Rural"], Avg_Fare["Rural"], s=Driver_Count["Rural"]*10, c="gold", label="Rural", marker="o", edgecolors="black", alpha=0.75)
Suburban_Scatter = plt.scatter(City_Count["Suburban"], Avg_Fare["Suburban"], s=Driver_Count["Suburban"]*10, c="lightskyblue", label="Suburban", marker="o", edgecolors="black", alpha=0.75)

plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")


legend = plt.legend(title="City Types", fontsize="small", loc="upper right")
plt.grid()
legend.legendHandles[0]._sizes = [30]
legend.legendHandles[1]._sizes = [30]
legend.legendHandles[2]._sizes = [30]

plt.gcf().text(.95, 0.5, "Note: Circle size correlates with driver count per city", fontsize=12)

plt.savefig('Pyber_Scatter_Plot.png')
plt.show()

## Total Fares by City Type

# Calculate Type Percents
Total_Rural_Fares = sum(Total_Fare["Rural"])
Total_Sum_Fares = sum(Total_Fare)
Rural_Percent_Fares = Total_Rural_Fares / Total_Sum_Fares * 100

Total_Urban_Fares = sum(Total_Fare["Urban"])
Urban_Percent_Fares = Total_Urban_Fares / Total_Sum_Fares * 100

Total_Suburban_Fares = sum(Total_Fare["Suburban"])
Suburban_Percent_Fares = Total_Suburban_Fares / Total_Sum_Fares * 100

labels = ["Urban", "Suburban", "Rural"]
sizes = [Urban_Percent_Fares, Rural_Percent_Fares, Suburban_Percent_Fares]
colors = "lightcoral", "gold", "lightskyblue"
explode = (.1, 0, 0)

plt.pie(sizes, labels=labels, colors=colors, 
        autopct="%1.1f%%", startangle=-75, shadow=True, explode=explode)
plt.title("% of Total Fares by City Type")

plt.savefig("Percent Fares by City Type.png")
plt.show()

## Total Rides by City Type

# Calculate Ride Percents
Total_Rural_Rides = sum(Total_Ride["Rural"])
Total_Sum_Rides = sum(Total_Ride)
Rural_Percent_Rides = Total_Rural_Rides / Total_Sum_Rides * 100

Total_Suburban_Rides = sum(Total_Ride["Suburban"])
Suburban_Percent_Rides = Total_Suburban_Rides / Total_Sum_Rides * 100

Total_Urban_Rides = sum(Total_Ride["Urban"])
Urban_Percent_Rides = Total_Urban_Rides / Total_Sum_Rides * 100


labels = ["Urban", "Suburban", "Rural"]
colors = "lightcoral", "gold", "lightskyblue"
explode = (.1, 0, 0)
sizes = [Urban_Percent_Rides, Rural_Percent_Rides, Suburban_Percent_Rides]

plt.pie(sizes, labels=labels, colors=colors, 
        autopct="%1.1f%%", startangle=-100, shadow=True, explode=explode)
plt.title("% of Total Rides by City Type")

plt.savefig("Percent Total Rides by City Type")
plt.show()

## Total Drivers by City Type

# Calculate Driver Percents
Total_Drivers = sum(Driver_Count)

Rural_Percent_Drivers = Driver_Count["Rural"].sum() / Total_Drivers * 100
Suburban_Percent_Drivers = Driver_Count["Suburban"].sum() / Total_Drivers * 100
Urban_Percent_Drivers = Driver_Count["Urban"].sum() / Total_Drivers * 100

labels = ["Urban", "Suburban", "Rural"]
colors = "lightcoral", "gold", "lightskyblue"
explode = (.1, 0, 0)
sizes = [Urban_Percent_Drivers, Rural_Percent_Drivers, Suburban_Percent_Drivers]

plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=-135, shadow=True, explode=explode)
plt.title("% of Total Drivers by City Type")

plt.savefig("Percent Total Driver by City Type")
plt.show()
