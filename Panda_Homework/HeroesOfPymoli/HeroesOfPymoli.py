
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)


## Player Count

* Display the total number of players


All_Items = len(purchase_data["SN"])

Total_Players = len(purchase_data["SN"].unique())
Total_Players_df = pd.DataFrame({"Unique Players": [Total_Players]}, index=["Purchase Data"])
Total_Players_df

Dropped_Duplicates = purchase_data.drop_duplicates("SN")

Player_Names = Dropped_Duplicates[["SN"]]

Players_Names_df = Player_Names.rename(columns={"SN":"Unique Player Names"})

Players_Names_df.head()


## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


Dropped_Duplicates = purchase_data.drop_duplicates("SN")
#print(Dropped_Duplicates)

Unique_Items = len(purchase_data["Item ID"].unique())
#Unique_Items

Average_Price = sum(purchase_data["Price"]) / len(purchase_data["Price"])

Total_Purchases = len(purchase_data["Item ID"])
#Total_Purchases

Total_Revenue = sum(purchase_data["Price"])
Total_Revenue

Average_Age = sum(Dropped_Duplicates["Age"]) / len(Dropped_Duplicates["Age"])

#Summary_Data_df["Average Age"] = Summary_Data_df["Average Age"].map("{:}".format)
#Summary_Data_df["Average Price"] = Summary_Data_df["Average Price"].map("${:,.2f}".format)
                                      
Summary_Data_df = pd.DataFrame({"Number of Unique Items": [Unique_Items], 
                                "Average Price": [Average_Price], "Average Age": [Average_Age], 
                               "Number of Purchases": [Total_Purchases], 
                               "Total Revenue": [Total_Revenue]}, index=["Purchasing Analysis"])

Summary_Data_df["Average Age"] = Summary_Data_df["Average Age"].map("{:,.0f}".format)
Summary_Data_df["Average Price"] = Summary_Data_df["Average Price"].map("${:,.2f}".format)
Summary_Data_df["Total Revenue"] = Summary_Data_df["Total Revenue"].map("${:,.2f}".format)


Summary_Data_df = Summary_Data_df[["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue", "Average Age"]]

Summary_Data_df


## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed




Gender_Count = Dropped_Duplicates['Gender'].value_counts()
#Gender_Count

Male_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Gender == 'Male', 'Gender'].count()
#Male_Count

Female_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Gender == 'Female', 'Gender'].count()
#Female_Count

Other_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Gender == 'Other / Non-Disclosed', 'Gender'].count()
#Other_Count

Total_Count = Male_Count + Female_Count + Other_Count
#Total_Count

Male_Percent = 100. * Male_Count / Total_Count
#Male_Percent

Female_Percent = 100. * Female_Count / Total_Count

Other_Percent = 100. * Other_Count / Total_Count
 
Gender_Index = ["Male", "Female", "Other / Non-Disclosed"]

Gender_df = pd.DataFrame({"Gender Count": [Male_Count, Female_Count, Other_Count], 
                          "Gender Percent": [Male_Percent, Female_Percent, Other_Percent]}, 
                         index=Gender_Index)

Gender_df["Gender Percent"] = Gender_df["Gender Percent"].map("{:.2f}%".format)


Gender_df 




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

Purchase_Count = len(purchase_data ["Item Name"])

Male_Purchases = purchase_data.loc[(purchase_data["Gender"] == "Male")]

Purchase_Male_Count = len(Male_Purchases["Gender"])

Avg_Male_Purchases = Male_Purchases["Price"].sum() / Purchase_Male_Count

Avg_Male_Total = Purchase_Male_Count / Male_Count

Female_Purchases = purchase_data.loc[(purchase_data["Gender"] == "Female")]

Purchase_Female_Count = len(Female_Purchases["Gender"])

Avg_Female_Purchases = Female_Purchases["Price"].sum() / Purchase_Female_Count

Avg_Female_Total = Purchase_Female_Count / Female_Count

Other_Purchases = purchase_data.loc[(purchase_data["Gender"] == "Other / Non-Disclosed")]

Purchase_Other_Count = len(Other_Purchases["Gender"])

