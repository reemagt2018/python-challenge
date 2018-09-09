import os
import csv
import datetime

# Lists to store data
empid = []
name = []
firstname = []
lastname = []
DOB = []
ssn = []
state=[]
newDOB= []
newssn=[]
stateabbr=[]


with open(r"C:\Users\reema\Desktop\PythonStuff\Employee_Data.csv",  newline="",encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:

        #print(row[0])
        # Add empid
        empid.append(row[0])

        # Add name split name with space
        name.append(row[1])

        # Add DOB
        DOB.append(row[2])

        # Add ssn
        ssn.append(row[3])

        # Add state
        state.append(row[4])

# print (DOB)
# print (empid)
# print(ssn)
# print(name)
# print(state)

for date1 in DOB:

# now convert the string into datetime object given the pattern
    d = datetime.datetime.strptime(date1, "%Y-%m-%d")

# print the datetime in any format you wish.

    newDOB.append(d.strftime("%m/%d/%Y "))

#for ssn in ssn:

for name in name:
    #print(name)
    names = name.split()



    firstname.append(names[0])
    lastname.append(names[1])

for ssn in ssn:
    # print(ssn)
    ssn = ssn.split("-")
    news='***-**-'+(ssn[2])
#    print (ssn[0])
#    print (news)
    newssn.append(news)
#print (newssn)


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

for state in state:
    # print (state)
    # print (f'{us_state_abbrev[state]}')
    stateabbr.append(us_state_abbrev[state])

#print(stateabbr)


# Zip lists together
cleaned_csv = zip(empid, firstname, lastname, newDOB, newssn, stateabbr)

# Set variable for output file
output_file = ("bonus_employee_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
