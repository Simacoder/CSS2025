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
review_data =extract("data/review_data.csv")

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

reviews_series = review_data["App"].isin(subset_apps["App"])

subset_reviews = review_data[reviews_series]

aggregated_reviews = subset_reviews.groupby("App")["Sentiment_Polarity"].mean().reset_index()

joined_apps_reviews = subset_apps.merge(aggregated_reviews, on = "App", how = "left")

filtered_apps_reviews = joined_apps_reviews[["App", 'Rating', "Reviews", "Installs", "Sentiment_Polarity"]]

print(filtered_apps_reviews.info())

# using filtered_apps_reviews based  min-rating and min_reviews

#apps_with_min_rating = 

filtered_apps_reviews["Reviews"] = filtered_apps_reviews["Reviews"].astype(int)

rating_series = filtered_apps_reviews["Reviews"] >= min_rating
apps_with_min_rating = filtered_apps_reviews[rating_series]

reviews_series = apps_with_min_rating["Reviews"] >= min_reviews
top_apps = apps_with_min_rating[reviews_series]

top_apps = top_apps.sort_values(by = ["Rating", "Reviews"], ascending = False).reset_index(drop=True)

# Transorm function
def transform(apps, reviews, category, min_rating, min_reviews):
    # drop any duplicate from both dataframe
    reviews = reviews.drop_duplicates()
    apps = apps.drop_duplices(["App"])

    # Find all of the apps and reviews in the food and drink category
    subset_apps = app.loc[app["Category"] == category]

    return top_apps


# Call the function 
top_apps_data = transform(
    apps = apps_data,
    reviews = reviews_data,
    category = "FOOD_AND_DRINK",
    min_rating = 4.0,
    min_reviews = 1000
)