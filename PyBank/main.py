# Import Dependencies

import os
import csv

# Path to collect data from Downloads folder
budget_data = os.path.join("/Users/karly/Desktop/budget_data.csv")

# Define variables as 
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

    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_prof_loss += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_prof_loss += + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_prof_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