Avg_Other_Purchases = Other_Purchases["Price"].sum() / Purchase_Other_Count

Avg_Other_Total = Purchase_Other_Count / Other_Count

Male_Total_Purchase_Value = Purchase_Male_Count * Avg_Male_Purchases

Female_Total_Purchase_Value = Purchase_Female_Count * Avg_Female_Purchases

Other_Total_Purchase_Value = Purchase_Other_Count * Avg_Other_Purchases


Gender_Purchase_df = pd.DataFrame({"Purchase Count": [Purchase_Male_Count, Purchase_Female_Count, Purchase_Other_Count], 
                                   "Avg Purchase Price": [Avg_Male_Purchases, Avg_Female_Purchases, Avg_Other_Purchases], 
                                   "Avg Items Purchased Per Player": [Avg_Male_Total, Avg_Female_Total, Avg_Other_Total],
                                  "Total Purchase Value": [Male_Total_Purchase_Value, Female_Total_Purchase_Value, 
                                    Other_Total_Purchase_Value]}, index=Gender_Index)

Gender_Purchase_df["Avg Items Purchased Per Player"] = Gender_Purchase_df["Avg Items Purchased Per Player"].map("{:.2f}".format)
Gender_Purchase_df["Avg Purchase Price"] = Gender_Purchase_df["Avg Purchase Price"].map("${:.2f}".format)
Gender_Purchase_df["Total Purchase Value"] = Gender_Purchase_df["Total Purchase Value"].map("${:.2f}".format)

Gender_Purchase_df

## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table


# Establish bins for ages
Age_Bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
Group_Names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age_Group"] = pd.cut(purchase_data["Age"], Age_Bins, labels = Group_Names)
Dropped_Duplicates["Age_Group"] = pd.cut(purchase_data["Age"], Age_Bins, labels = Group_Names)



Sub_Ten_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "<10")])
Sub_Ten_Percent = Sub_Ten_Purchase / All_Items * 100

Ten_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "10-14")])
Ten_Percent = Ten_Purchase / All_Items * 100

Fifteen_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "15-19")])
Fifteen_Percent = Fifteen_Purchase / All_Items * 100

Twenty_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "20-24")])
Twenty_Percent = Twenty_Purchase / All_Items * 100
                             
Twenty_Five_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "25-29")])
Twenty_Five_Percent = Twenty_Five_Purchase / All_Items * 100

Thirty_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "30-34")])
Thirty_Percent = Thirty_Purchase / All_Items * 100

Thirty_Five_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "35-39")])
Thirty_Five_Percent = Thirty_Five_Purchase / All_Items * 100

Forty_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "40+")])
Forty_Percent = Forty_Purchase / All_Items * 100

Age_Index = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

Age_Demographics_df = pd.DataFrame({"Purchase Count": [Sub_Ten_Purchase, Ten_Purchase, 
                                                        Fifteen_Purchase, Twenty_Purchase, 
                                                        Twenty_Five_Purchase, Thirty_Purchase, 
                                                        Thirty_Five_Purchase, Forty_Purchase], 
                                    "Purchase Percent": [Sub_Ten_Percent, Ten_Percent, Fifteen_Percent, 
                                                         Twenty_Percent, Twenty_Five_Percent, Thirty_Percent, 
                                                         Thirty_Five_Percent, Forty_Percent]}, index=Age_Index)


Age_Demographics_df["Purchase Percent"] = Age_Demographics_df["Purchase Percent"].map("{:.2f}%".format)

Age_Demographics_df

## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame

Age_Bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
Group_Names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

Sub_Ten_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '<10', 'Age_Group'].count()
Sub_Ten_Total = purchase_data.loc[(purchase_data["Age_Group"] == "<10")]
Sub_Ten_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "<10")])
Avg_Sub_Ten_Purchases = Sub_Ten_Total["Price"].sum() / Sub_Ten_Purchase
Avg_Sub_Ten_Total = Sub_Ten_Purchase / Sub_Ten_Count
Sub_Ten_Total_Purchase_Value = Sub_Ten_Purchase * Avg_Sub_Ten_Purchases

