# Module to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# Module to manipulate date and time
import datetime

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
employee_csv = os.path.join(dirname,"employee_data.csv")

#Path to write the result
output_file = os.path.join(dirname,"employee_final.csv")

# firstName = []
# lastName =[]
# name = []
# dob = []
# year=""
# month=""
# day=""
# ssn = []
# state =[]

firstName = ""
lastName =""
name = []
dob = ""
year=""
month=""
day=""
ssn = ""
state =""
employees=[]


#Python Dictionary to translate US States to Two letter codes
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Reading using CSV module
with open(employee_csv,'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter =",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader) 

      
    # Read each row of data after the header
    for row in csvreader:

        #Name column split into separate First Name and Last Name columns
        name = row[1].split(" ")
        firstName= name[0]
        lastName=name[-1]
        # firstName.append(name[0])
        # lastName.append(name[-1])

        #DOB data re-written into MM/DD/YYYY format
        year=datetime.datetime.strptime(row[2],"%Y-%m-%d").year
        month=datetime.datetime.strptime(row[2],"%Y-%m-%d").month
        day=datetime.datetime.strptime(row[2],"%Y-%m-%d").day

        dob = f"{month}/{day}/{year}"
        # dob.append(f"{month}/{day}/{year}")

        #SSN data re-written to hide the first five numbers from view
        ssn = "***-**-" + row[3][7:11]
        # ssn.append("***-**-" + row[3][7:11])

        #State data re-written as simple two-letter abbreviations
        state = us_state_abbrev [row[4]]
        # state.append(us_state_abbrev [row[4]])

        employees.append([firstName,lastName,dob,ssn,state])

print(employees)

#cleaned_csv= zip(firstName,lastName,dob,ssn,state)


#Write the result into employee_final.csv file
with open(output_file,'w',newline='') as dataFile:
    writer = csv.writer(dataFile)
    
    writer.writerow(["First Name","Last Name","Date of Birth","SSN","State"])
    writer.writerows(employees)
        
    
