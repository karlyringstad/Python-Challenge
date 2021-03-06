# Import Dependencies

import os
import csv

# Path to collect data from Desktop
budget_data = os.path.join("/Users/karly/Desktop/budget_data.csv")

# Define variables as counters and lists
total_months = 0
total_prof_loss = 0
value = 0
change = 0
dates = []
profits = []

# Open and read the CSV file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the header row first
    csv_header = next(csvreader)

    # Read the first row 
    first_row = next(csvreader)
    
    # Total number of months
    total_months += 1
    
    # Net total amount of Profits/Losses
    total_prof_loss += int(first_row[1])
    value = int(first_row[1])
    
    # Loop through each row of data after header and first row
    for row in csvreader:
        
        # Keep track of dates
        dates.append(row[0])
        
        # Calculate the change and add to changes list
        prof_loss_change = int(row[1])-value
        profits.append(prof_loss_change)
        value = int(row[1])
        
        # Total number of months
        total_months += 1

        # Net total amount of Profits/Losses
        total_prof_loss += + int(row[1])

    # Greatest increase in profits
    greatest_inc = max(profits)
    greatest_index = profits.index(greatest_inc)
    greatest_date = dates[greatest_index]

    # Greatest decrease in profits 
    greatest_dec = min(profits)
    worst_index = profits.index(greatest_dec)
    worst_date = dates[worst_index]

    # Average of the changes in Profits/Losses
    avg_change = sum(profits)/len(profits)
    

# Print final analysis
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_prof_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_dec)})")

# Output file
text_file = os.path.join("/Users/karly/Desktop/Python-Challenge/PyBank/Pybank_Summary.txt")

with open(text_file,"w") as file:

    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write(f"Total Months: {str(total_months)}\n")
    file.write(f"Total: ${str(total_prof_loss)}\n")
    file.write(f"Average Change: ${str(round(avg_change,2))}\n")
    file.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_inc)})\n")
    file.write(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_dec)})\n")