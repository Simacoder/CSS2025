# CHPC Summer School 2025
# On your own exercise: Data Handling

# Import packages
import pandas as pd
import os

# Change the file path to where the data is located on your device
os.chdir(r"G:\My Drive\7 Seminars\CHPC summer school\CHPC summer school 2025")
#%%
# Import the data set
coffee = pd.read_csv("CoffeeTruck.csv")

#%%
# How many rows and columns does the dataset have?
rows, columns = coffee.shape

print(f"The data set has {rows} rows and {columns} columns.")

#%%
# List all the variables available in the data set
list(coffee)

#%%
# Unique values in the location variable.
coffee["Location"].unique()

#%%
# Subset the data to include only the observations of sales at the Zoo
coffee_zoo = coffee.loc[coffee["Location"] == "Zoo", :]

#%%
# How many duplicated rows are there in the data?
duplicates = coffee.duplicated(keep = False)
coffee[duplicates]

print(f"The data set has {sum(duplicates)} duplicated rows.")

# Remove the duplicated rows
coffee_nodups = coffee.drop_duplicates(keep = "first")

print(f"There are {coffee_nodups.shape[0]} rows left in the data set after all the duplicated rows are removed")

#%%
# Sort the data set first by profit made (from smallest to largest) and 
# then by music played (from Z to A)

coffee_sorted = coffee_nodups.sort_values(
    by=['Profit', 'Music'],
    ascending=[True, False])

#%%
# Create a new variable called ‘Indicator’ that contains the word 'Loss' 
# if the profit for the day is less than 0, and 'Profit' if the profit 
# for the day is greater than 0. 

def profit_check(amount):
    if amount < 0:
        return "Loss"
    else:
        return "Profit"
    
coffee_sorted["Indicator"] = coffee_sorted["Profit"].apply(profit_check)



