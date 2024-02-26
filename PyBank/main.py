import os
import csv

# current_dir = os.getcwd()
budget_csv = os.path.join('Resources','budget_data.csv')

#Create lists to store data
date = []
changes = []  #this list of changes in profit is used for calculating average change sum(changes)/len(changes)

#variables
total_months = 0
total_profit = 0
changes_profit = 0
greatest_increase = 0
greatest_decrease = 0
increase_date = ""
decrease_date = ""

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)  #skip the header row
    data = list(csvreader)

 # When you read in a CSV file using Python's CSV reader, 
 # each row of the CSV file is typically stored as a list where each element in the list corresponds to a column in that row. 
 # when you read this CSV file using the CSV reader, each row will be stored as a list where the first element corresponds to the "Date" column and the second element corresponds to the "Profit/Losses" column.
 # when you read the CSV file and store it in a list called data using data = list(csvreader), 
 # each element in the data list will represent a row from the CSV file, with the elements of that row corresponding to the columns "Date" and "Profit/Losses". 
 # data[i][0] would give you the date value for the ith row, and data[i][1] would give you the profit value for the ith row.


    for i in range(len(data)):
     date.append(data[i][0])
     total_profit = total_profit + int(data[i][1]) #total_profit += int(row[1])     
     total_months += 1
     
     if i > 0:  # because range(x) --> 0,1,2...,x-1, when i = 0, there is no i-1 to compare with
       changes_profit = int(data[i][1]) - int(data[i-1][1])
       changes.append(changes_profit)

    #    greatest_increase=max(changes)
    #    greatest_decrease=min(changes)
    #    increase_date=date[changes.index(greatest_increase)]
    #    decrease_date=date[changes.index(greatest_decrease)]
       if changes_profit > greatest_increase:
          greatest_increase = changes_profit
          increase_date = data[i][0]
       if changes_profit < greatest_decrease:
          greatest_decrease = changes_profit
          decrease_date = data[i][0]

    average_change = sum(changes) / len(changes) # sum() --> add all items in a tuple or list

    #Print the Analysis result
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

    #Export the results to a text file:
    with open('financial_analysis.txt', 'w') as output_file:
       output_file.write("Financial Analysis\n")   #\n is an escape sequence that represents a newline character, it creates a line break in the output
       output_file.write("-----------------------\n")
       output_file.write(f"Total Months: {total_months}\n")
       output_file.write(f"Average Change: ${average_change:.2f}")
       output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
       output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")


       






