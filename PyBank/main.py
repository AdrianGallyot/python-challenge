#import necessary modules
import os
import csv
#Read in the CSV data for budget data
csvReader = os.path.join('PyBank','Resources','budget_data.csv')
output_path = os.path.join('PyBank','Output','Results.txt')
#create variable to count months and List to hold budget data
count = 0 #Count the number of row and months in list
sums = [] #sums to hold the values from list
Vals = [] #sum 
# Define a function to find the difference between consecutive values in a list of numeric value
def diff_nums(nums):
    result = [b-a for a, b in zip(nums[:-1], nums[1:])]
    return result

# read in the CSV file and skip the header row
with open(csvReader) as f:
  data = csv.reader(f,delimiter=',')
  csvfile = csv.DictReader(f)
  header = next(data)

# loop through the list to create lists and count the number of months
  for row in data:
        count += 1
        sums.append(int(row[1]))
        Vals.append(str(row[0]))


# Summary Calculations

sumstotal = int(sum(sums)) #create Sum total of all Profit/Loss Values
CalcAvg = diff_nums(sums) #Using the Diffnums function to create a list of difference values from original list
AvgChange = round(int(sum(CalcAvg)) / len(CalcAvg), 2) # Calculating the Average change using difference list above
max_value = max(CalcAvg) # find the max value if the difference list
min_value = min(CalcAvg) # find the minimum value of the difference list
max_new = CalcAvg.index(max_value) # Find the index number of maximum value
min_new = CalcAvg.index(min_value) # Find the index number of minimum value

#Display summary results - Will need to add one to the index numbers 
print("Financial Analysis")
print("-------------------------------")
totalmonths = f"Total Months: {count}"
SumValues = f"Total:  $ {sumstotal}"
AverageChange = f"Average Change: {AvgChange}"
Increase = f"Greatest Increase in Profits: {Vals[max_new + 1]} (${max_value})"
Decrease = f"Greatest decrease in Profits: {Vals[min_new + 1]} (${min_value})"


print(totalmonths)
print(SumValues)
print(AverageChange)
print(Increase)
print(Decrease)

with open (output_path, 'w',newline='') as Output:
      #Initialize csv.writer
     Output.writelines("Financial Analysis \n")
     Output.writelines("------------------------------- \n")
     Output.writelines(totalmonths+"\n")
     Output.writelines(SumValues+"\n")
     Output.writelines(AverageChange+"\n")
     Output.writelines(Increase+"\n")
     Output.writelines(Decrease+"\n")