import csv
with open(r"C:\Users\reema\Desktop\PythonStuff\Budget_Data.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  DatesConsidered = []
  Profit_Loss = []
  Change_data=[]
  previous_amount=0
  total=0
  #next(reader)
  for row in reader:
    #  print(row['Date'], row['Profit/Losses'])
      DatesConsidered.append(row['Date'])
      total=total + int(row['Profit/Losses'])
      Profit_Loss.append(row['Profit/Losses'])
     # print (Profit_Loss)
for Amount_data in Profit_Loss:
    #print(Profit_Loss[Amount_data])
    Change_data.append(int(Amount_data)- previous_amount)
    previous_amount=int(Amount_data)

# Drop the first record as it doesnt show any change
Change_data.pop(0)
#print (Change_data)
max_change=Change_data.index(max(Change_data))
min_change=Change_data.index(min(Change_data))

Date_positive_change=DatesConsidered[max_change + 1]
Date_negative_change=DatesConsidered[min_change + 1]

# print (max_change)
# print (min_change)
# print(Date_positive_change)
# print(Date_negative_change)
total_change=sum(Change_data)
#print (total_change)



DatesConsidered = set(DatesConsidered)
#print (DatesConsidered)
#print (f'No of dates ={len(DatesConsidered)}')
#print (f'total = {total}')
Average=0
Average=total_change/(len(DatesConsidered)-1)
#print("Printing avg", Average)


Header1="Financial Analysis"
Line0="'----------------------------'"
Line1= f'Total Months : {len(DatesConsidered)}'
Line2= f'Total : {total}'
Line3= f'Average  Change : $ {Average} '
Line4=f'Greatest Increase in Profits : {Date_positive_change}   $ {max(Change_data)}'
Line5=f'Greatest Decrease in Profits : {Date_negative_change}  $ {min(Change_data)}'

print (f'{Header1}')
print (f'{Line0}')
print (f'{Line1}')
print (f'{Line2}')
print (f'{Line3}')
print (f'{Line4}')
print (f'{Line5}')


# Set variable for output file
output_file = (r"C:\Users\reema\Desktop\PythonStuff\python-challenge\PyBank\Budget_final.csv")
#
# file1 = open(r"C:\Users\reema\Desktop\PythonStuff\python-challenge\PyBank\Budget_final.csv","w")
# L = ["Header1 \n"]
# file1.close()



#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write in zipped rows
    writer.writerows(Header1)
