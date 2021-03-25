# Module to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# Module to do statistic calculations
import statistics

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
election_csv = os.path.join(dirname, "Resources", "election_data.csv")

#Path to write the result
output_path = os.path.join(dirname,"analysis","result.txt")

totalVotes =0
candidateVotes={}
electionResult=[]
winner = ""
electionResulttxt=""
message ="\n"

#Reading using CSV module
with open(election_csv,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter =",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:

        #Calculates total number of months
        totalVotes +=1   
                
        # Creates candidateVotes dictionary with candidate's surname as index and number of votes as value
        if row[2] not in candidateVotes:
            candidateVotes[row[2]] = 1
        else:
            candidateVotes[row[2]] +=1

    #Create electionResult List
    for candidate, votes in candidateVotes.items():
        electionResult.append("{} : {} ({})".format(candidate,"{:.3%}".format(votes/totalVotes),str(votes)))
        if votes == max(candidateVotes.values()):
            winner = candidate

#Create Election result
for result in electionResult:
    electionResulttxt += f"{result}\n"

#Prepare the result
message = f"\nElection Results\n----------------------------\
    \nTotal Votes : {totalVotes}\n----------------------------\
    \n{electionResulttxt}----------------------------\
    \nWinner : {winner}\n----------------------------"


#print Financial Analysis result into terminal
print(message)

#Write the result into result.txt file
outF = open(output_path,'w')
# Write result using writelines()
outF.writelines(message)
outF.close()
    
