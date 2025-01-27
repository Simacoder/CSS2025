# Import the libraries
# We have: star_wars!1977&Lucas.avi
# We want: Star Wars (1977) - Lucas.mp4

import os
import shutil

# Define the directory containing the messy files
source_directory = "./messy_movie_files"
new_directory = "./renamed_movie_files"

# Ensure the directory exists
if not os.path.exists(source_directory):
    print("Directory ayikho!!")

if not os.path.exists(new_directory):
    print("Directory ayikho!!")
    os.makedirs(new_directory)

# Function to normalises file names
def normalize_filename(filename):
    # Remove the file extension
    name, ext = os.path.splitext(filename)
    print(f"Name: {name} Extension:  {ext}")



# Replace common separators with spaces
# for loop 
    chars = ["_", "!", "&", ";", "@"]
    for char in chars:
        name = name.replace(char, " ")
        print(name)
# Replace underscore with space
#    name = name.replace("_", " ")
#    name = name.replace("!", " ")
#    name = name.replace("&", " ")
#    name = name.replace(";", " ")
#    name = name.replace("@", " ")
#    print(name)

    parts = name.split()
    print(parts)

    year = None
    for part in parts:
        if part.isdigit() and len(part) == 4:
            year = part
            print(f"Year found: {year}")
            break
    if not year:
        print(f"Skipping: {filename} - no year")
        return None

# hardcore function call 
normalize_filename("star_wars!1977&Lucas.avi")

