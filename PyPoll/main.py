import os
import csv

# define file path
poll_csv = os.path.join('Resources','election_data.csv')

#set variables
vote_count = 0
candidate_list={}
winner_votes=0
winner=""

#Read CSV file
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #skip the header row
    data=list(csvreader)

    #Loop through each row in the csv
    for i in range(len(data)):
        vote_count += 1
        candidate_name = data[i][2]
        #count votes for each candidate
        if candidate_name in candidate_list:
            candidate_list[candidate_name] += 1
        else:
            candidate_list[candidate_name] = 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidate_list.items():   #Python Dictionary items() Method
    percentage = (votes / vote_count) * 100
    candidate_list[candidate] = {"votes": votes, "percentage": percentage}

# Find the winner based on popular vote
for candidate, result in candidate_list.items():
    if result["votes"] > winner_votes:
        winner_votes = result["votes"]
        winner = candidate

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for candidate, data in candidate_list.items():
    print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
folder_path = "/Users/PennyChen/Desktop/2024 UCB Data Boot Camp/Class 7/python---challenge-3/PyPoll/Analysis/"
output_file = "election_results.txt"
# Combine the folder path and file name
file_path = os.path.join(folder_path, output_file)
# Write the content to the text file
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {vote_count}\n")
    file.write("-------------------------\n")
    for candidate, data in candidate_list.items():
        file.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print("Results have been exported to 'election_results.txt'.")


