"""
    Data Pipeline for ETL
    In this code- a long, we'll focus on extracting data from flat-files.
    A flat file might be something like a .csv or a .json file.
    The two files that we'll be extracting data from are the app_data.csv
    and the review_data.csv file. To do this , we'll used pandas. let's take a closer look!

"""
# Import Pandas
import pandas as pd
import os

#os.path.exists()
#import toolbox

# Ingest these dataset into memory using read_csv and save as app and reviews variable
apps = pd.read_csv("data/apps_data.csv")
reviews = pd.read_csv("data/review_data.csv")

# Take peak at the two data sets with print function
# 
# # View the columns , shape and data types
# 
print(apps.columns)
print(apps.shape)
print(apps.dtypes) 

# Is there a single pandas method that does this
print(apps.info())

# Can you see the data in variable explorer

# Extract Function
def extract(file_path):
    # Read the file into memory
    data = pd.read_csv(file_path)

    # Now, print the details about the file
    print(data.info())
    # Finally, print a message before returning the Dataframe
    print("Data has been ingested!!")

    return data

# Call the function (create apps_data and reviews_data)
apps_data = extract("data/apps_data.csv")
review_data =extract("data/apps_data.csv")

# Take a peek at one of the dataframe

print(apps_data["Category"].unique())

category = "FOOD_AND_DRINK"
min_rating = 4.0
min_reviews = 1000

reviews_data = review_data.drop_duplicates()
apps_data = apps_data.drop_duplicates(subset=["App"])

apps_series = apps_data["Category"] == category
print(apps_series)

#subset_apps = apps_data
subset_apps = apps_data[apps_series]
print(subset_apps.head())