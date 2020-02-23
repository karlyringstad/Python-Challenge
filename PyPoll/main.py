# Import Dependencies

import os
import csv

# Path to collect data from Desktop
election_data = os.path.join("/Users/karly/Desktop/election_data.csv")

# Candidate names
candidates = []

# Number of votes for each candidate
voting_numbers = []

# Percentage of votes for each candidate
voting_percent = []

# Total number of votes counter
total_votes = 0

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
     # Read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        # Total number of votes 
        total_votes += 1 

        # Add candidates if not in list and a vote for them
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            voting_numbers.append(1)
       
        # Add a vote for candidates already in list
        else:
            index = candidates.index(row[2])
            voting_numbers[index] += 1
    
    # Percentage of votes for each candidate 
    for votes in voting_numbers:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        voting_percent.append(percentage)
    
    # Find election winner
    winner = max(voting_numbers)
    index = voting_numbers.index(winner)
    winning_candidate = candidates[index]

# Print final analysis
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(voting_percent[i])} ({str(voting_numbers[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Output file
text_file = os.path.join("/Users/karly/Desktop/Python-Challenge/PyPoll/PyPoll_Summary.txt")

with open(text_file,"w") as file:
    file.write("Election Results\n")
    file.write("--------------------------\n")
    file.write(f"Total Votes: {str(total_votes)}\n")
    file.write("--------------------------\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {str(voting_percent[i])} ({str(voting_numbers[i])})\n")
    file.write("--------------------------\n")
    file.write(f"Winner: {winning_candidate}\n")
    file.write("--------------------------")



















