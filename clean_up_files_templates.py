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
 
    #chars = ["_", "!", "&", ";", "@", ".", "-"]
    #for char in chars:
        #name = name.replace(char, " ")
        #print(name)

  
# Replace underscore with space
    name = name.replace("_", " ")
    name = name.replace("!", " ")
    name = name.replace("&", " ")
    name = name.replace(";", " ")
    name = name.replace("@", " ")
    name = name.replace("-", " ")
    name = name.replace(".", " ")
    #print(name)

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

# Get the movie titles(everything before the year)
    title_parts =  parts[:parts.index(year)]
    movie_title = " ".join(title_parts).strip().title()
    print(f"The tile is: {movie_title}")
#Get the director (everything after the year)
    name_director = parts[parts.index(year) + 1:]
    movie_dir = " ".join(name_director).strip().title()
    print(f"Director of the movie is: {movie_dir}")

# Format the new file name
    new_name = f"{movie_title} {year} - {movie_dir}{ext}"
    print(new_name) 
    return new_name 

# Process files in the source directory
    for filename in os.listdir(source_directory):
        #print(filename)
        old_path = os.path.join(source_directory, filename)
        if not os.path.isfile(old_path):
            continue
        new_name = normalize_filename(filename)
        print(new_name)

# Define the new path in the new directory
        new_path = os.path.join(new_directory, new_name)
        shutil.copy(old_path, new_path)
        print(f"copied and renamed {filename} -> {new_name}")

        # Check old path
        #if not new_name:



if __name__ == "__main__":
# hardcore function call 
    normalize_filename("star_wars!1977&Lucas.avi")

