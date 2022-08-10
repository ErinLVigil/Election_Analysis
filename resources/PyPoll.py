# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate wom
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 


import datetime as dt

now = dt.datetime.now()
import csv
import os
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# open the election results and read the file.

# with open(file_to_load) as election_data:

# To do: Perform analysis

#close the file
    # print(election_data)

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#with open(file_to_load) as election_data:
        


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:
#To do:: read and analysze the data here
    file_reader = csv.reader(election_data)

   #read and print header rows
    headers = next(file_reader)
    print(headers)