Ten_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '10-14', 'Age_Group'].count()
Ten_Total = purchase_data.loc[(purchase_data["Age_Group"] == "10-14")]
Ten_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "10-14")])
Avg_Ten_Purchases = Ten_Total["Price"].sum() / Ten_Purchase
Avg_Ten_Total = Ten_Purchase / Ten_Count
Ten_Total_Purchase_Value = Ten_Purchase * Avg_Ten_Purchases

Fifteen_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '15-19', 'Age_Group'].count()
Fifteen_Total = purchase_data.loc[(purchase_data["Age_Group"] == "15-19")]
Fifteen_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "15-19")])
Avg_Fifteen_Purchases = Fifteen_Total["Price"].sum() / Fifteen_Purchase
Avg_Fifteen_Total = Fifteen_Purchase / Fifteen_Count
Fifteen_Total_Purchase_Value = Fifteen_Purchase * Avg_Fifteen_Purchases

Twenty_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '20-24', 'Age_Group'].count()
Twenty_Total = purchase_data.loc[(purchase_data["Age_Group"] == "20-24")]
Twenty_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "20-24")])
Avg_Twenty_Purchases = Twenty_Total["Price"].sum() / Twenty_Purchase
Avg_Twenty_Total = Twenty_Purchase / Twenty_Count
Twenty_Total_Purchase_Value = Twenty_Purchase * Avg_Twenty_Purchases

Twenty_Five_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '25-29', 'Age_Group'].count()
Twenty_Five_Total = purchase_data.loc[(purchase_data["Age_Group"] == "25-29")]
Twenty_Five_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "25-29")])
Avg_Twenty_Five_Purchases = Twenty_Five_Total["Price"].sum() / Twenty_Five_Purchase
Avg_Twenty_Five_Total = Twenty_Five_Purchase / Twenty_Five_Count
Twenty_Five_Total_Purchase_Value = Twenty_Five_Purchase * Avg_Twenty_Five_Purchases

Thirty_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '30-34', 'Age_Group'].count()
Thirty_Total = purchase_data.loc[(purchase_data["Age_Group"] == "30-34")]
Thirty_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "30-34")])
Avg_Thirty_Purchases = Thirty_Total["Price"].sum() / Thirty_Purchase
Avg_Thirty_Total = Thirty_Purchase / Thirty_Count
Thirty_Total_Purchase_Value = Thirty_Purchase * Avg_Thirty_Purchases

Thirty_Five_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '35-39', 'Age_Group'].count()
Thirty_Five_Total = purchase_data.loc[(purchase_data["Age_Group"] == "35-39")]
Thirty_Five_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "35-39")])
Avg_Thirty_Five_Purchases = Thirty_Five_Total["Price"].sum() / Thirty_Five_Purchase
Avg_Thirty_Five_Total = Thirty_Five_Purchase / Thirty_Five_Count
Thirty_Five_Total_Purchase_Value = Thirty_Five_Purchase * Avg_Thirty_Five_Purchases

Forty_Count = Dropped_Duplicates.loc[Dropped_Duplicates.Age_Group == '40+', 'Age_Group'].count()
Forty_Total = purchase_data.loc[(purchase_data["Age_Group"] == "40+")]
Forty_Purchase = len(purchase_data.loc[(purchase_data["Age_Group"] == "40+")])
Avg_Forty_Purchases = Forty_Total["Price"].sum() / Forty_Purchase
Avg_Forty_Total = Forty_Purchase / Forty_Count
Forty_Total_Purchase_Value = Forty_Purchase * Avg_Forty_Purchases


Age_Index = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

