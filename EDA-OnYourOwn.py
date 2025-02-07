# CHPC Summer School 2025
# On your own exercise: Exploratory Data Analysis

# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(r"G:\My Drive\7 Seminars\CHPC summer school\CHPC summer school 2025")
#%%
# Import the data set
coffee = pd.read_csv("CoffeeTruck.csv")

#%%
# Draw a frequency table of the ‘Location’ variable
location_freq = coffee["Location"].value_counts()

print(f"The coffee truck stopped at the {location_freq.idxmax()} the most frequently.")

#%%
# Create a new variable called ‘Indicator’ that contains the word 'Loss' 
# if the profit for the day is less than 0, and 'Profit' if the profit 
# for the day is greater than 0. 

def profit_check(amount):
    if amount < 0:
        return "Loss"
    else:
        return "Profit"
    
coffee["Indicator"] = coffee["Profit"].apply(profit_check)

#%%
# Draw a frequency table of the ‘Music’ variable and the new 
# “Indicator” variable.

twoway = pd.crosstab(coffee["Music"], coffee["Indicator"])

#%%
# Draw a histogram of the profits made.

prof = sns.histplot(data = coffee, x = "Profit",
                    color = "green",
                    edgecolor = "black",
                    bins = 20)
prof.set(ylabel = "Frequency",
         title = "Histogram of the profits made by the coffee truck")
plt.show()

#%%
# Draw a barplot of the ‘Music’ variable
music_freq = coffee["Music"].value_counts()

mus = sns.barplot(x=music_freq.index, y=music_freq.values)
mus.set(ylabel = "Frequency",
         title = "Barplot of the music played at the coffee truck")
plt.show()

#%%
# Draw a side-by-side boxplot of the profit per location
sns.boxplot(data = coffee, x = "Profit", y = "Location")

#%%
# Obtain numerical summaries of the profit for each location

sum_profit = coffee.groupby(["Location"])["Profit"].describe()

#%%
# BONUS: What is the mean number of sales at the Zoo when the coffee truck 
# made a profit for the day?

coffee_zoo_profit = coffee.loc[(coffee["Location"] == "Zoo") & 
                               (coffee["Indicator"] == "Profit"), :]

mean_sales = coffee_zoo_profit["Sales"].mean()
print(f"The mean number of sales at the Zoo on days where the coffee truck made a profit is: {round(mean_sales,4)}")


