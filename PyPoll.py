# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counte
total_votes = 0

# Initialize a list of candidate options
candidate_options = []

# Initialize an empty dictionary for individual candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    
    # Read and Print the header row
    headers = next(file_reader)
    # #print(headers)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate add to the list of candidates
        if candidate_name not in candidate_options:
        
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        
            # Track the candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add to the total vote count
        total_votes += 1
        
        # Add to the candidate vote count
        candidate_votes[candidate_name] += 1


# Print the cancidate list
# print(candidate_options)

# Print the candidate vote dictionary
# print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retrieve vote cound for the candidate
    votes = candidate_votes[candidate_name]
    
    # Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    
    # Print the candidate name and percentage of votes
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"------------------------\n")
    txt_file.write(election_results)


    for candidate_name in candidate_votes:
        # Retrieve vote cound for the candidate
        votes = candidate_votes[candidate_name]
    
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")     
        txt_file.write(candidate_results)   
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    txt_file.write(winning_candidate_summary)

    


