#import necessary modules
import os
import csv
#Read in the CSV data for budget data

csvReader = os.path.join('PyRoll','Resources','election_data.csv')
output_path = os.path.join('PyRoll','Output','Results.txt')

#create variable to count months and List to hold election data
count = 0
votes = [] #sums to hold the values from list

# Define a function to find a unique list of values from a list
def unique(nums):
    list_set = set(nums)
    unique_list = (list(list_set))
    return unique_list

# read in the CSV file and skip the header row
with open(csvReader) as f:
  data = csv.reader(f,delimiter=',')
  csvfile = csv.DictReader(f)
  header = next(data)

# loop through the list to create lists for votes
  for row in data:
        count += 1
        votes.append(str(row[2]))

# Pass votes list to determine a unique list of canditates
UniqueCandidates = unique(votes)

# Create a Dictionary to hold the total votes for each canditate
vote_count = {}.fromkeys(votes, 0)

for x in votes:
    vote_count[x] += 1

# Create a Dictionary to hold the total Vote Percentage for each canditate
vote_percent = {}.fromkeys(votes, 0)

for x in vote_count:
 vote_percent[x] = round(float((vote_count[x]/count)), 4)

# read both results dictionaries into a nested Dictionary to hold percentage and vote count
resultDict = {k: {'Votes':vote_count[k], 'Percent':vote_percent[k]} for k in vote_count.keys() & vote_percent.keys()}

# This will determine be used to determine the election
winner_count = max(vote_count.values()) 

# Summary Results
print("Election Results")
print("-------------------------------")
total = f"Total Votes: {count}"
print(total)
print("-------------------------------")

#loo[ through each candidate to determine display their vote count and percentage
resultsList = [] #read results into a list to be used later in the output file
for x in vote_count:
    Form_percent = "{:.4%}".format(resultDict[x]['Percent'])
    results = f"{x}: {Form_percent} ({resultDict[x]['Votes']})"
    resultsList.append(results)
    print(results)
print("-------------------------------")

#using the winner count variable to determine the winning candidate
for x,y in vote_count.items():
  if y == winner_count:
    winner = f"Winner: {x}"
    print(winner)
print("-------------------------------")

# This will output the final results to a text file Pyroll/Output/Results.txt
with open (output_path, 'w',newline='') as Output:
  Output.writelines("Election Results\n")
  Output.writelines("------------------------------\n")
  Output.writelines(total+"\n")
  Output.writelines("------------------------------\n")
  Output.writelines("%s\n" % x for x in resultsList)
  Output.writelines("------------------------------\n")
  Output.writelines(winner+"\n")
  Output.writelines("------------------------------\n")