Age_Purchases_df = pd.DataFrame({"Purchase Count": [Sub_Ten_Purchase, Ten_Purchase, 
                                                        Fifteen_Purchase, Twenty_Purchase, 
                                                        Twenty_Five_Purchase, Thirty_Purchase, 
                                                        Thirty_Five_Purchase, Forty_Purchase],
                                 "Avg Purchase Price": [Avg_Sub_Ten_Purchases, Avg_Ten_Purchases, 
                                                         Avg_Fifteen_Purchases, Avg_Twenty_Purchases, 
                                                         Avg_Twenty_Five_Purchases, Avg_Thirty_Purchases, 
                                                         Avg_Thirty_Five_Purchases, Avg_Forty_Purchases], 
                                 "Avg Items Purchased": [Avg_Sub_Ten_Total, Avg_Ten_Total, Avg_Fifteen_Total, 
                                                        Avg_Twenty_Total, Avg_Twenty_Five_Total, Avg_Thirty_Total, 
                                                        Avg_Thirty_Five_Total, Avg_Forty_Total], 
                                "Total Purchase Value": [Sub_Ten_Total_Purchase_Value, Ten_Total_Purchase_Value, 
                                                         Fifteen_Total_Purchase_Value, Twenty_Total_Purchase_Value, 
                                                         Twenty_Five_Total_Purchase_Value, Thirty_Total_Purchase_Value, 
                                                         Thirty_Five_Total_Purchase_Value, Forty_Total_Purchase_Value]}, 
                                                         index=Age_Index)

Age_Purchases_df["Avg Items Purchased"] = Age_Purchases_df["Avg Items Purchased"].map("{:.2f}".format)
Age_Purchases_df["Avg Purchase Price"] = Age_Purchases_df["Avg Purchase Price"].map("${:.2f}".format)
Age_Purchases_df["Total Purchase Value"] = Age_Purchases_df["Total Purchase Value"].map("${:.2f}".format)

Age_Purchases_df

## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame





#purchase_data.groupby(['SN', 'Price']).sum().reset_index()

Spenders = purchase_data[["SN", "Price", "Item ID"]]

Spenders_df = pd.DataFrame(Spenders)

#Spenders_df
#Grouped_SN = Spenders_df.groupby(['SN'])
   
Top_Spenders = Spenders_df.groupby(["SN"])
Top_Spenders_Total = Top_Spenders["Price"].sum()
Top_Spenders_Count = Top_Spenders["Item ID"].count()
Top_Spenders_Avg = Top_Spenders_Total / Top_Spenders_Count

Top_Spenders_df = pd.DataFrame({"Purchase Count": [Top_Spenders_Count], "Average Purchase Price": [Top_Spenders_Avg],
                                "Total Purchase Value": [Top_Spenders_Total]})
                                
Top_Spenders_df
#Top_Spenders_Count = Spenders_df.groupby("SN").count()
#Top_Spenders_Avg = 

#print(Top_Spenders_Count)

#Top_Spenders = purchase_data.reset_index().groupby("SN").sum()

#Top_Spenders_Sort = Top_Spenders.sort_values("Price", ascending=False)

#Top_Spenders_Sort.head()

## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame



#Count amount each item purchased
#Find price of each item: total price / count amount
#total purchase amount of each item


#Popular_Table = purchase_data.loc[:, ["Item ID", "Item Name", "Price"]]
#Popular_Table

#Item_Name_Counts = purchase_data["Item Name"].value_counts()
#Item_ID_Counts = purchase_data["Item ID"].value_counts()
#print(Item_Name_Counts)


Popular_Table = purchase_data[["Item ID", "Item Name", "Price"]]


Grouped_Popular_Table = Popular_Table.groupby(["Item Name", "Item ID"])
#Grouped_Popular_Table_1 = pd.DataFrame(Grouped_Popular_Table, columns=["Item Name", "Item ID", "Price"])



#Combined = pd.DataFrame(Grouped_Popular_Table.size().reset_index(name = "Item Count"))
#Combined

#Merged_Table = pd.merge(Grouped_Popular_Table, Combined, on="Item ID")
#Merged_Table


#Grouped_Popular_Table["Amount Purchased"] = Item_Name_Counts

#Grouped_Popular_Table

#Total_Item_Value = Grouped_Popular_Table["Price"].sum()

#Total_Item_Value

###Total_Item_Value["Item Price"] = Total_Item_Value[""]



#Grouped_Popular_Table["Item Name"] = pd.to_numeric(Grouped_Popular_Table)

#Grouped_Popular_Table.count()


## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




