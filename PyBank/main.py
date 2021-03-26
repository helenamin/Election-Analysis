  
# Module to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# Module to do statistic calculations
import statistics

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
bank_csv = os.path.join(dirname, "Resources", "budget_data.csv")

#Path to write the result
output_path = os.path.join(dirname,"analysis","result.txt")

totalMonths =0
totalProfitLoss =0
previousProfitLoss =0
changes={}
averageChange =0
gip =""
gdp =""
message ="\n"
message_list =[]

#Reading using CSV module
with open(bank_csv,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter =",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:

        #Calculates total number of months
        totalMonths +=1   
        #Calculates the net total amount of "Profit/Losses"
        totalProfitLoss +=int(row[1])   
        
        #Excludes the first row difference(change) as there is no data(ProfitLoss) before that
        if previousProfitLoss !=0 :
            # Creates changes dictionary with date as index and change as value
            changes[row[0]] = int(row[1])-previousProfitLoss
        #Changes previousProfitLoss variable to current ProfitLoss, preparing the variable for next iteration moving down the list
        previousProfitLoss =int(row[1])
    
    

    #Calculates the average change
    averageChange = statistics.mean(changes.values()) 
    
    #finds the greatest increase in profits and greatest decrease in losses (date and amount for both)
    for date, change in changes.items():
        if change == max(changes.values()) :
            gip = "{} (${})".format(date,change)
        if change == min(changes.values()):
            gdp = "{} (${})".format(date,change).replace('$-', '-$')


#Create Financial Analysis result
message_list= ["\n","Financial Analysis","----------------------------",\
    f"Total Months : {str(totalMonths)}",f"Total : ${str(totalProfitLoss)}",\
    "Average Change : ${:.2f}".format(averageChange).replace('$-', '-$'),f"Greatest Increase in Profits : {gip}",\
    f"Greatest Decrease in Profits : {gdp}","----------------------------"]

message = message.join(message_list)

#print Financial Analysis result into terminal
print(message)

#Write the result into result.txt file
outF = open(output_path,'w')
# Write result using writelines()
outF.writelines(message)
outF.close()