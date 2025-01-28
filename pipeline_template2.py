"""
Data Pipeline for ETL

In this code-along, we'll focus on extracting data from flat-files. 
A flat file might be something like a .csv or a .json file. 
The two files that we'll be extracting data from are the apps_data.csv and 
the review_data.csv file. To do this, we'll used pandas. 
Let's take a closer look!

"""

# Import Pandas
import pandas as pd

# Remove warnings
pd.options.mode.chained_assignment = None

# Extract Function
def extract(file_path):

    # Read the file into memory
    data = pd.read_csv(file_path)
    
    # Now, print the details about the file
    print(data.info())
    
    # Print the type of each column
    
    # Finally, print a message before returning the DataFrame
    print("Data has been ingested")
    
    return data


# Call the function (create apps_data and reviews_data)
apps_data = extract("data/apps_data.csv")
reviews_data = extract("data/review_data.csv")


# Transform Function
def transform(apps, reviews, category, min_rating, min_reviews):
    
    # Drop any duplicates from both DataFrames
    reviews_data = reviews.drop_duplicates()
    apps_data = apps.drop_duplicates(subset=["App"])
    
    # Find all of the apps and reviews in the food and drink category
    apps_series = apps_data["Category"] == category

    subset_apps = apps_data[apps_series]

    reviews_series = reviews_data["App"].isin(subset_apps["App"])

    subset_reviews = reviews_data[reviews_series]
    
    
    # Aggregate the subset_reviews DataFrame
    aggregated_reviews = subset_reviews.groupby("App")["Sentiment_Polarity"].mean().reset_index()
    
    
    # Join it back to the subset_apps table
    joined_apps_reviews = subset_apps.merge(aggregated_reviews, on="App", how="left")
 
    # Keep only the needed columns
    filtered_apps_reviews = joined_apps_reviews[["App", "Rating", "Reviews",
                                                 "Installs", 
                                                 "Sentiment_Polarity"]]  
    # Convert reviews to int
    filtered_apps_reviews["Reviews"] = filtered_apps_reviews["Reviews"].astype(int)
 
    # Create series for min rating and filter dataframe with it
    rating_series = filtered_apps_reviews["Rating"] >= min_rating
    
    apps_with_min_rating = filtered_apps_reviews[rating_series]

    # Create series for min reviews and filter dataframe with it
    reviews_series = apps_with_min_rating["Reviews"] >= min_reviews
    
    top_apps = apps_with_min_rating[reviews_series]
    
    # Sort dataframe
    top_apps = top_apps.sort_values(by=["Rating","Reviews"]
                                    ,ascending=False).reset_index(drop=True)
    
    #Persist and convert the df top_apps as a csv file

    top_apps.to_csv("data/top_apps.csv")
    # Return the transformed DataFrame
    print("data transformed")
    
    return top_apps
    
# Call the function
top_apps_data = transform(
    apps=apps_data, 
    reviews=reviews_data,
    category="FOOD_AND_DRINK",
    min_rating=4.0,
    min_reviews=1000)

# Show the data
print(top_apps_data)

# import sqlite
import sqlite3
# load function
def load(dataframe, database_name, table_name):
    # create a connection object
    con = sqlite3.connect(database_name) 
    # Write the data to the specified table
    dataframe.to_sql(name = table_name, con = con, if_exists = "replace", index = False)
    print("Original dataframe have been loaded to sqlite\n")

    # read the data , and return the result 
    loaded_dataframe = pd.read_sql(sql = f"SELECT * FROM {table_name}", con = con)
    print("The loaded dataframe has been read from Sqlite\n")
    """
     print(dataframe.shape)
     print(loaded_dataframe.shape)
    """
    if (dataframe.shape) == (loaded_dataframe.shape):
        print('The shape is the same')
    else:
        print("The shaep are diffrent")
    # add the try/except to handle error handling and assert to check for conditions
    #try:



# Call the function
load(
    dataframe = top_apps_data,
    database_name = "market_research",
    table_name = "top_apps"
)
